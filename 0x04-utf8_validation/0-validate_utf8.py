#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Helper function to check if a byte is a valid start byte
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    # Helper function to count the number of leading ones in a byte
    def count_leading_ones(byte):
        count = 0
        while (byte & 0b10000000) == 0b10000000:
            count += 1
            byte <<= 1
        return count

    # Main validation logic
    i = 0
    while i < len(data):
        current_byte = data[i]

        # Count the number of leading ones in the current byte
        num_leading_ones = count_leading_ones(current_byte)

        # Check if it's a valid start byte
        if num_leading_ones == 0:
            num_following_bytes = 0
        elif num_leading_ones == 1 or num_leading_ones > 4:
            return False
        else:
            num_following_bytes = num_leading_ones - 1

        # Check if there are enough bytes left in the data
        if i + num_following_bytes >= len(data):
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_following_bytes + 1):
            if (data[i + j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += num_following_bytes + 1

    return True
