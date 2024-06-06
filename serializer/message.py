from serializer.encoders import ShortBinaryEncoder
from serializer.fields import BasicField


class BasicMessage:
    proto = []
    length_encoder = ShortBinaryEncoder()

    def __init__(self, proto=None):
        self.proto = proto if proto else self.proto
        self.elements = {}

        for element in self.proto:
            self._element_init(element)

    def __getitem__(self, item):
        return self.elements[item]

    def encode(self) -> bytes:
        packed = b''.join(element.encode() for element in self.elements.values())
        length = self.calc_message_length(packed)

        return length + packed

    def decode(self, data):
        pass

    def _element_init(self, element):
        name = element['name']
        subfields = element.get('subfields')
        encoder = element.get('encoder')

        if subfields:
            cls = self._init_subfields(subfields)
        else:
            cls = self._init_field(name, encoder)
        self.elements[name] = cls

    def _init_field(self, name, encoder):
        cls = BasicField(encoder)
        setattr(self, name, cls)

        return cls

    def _init_subfields(self, proto):
        cls = self.__class__(proto)

        return cls

    @classmethod
    def calc_message_length(cls, data):
        length = len(data)
        encoded_length = cls.length_encoder.encode(length)

        return encoded_length