from pprint import pprint
from serializer.messages import BasicMessage
from proto import example_proto


class Message(BasicMessage):
    proto = example_proto


def main():
    message_to_encode = Message()

    message_to_encode['field_1'].value = 'Hello!'
    message_to_encode['field_2'].value = 'Hello!'
    message_to_encode['field_3'].value = 2
    message_to_encode['field_4'].value = 'Hello!'

    print(message_to_encode.encode())

    data = b'\x1c\x00\x06\x00Hello!\x06\x00Hello!\x02\x00\x02\x00\x06\x00Hello!'
    message_to_decode = Message()
    print(message_to_decode.decode(data))


if __name__ == '__main__':
    main()
