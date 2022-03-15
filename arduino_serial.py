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
"""Example code for serialwrapper library"""

import numpy as np
from raspberry_pi_libraries import SerialWrapper

def main():
    """Demonstrates correct usage of serialwrapper library"""
    SerialWrapper.begin('/dev/serial0', 115200)

    message = [-1, 0, 2, -3, 4, 20000, 29, 30, 31, 2147483647, -0, 1, -2, 3, -4, -5, -29, -30, -31, -2147483648]
    packet = np.zeros(256, dtype=np.int32)

    while True:
        SerialWrapper.send(message)

        packet, size = SerialWrapper.receive(packet)
        if size > 0:
            print(packet[:size])

if __name__ == '__main__':
    main()
