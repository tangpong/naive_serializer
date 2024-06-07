from serializer.messages import BasicMessage
from protos import example_proto


class ExampleMessage(BasicMessage):
    proto = example_proto


def main():

    message = ExampleMessage()
    message['message_type'].value = 0
    message['field_1'].value = 1
    message['field_2'].value = 1
    message['field_3'].value = 'Hello!'

    message['field_4']['subfield_1'].value = 1
    message['field_4']['subfield_2'].value = 1
    message['field_4']['subfield_3'].value = 'Hello2!'
    print(message.encode())


    message_to_decode = ExampleMessage()
    message_to_decode.decode(b'\x1a\x00\x00\x01\x01\x00\x06\x00Hello!\x0c\x00\x01\x01\x00\x07\x00Hello2!')


if __name__ == '__main__':
    main()
