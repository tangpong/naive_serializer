import unittest
from typing import Any
from dataclasses import dataclass
from serializer.fields import BasicField
from serializer.encoders import ShortBinaryEncoder, CharBinaryEncoder, UTF8Encoder


@dataclass
class Values:
    input: Any
    expected: Any


class TestBasicField(unittest.TestCase):
    def test_field_encode(self):
        expected = {
            CharBinaryEncoder: Values(input=1, expected=b'\x01'),
            ShortBinaryEncoder: Values(input=1, expected=b'\x01\x00'),
            UTF8Encoder: Values(input='Hello!', expected=b'\x06\x00Hello!')
        }

        for encoder, values in expected.items():
            field = BasicField(value=values.input, encoder=encoder)
            self.assertEqual(values.expected, field.encode())

    def test_field_decode(self):
        expected = {
            CharBinaryEncoder: Values(input=b'\x01', expected=1),
            ShortBinaryEncoder: Values(input=b'\x01\x00', expected=1),
            UTF8Encoder: Values(input=b'\x06\x00Hello!', expected='Hello!')
        }

        for encoder, values in expected.items():
            field = BasicField(encoder=encoder)
            self.assertEqual(values.expected, field.decode(values.input))

    def calc_length_header(self):
        ...
