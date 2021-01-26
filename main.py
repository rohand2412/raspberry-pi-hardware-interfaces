from serialwrapper import SerialWrapper

SerialWrapper.begin('/dev/ttyS0', 115200)

message = 'a'

while True:
    SerialWrapper.send([message])

    receive = SerialWrapper.receive()
    print(receive)
