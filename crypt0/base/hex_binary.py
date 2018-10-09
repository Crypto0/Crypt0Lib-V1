import binascii
def hex_to_binary(hex):
    def ascii_bin(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    try:
        ascii = hex.decode("hex")
        binary = ascii_bin(ascii)
        return binary
    except TypeError:
        return "Sorry! This is not a Hex."
