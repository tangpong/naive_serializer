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


class ShortBinaryEncoder(EncoderInterface):
    __struct_format: str = 'H'

    @classmethod
    def encode(cls, data: int) -> bytes:
        return struct.pack(cls.__struct_format, data)

    @classmethod
    def decode(cls, data: bytes, offset=0, *args, **kwargs):
        decoded = struct.unpack_from(cls.__struct_format, data, offset=offset)[0]
        offset += cls.calc_struct_length()
        return decoded, offset

    @classmethod
    def calc_struct_length(cls) -> int:
        return struct.calcsize(cls.__struct_format)


class UTF8Encoder(EncoderInterface):

    @classmethod
    def encode(cls, data: str) -> bytes:
        return data.encode('utf-8')

    @classmethod
    def decode(cls, data: bytes, offset=0, limit: int = None):
        limit = limit + offset if limit else None
        dec = data[offset:limit].decode('utf-8')
        offset = len(data[offset:limit]) if not limit else limit
        return dec, offset

    @classmethod
    def calc_struct_length(cls) -> int:
        return 0
