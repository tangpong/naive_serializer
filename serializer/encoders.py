from abc import ABC, abstractmethod
import struct


class EncoderInterface(ABC):
    @abstractmethod
    def encode(self, data):
        ...

    @abstractmethod
    def decode(self, data):
        ...

    @abstractmethod
    def calc_struct_length(self):
        ...


class CharBinaryEncoder(EncoderInterface):
    struct_format: str = 'B'

    def encode(self, data: int) -> bytes:
        return struct.pack(self.struct_format, data)

    def decode(self, buffer: bytes, offset=0) -> int:
        return struct.unpack_from(self.struct_format, buffer, offset=offset)[0]

    def calc_struct_length(self):
        return struct.calcsize(self.struct_format)


class ShortBinaryEncoder(EncoderInterface):
    struct_format: str = 'H'

    def encode(self, data: int) -> bytes:
        return struct.pack(self.struct_format, data)

    def decode(self, buffer: bytes, offset=0):
        decoded = struct.unpack_from(self.struct_format, buffer, offset=offset)[0]
        offset += self.calc_struct_length()
        return decoded, offset

    def calc_struct_length(self):
        return struct.calcsize(self.struct_format)


class UTF8Encoder(EncoderInterface):

    def encode(self, data: str) -> bytes:
        return data.encode('utf-8')

    def decode(self, data: bytes, offset=0) -> str:
        return data[offset:].decode('utf-8')

    def calc_struct_length(self):
        return float('inf')
