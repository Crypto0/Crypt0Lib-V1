import re,binascii
def decimal_to_binary(decimal):
    def ascii_bin(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    try:
        s = re.sub('3[2-9]|[4-9][0-9]|1[0-1][0-9]|12[0-6]', r' \g<0>', decimal)
        ascii = ''.join(chr(int(x)) for x in s.split())
    	binary = ascii_bin(ascii)
    	return binary
    except ValueError:
        return "Sorry! This is not a decimal."
