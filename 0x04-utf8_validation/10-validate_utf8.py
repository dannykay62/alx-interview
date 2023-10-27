#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    num_bytes_to_follow = 0

    for num in data:
        """Check if the number of bytes to follow is 0"""
        if num_bytes_to_follow == 0:
            if num >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                num_bytes_to_follow == 2
            elif num >> 3 == 0b11110:
                num_bytes_to_follow = 3
            elif num >> 7 == 0b0:
                num_bytes_to_follow = 0
            else:
                return False
        else:
            """Check if the current number is a valid continuation byte"""
            if num >> 6 == 0b10:
                num_bytes_to_follow -= 1
            else:
                return False
    """Check if all bytes have been used (num_bytes_to_follow should be 0)"""
    return num_bytes_to_follow == 0
