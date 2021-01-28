import numpy as np
from serialwrapper import SerialWrapper

SerialWrapper.begin('/dev/ttyS0', 115200)

message = [0, 1, 2, 3, 4, 0x1f, 0x1e, 5, 6, 8]
packet = np.zeros(256, dtype=np.uint8)

while True:
    SerialWrapper.send(message)

    receive, itemNum = SerialWrapper.receive(packet)
    if type(receive) == np.ndarray:
        print(receive[:itemNum])
