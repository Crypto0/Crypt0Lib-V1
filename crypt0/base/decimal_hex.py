import re
def decimal_to_hex(decimal):
    try:
        s = re.sub('3[2-9]|[4-9][0-9]|1[0-1][0-9]|12[0-6]', r' \g<0>', decimal)
        ascii = ''.join(chr(int(x)) for x in s.split())
        hex = ascii.encode("hex")
        return hex
    except ValueError:
        return "Sorry! This is not a Decimal."
