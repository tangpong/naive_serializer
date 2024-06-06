from serializer.encoders import CharBinaryEncoder, ShortBinaryEncoder, UTF8Encoder

fields = 'fields'
name = 'name'
optional = 'optional'
encoder = 'encoder'
subfields = 'subfields'

example_proto = [
    {name: 'message_type', encoder: CharBinaryEncoder},
    {name: 'field_1', encoder: CharBinaryEncoder},
    {name: 'field_2', encoder: ShortBinaryEncoder},
    {name: 'field_3', encoder: UTF8Encoder},
    {name: 'field_4', subfields: [
        {name: 'subfield_1', encoder: CharBinaryEncoder},
        {name: 'subfield_2', encoder: ShortBinaryEncoder},
        {name: 'subfield_3', encoder: UTF8Encoder}, ]
     }
]


