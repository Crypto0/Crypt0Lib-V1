def hex_to_ascii(hex):
    try:
        ascii = hex.decode("hex")
        return ascii
    except TypeError:
        return "Sorry! This is not a Hex."
