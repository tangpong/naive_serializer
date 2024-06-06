from serializer.encoders import ShortBinaryEncoder


class BasicField:
    __slots__ = ('encoder', 'value')
    length_encoder = ShortBinaryEncoder()

    def __init__(self, encoder, value=None):
        self.encoder = encoder()
        self.value = value

    def encode(self):
        print(self.value)
        encoded = self.encoder.encode(self.value)
        length = self.calc_length_header(encoded)

        return length + encoded

    def decode(self, buffer, offset):

        self.value, offset = self.encoder.decode(buffer, offset)

        return self.value, offset

    def extract_length_header(self, buffer, offset):
        if self.encoder.calc_struct_length() == float('inf'):
            return self.length_encoder.decode(buffer, offset)
        return 0, 0

    def calc_length_header(self, data):
        if self.encoder.calc_struct_length() == float('inf'):
            return self.length_encoder.encode(len(data))

        return b''

    def __repr__(self):
        return f'{self.__class__.__name__}(encoder={self.encoder}, value={self.value})'
