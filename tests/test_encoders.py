import struct
import unittest
from dataclasses import dataclass
from typing import Any

from serializer.encoders import ShortBinaryEncoder, UTF8Encoder


@dataclass
class Values:
    input: Any
    expected: Any


class TestEncoders(unittest.TestCase):
    def test_normal_encode(self):
        expected = {
            ShortBinaryEncoder: Values(input=1, expected=b'\x01\x00'),
            UTF8Encoder: Values(input='Hello!', expected=b'Hello!')
        }

        for encoder, value in expected.items():
            output = encoder.encode(value.input)
            self.assertEqual(value.expected, output)

    def test_overflow_encode_exception(self):
        expected = {
            ShortBinaryEncoder: Values(input=(-1, 65536,), expected="'H' format requires 0 <= number <= 65535")
        }
        for encoder, values in expected.items():
            for inp in values.input:
                with self.assertRaisesRegex(struct.error, values.expected):
                    encoder.encode(inp)

    def test_normal_decode(self):
        expected = {
            ShortBinaryEncoder: Values(input=b'\x01\x00', expected=(1, 2)),
            UTF8Encoder: Values(input=b'Hello!', expected=('Hello!', 6))
        }

        for encoder, value in expected.items():
            output = encoder.decode(value.input)
            self.assertEqual(value.expected, output)

    def test_calc_struct_length(self):
        expected = {
            ShortBinaryEncoder: 2,
            UTF8Encoder: 0
        }

        for encoder, expected in expected.items():
            output = encoder.calc_struct_length()
            self.assertEqual(expected, output)
