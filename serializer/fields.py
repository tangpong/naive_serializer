import typing

from serializer.encoders import ShortBinaryEncoder, EncoderInterface
from typing import Any


class BasicField:
    __slots__ = ('encoder', 'value')
    length_encoder = ShortBinaryEncoder

    def __init__(self, encoder: type[EncoderInterface], value: Any = None):
        self.encoder = encoder()
        self.value = value

    def encode(self) -> bytes:
        encoded = self.encoder.encode(self.value)
        encoded_length = self._encode_length(encoded)
        return encoded_length + encoded

    def decode(self, data, offset=0) -> typing.Any:
        if not self.encoder.calc_struct_length():
            self.value = self._decode_dynamic_length_field(data, offset)
        else:
            self.value = self.encoder.decode(data, offset)
        return self.value

    def _decode_dynamic_length_field(self, data, offset) -> typing.Any:
        length = self._decode_length(data, offset)
        offset += self.length_encoder.calc_struct_length()
        return self.encoder.decode(data, offset, limit=length)

    def _decode_length(self, data, offset) -> int:
        if not self.encoder.calc_struct_length():
            return self.length_encoder.decode(data, offset)
        return 0

    def _encode_length(self, data) -> bytes:
        if not self.encoder.calc_struct_length():
            return self.length_encoder.encode(len(data))
        return b''

    def __repr__(self):
        return f'{self.__class__.__name__}(encoder={self.encoder}, value={self.value})'
