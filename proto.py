from serializer.fields import UTF8Field, ShortField

NAME = 'name'
FIELD = 'field'


example_proto = [
    {NAME: 'field_1', FIELD: UTF8Field},
    {NAME: 'field_2', FIELD: UTF8Field},
    {NAME: 'field_3', FIELD: ShortField},
    {NAME: 'field_4', FIELD: UTF8Field},
]
