#!/usr/bin/python3
"""
A method that determines if a given data set 
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Helper function to check if a byte is a valid start byte
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    # Helper function to count the number of trailing ones in a byte
    def count_trailing_ones(byte):
        count = 0
        while (byte & 0b10000000) == 0b10000000:
            count += 1
            byte <<= 1
        return count

    # Main validation logic
    i = 0
    while i < len(data):
        current_byte = data[i]

        # Check if it's a start byte
        if is_start_byte(current_byte):
            # Determine the number of bytes to follow based on the leading ones
            num_following_bytes = count_trailing_ones(current_byte)

            # Check if the number of following bytes is valid
            if num_following_bytes > 3 or num_following_bytes == 1:
                return False

            # Check if there are enough bytes left in the data
            if i + num_following_bytes >= len(data):
                return False

            # Check if the following bytes are valid continuation bytes
            for j in range(1, num_following_bytes + 1):
                if (data[i + j] & 0b11000000) != 0b10000000:
                    return False

            # Move to the next character
            i += num_following_bytes + 1
        else:
            return False

    return True
