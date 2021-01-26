import serial
ser = serial.Serial('/dev/ttyS0', 115200)

message = '1'
message = message.encode()

while True:
    ser.write(message)

    receive = ser.read().decode()
    print(receive)
