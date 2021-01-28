#!/usr/bin/env python3
"""Example code for serialwrapper library"""

import numpy as np
from serialwrapper import SerialWrapper

def main():
    """Demonstrates correct usage of serialwrapper library"""
    SerialWrapper.begin('/dev/ttyS0', 115200)

    message = [0, 1, 2, 3, 4, 0x1f, 0x1e, 5, 6, 8]
    packet = np.zeros(256, dtype=np.uint8)

    while True:
        SerialWrapper.send(message)

        receive, item_num = SerialWrapper.receive(packet)
        if isinstance(receive, np.ndarray):
            print(receive[:item_num])

if __name__ == '__main__':
    main()
