from abc import ABC, abstractmethod
from serializer.encoders import EncoderInterface, ShortBinaryEncoder, UTF8Encoder


class AbstractField(ABC):

    @property
    @abstractmethod
    def length_encoder(self) -> EncoderInterface:
        ...

    @property
    @abstractmethod
    def content_encoder(self) -> EncoderInterface:
        ...

    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value})'

    def decode(self, data, offset=0) -> tuple[any, int]:
        length, offset = self.decode_length(data, offset)
        dec_data, offset = self.content_encoder.decode(data, offset, limit=length)
        self.value = dec_data
        return dec_data, offset

    def decode_length(self, data, offset=0) -> tuple[any, int]:
        return self.length_encoder.decode(data, offset)

    def decode_content(self, data, offset=0) -> tuple[any, int]:
        return self.content_encoder.decode(data, offset)

    def encode(self) -> bytes:
        data = self.value
        enc_data = self.encode_content(data)
        length = self.encode_length(enc_data)

        return length + enc_data

    def encode_length(self, data) -> bytes:
        length = len(data)
        return self.length_encoder.encode(length)

    def encode_content(self, data) -> bytes:
        return self.content_encoder.encode(data)


class UTF8Field(AbstractField):
    length_encoder = ShortBinaryEncoder
    content_encoder = UTF8Encoder


class ShortField(AbstractField):
    length_encoder = ShortBinaryEncoder
    content_encoder = ShortBinaryEncoder
