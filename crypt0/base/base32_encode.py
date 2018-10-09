import base64
def base32_encode(data):
    encode = base64.b32encode(data)
    return encode
