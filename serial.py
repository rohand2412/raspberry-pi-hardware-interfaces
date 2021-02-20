#!/usr/bin/env python3
"""Example code for serialwrapper library"""

import numpy as np
from raspberry_pi_libraries import SerialWrapper

def main():
    """Demonstrates correct usage of serialwrapper library"""
    SerialWrapper.begin('/dev/ttyS0', 115200)

    message = [0, -1, 2, -3, 4, 20000, 29, 30, 31, 2147483647, -0, 1, -2, 3, -4, -5, -29, -30, -31, -2147483648]
    packet = np.zeros(256, dtype=np.int32)

    while True:
        SerialWrapper.send(message)

        data = SerialWrapper.receive(packet)
        if not isinstance(data, int):
            packet = data[0]
            size = data[1]
            print(packet[:size])

if __name__ == '__main__':
    main()