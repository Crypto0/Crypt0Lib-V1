import base64
def base32_decode(data):
    try:
	encode = base64.b32decode(data)
    	return encode
    except TypeError:
        return "Sorry! This is not Base32"
