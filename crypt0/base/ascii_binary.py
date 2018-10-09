import binascii
def ascii_to_binary(ascii):
    def ascii_bin(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    binary = ascii_bin(ascii)
    return binary
