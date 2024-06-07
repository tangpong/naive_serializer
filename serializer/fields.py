from serializer.encoders import ShortBinaryEncoder


class BasicField:
    __slots__ = ('encoder', 'value')
    length_encoder = ShortBinaryEncoder

    def __init__(self, encoder, value=None):
        self.encoder = encoder()
        self.value = value

    def encode(self):
        encoded = self.encoder.encode(self.value)
        encoded_length = self._encode_length(encoded)
        return encoded_length + encoded

    def decode(self, data, offset=0):
        if not self.encoder.calc_struct_length():
            self.value = self.encoder.decode(data, offset)
        return self.value

    def _decode_length(self, data, offset):
        if not self.encoder.calc_struct_length():
            return self.length_encoder.decode(data, offset)
        return 0

    def _encode_length(self, data):
        if not self.encoder.calc_struct_length():
            return self.length_encoder.encode(len(data))
        return b''

    def __repr__(self):
        return f'{self.__class__.__name__}(encoder={self.encoder}, value={self.value})'
