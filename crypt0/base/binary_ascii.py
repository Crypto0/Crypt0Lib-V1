import binascii
def binary_to_ascii(binary):
    def bin_ascii(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return int2bytes(n).decode(encoding, errors)
    def int2bytes(i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    try:
        ascii = bin_ascii(binary)
        return ascii
    except ValueError:
	return "Sorry! This is not a Binary."
