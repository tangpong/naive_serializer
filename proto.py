from serializer.fields import UTF8Field, ShortField

name = 'name'
field = 'field'


example_proto = [
    {name: 'field_1', field: UTF8Field},
    {name: 'field_2', field: UTF8Field},
    {name: 'field_3', field: ShortField},
    {name: 'field_4', field: UTF8Field},
]
