#!/usr/bin/env python3
"""Displays incoming pwm data from Arduino"""

import numpy as np
from raspberry_pi_libraries import SerialWrapper

def main():
    """Main code"""
    SerialWrapper.begin('/dev/ttyS0', 115200)

    packet = np.zeros(256, dtype=np.int32)

    while True:
        packet, size = SerialWrapper.receive(packet)
        if size > 0:
            print(packet[0], " ", packet[1]/100)

if __name__ == '__main__':
    main()
