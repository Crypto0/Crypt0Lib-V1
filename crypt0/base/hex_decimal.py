def hex_to_decimal(hex):
    try:
        ascii = hex.decode("hex")
        decimal = ''.join(str(ord(char)) for char in ascii)
        return decimal
    except TypeError:
        return "Sorry! This is not a Hex."
