import unittest
from dataclasses import dataclass
from serializer.fields import UTF8Field, ShortField
from serializer.messages import BasicMessage

NAME = 'name'
FIELD = 'field'


@dataclass
class Values:
    proto: list
    fields: dict
    encoded: bytes


class TestBasicMessage(unittest.TestCase):
    EXAMPLE_PROTO_1 = [
        {NAME: 'field_1', FIELD: UTF8Field},
    ]

    EXAMPLE_PROTO_2 = [
        {NAME: 'field_1', FIELD: ShortField},
        {NAME: 'field_2', FIELD: UTF8Field},
    ]

    EXAMPLE_PROTO_3 = [
        {NAME: 'field_1', FIELD: UTF8Field},
        {NAME: 'field_2', FIELD: ShortField},
        {NAME: 'field_3', FIELD: UTF8Field},
    ]

    DATA = [
        Values(proto=EXAMPLE_PROTO_1,
               encoded=b'\r\x00\x0b\x00HelloWorld!',
               fields={'field_1': 'HelloWorld!'}),
        Values(proto=EXAMPLE_PROTO_2,
               encoded=b'\x11\x00\x02\x00\x0f\x00\x0b\x00HelloWorld!',
               fields={'field_1': 15, 'field_2': 'HelloWorld!'}),
        Values(proto=EXAMPLE_PROTO_3,
               encoded=b'\x1c\x00\x0b\x00HelloWorld!\x02\x00\x0f\x00\t\x00ByeWorld!',
               fields={'field_1': 'HelloWorld!', 'field_2': 15, 'field_3': 'ByeWorld!'})
    ]

    def test_encode(self):
        for values in self.DATA:
            message = BasicMessage(values.proto)
            for name, value in values.fields.items():
                message[name].value = value
            encoded = message.encode()

            self.assertEqual(values.encoded, encoded)

    def test_decode(self):
        for values in self.DATA:
            message = BasicMessage(values.proto)
            decoded = message.decode(values.encoded)
            for field_name, field_instance in decoded[0].items():
                self.assertEqual(values.fields[field_name], field_instance.value)
