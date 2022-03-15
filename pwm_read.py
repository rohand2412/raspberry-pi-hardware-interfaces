# Copyright (C) 2022  Rohan Dugad
#
# Contact info:
# https://docs.google.com/document/d/17IhBs4cz7FXphE0praCaWMjz016a7BFU5IQbm1CNnUc/edit?usp=sharing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
