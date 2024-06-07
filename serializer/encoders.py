from abc import ABC, abstractmethod
import struct


class EncoderInterface(ABC):

    @classmethod
    @abstractmethod
    def encode(cls, *args, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def decode(cls, *args, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def calc_struct_length(cls):
        ...


class CharBinaryEncoder(EncoderInterface):
    __struct_format: str = 'B'

    @classmethod
    def encode(cls, data: int) -> bytes:
        return struct.pack(cls.__struct_format, data)

    @classmethod
    def decode(cls, data: bytes, offset=0) -> int:
        return struct.unpack_from(cls.__struct_format, data, offset=offset)[0]

    @classmethod
    def calc_struct_length(cls) -> int:
        return struct.calcsize(cls.__struct_format)


class ShortBinaryEncoder(EncoderInterface):
    __struct_format: str = 'H'

    @classmethod
    def encode(cls, data: int) -> bytes:
        return struct.pack(cls.__struct_format, data)

    @classmethod
    def decode(cls, data: bytes, offset=0):
        decoded = struct.unpack_from(cls.__struct_format, data, offset=offset)[0]
        return decoded

    @classmethod
    def calc_struct_length(cls) -> int:
        return struct.calcsize(cls.__struct_format)


class UTF8Encoder(EncoderInterface):

    @classmethod
    def encode(cls, data: str) -> bytes:
        return data.encode('utf-8')

    @classmethod
    def decode(cls, data: bytes, offset=0, limit: int | None = None) -> str:
        limit = limit + offset if limit else -1
        return data[offset:limit].decode('utf-8')

    @classmethod
    def calc_struct_length(cls) -> int:
        return 0
