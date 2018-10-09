def ascii_to_decimal(ascii):
    decimal = ''.join(str(ord(char)) for char in ascii)
    return decimal
