from collections import OrderedDict

from serializer.encoders import ShortBinaryEncoder


class BasicMessage:
    proto = []
    length_encoder = ShortBinaryEncoder

    def __init__(self, proto=None):
        self.proto = proto if proto else self.proto
        self.elements = OrderedDict()
        for element in self.proto:
            self._element_init(element)

    def __getitem__(self, item):
        return self.elements[item]

    def _element_init(self, element):
        name = element['name']
        field = element['field']
        cls = field()
        setattr(self, name, cls)
        self.elements[name] = cls

    def encode(self) -> bytes:
        enc_elements = self.encode_elements()
        enc_length = self.encode_length(enc_elements)
        return enc_length + enc_elements

    def encode_elements(self):
        return b''.join(element.encode() for element in self.elements.values())

    def encode_length(self, data) -> bytes:
        length = len(data)
        return self.length_encoder.encode(length)

    def decode(self, data, offset=0) -> tuple[any, int]:
        length, offset = self.decode_length(data, offset)

        for field in self.elements.values():
            dec_data, offset = field.decode(data, offset)
        return self.elements, offset

    def decode_length(self, data, offset=0) -> tuple[any, int]:
        return self.length_encoder.decode(data, offset)

    def decode_element(self, field, data, offset=0) -> tuple[any, int]:
        data, offset = field.decode(data, offset)
        return data, offset
