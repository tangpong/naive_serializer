### NAIVE SERIALIZER

> Primitive serializer implementation.\
Just pet project for a practice sake.\
Protobuf and alternatives should be used instead.


#### Data encoders can be found in _serializer.encoders_

| encoder               | description                     |
|-----------------------|---------------------------------|
| _ShortBinaryEncoder_  | **int** to **short** of 2 bytes |
| _UTF8Encoder_         | **str** to **encoded UTF8**     |

#### Field encoders can be found in _serializer.fields_

| filed        | value encoder      | length encoder      |
|--------------|--------------------|---------------------|
| _ShortField_ | ShortBinaryEncoder | ShortBinaryEncoder  |
| _UTF8Field_  | UTF8Encoder        | ShortBinaryEncoder  |


#### Message protocol example can be found in _proto.py_
#### Message instance workflow can be found in _example.py_


>_What should be fixed in future?_

- Proto fields should not be called by string
- Add logger
- Add optional flag to proto fields
- Add subfields
- Create python package
