import unittest
from typing import Any
from dataclasses import dataclass
from serializer.fields import UTF8Field, ShortField


@dataclass
class Values:
    input: Any
    expected: Any


class TestBasicField(unittest.TestCase):
    def test_field_encode(self):
        expected = {
            ShortField: Values(input=1, expected=b'\x02\x00\x01\x00'),
            UTF8Field: Values(input='Hello!', expected=b'\x06\x00Hello!')
        }

        for field, values in expected.items():
            f = field(value=values.input)
            self.assertEqual(values.expected, f.encode())

    def test_field_decode(self):
        expected = {
            ShortField: Values(input=b'\x02\x00\x0A\x00', expected=(10, 4)),
            UTF8Field: Values(input=b'\x06\x00Hello!', expected=('Hello!', 8))
        }

        for field, values in expected.items():
            f = field()
            self.assertEqual(values.expected, f.decode(values.input))
