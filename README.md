# NAIVE SERIALIZER

> Naive serializer implementation.\
Just a pet-practice project.\
Protobuf and alternatives should be used instead.


>Наивная реализация сериализатора данных.\
Просто учебный проект для практики.\
Для живых проектов есть protobuf.

#### Data encoders can be found in serializer.fields

| encoder               | description                     |
|-----------------------|---------------------------------|
| _CharBinaryEncoder_   | **int** to **char**  of 1 byte  |
| _ShortBinaryEncoder_  | **int** to **short** of 2 bytes |
| _UTF8Encoder_         | **str** to **encoded UTF8**     |

### Message prototype example can be found in _proto.py_
### Message instance workflow can be found in _example.py_

