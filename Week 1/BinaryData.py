# The below is ASCII chars 'A', 'B', 'C'
binary_data = bytes([0b01000001, 0b01000010, 0b01000011])

binary_string = "01010100 01001001 01001110 01011000"
binary_bytes = bytearray([int(byte, 2) for byte in binary_string.split()])



