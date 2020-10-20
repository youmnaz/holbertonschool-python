#!/usr/bin/python3
"""
    0-validate_utf8.py
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    byte_num = 0
    for i, n in enumerate(data):
        byte = n & 0xFF
        if byte_num:
            if byte >> 6 != 2:
                return False
            byte_num -= 1
            continue
        while (1 << abs(7 - byte_num)) & byte:
            byte_num += 1
        if byte_num == 1 or byte_num > 4:
            return False
        byte_num = max(byte_num - 1, 0)
    return byte_num == 0
