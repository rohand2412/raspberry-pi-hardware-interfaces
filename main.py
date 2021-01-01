import serial
ser = serial.Serial('/dev/ttyS0', 115200)

message = '0'
message = message.encode()

while True:
    ser.write(message)
