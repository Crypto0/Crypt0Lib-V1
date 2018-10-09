import base64
def base64_decode(data):
    try:
	encode = base64.b64decode(data)
    	return encode
    except TypeError:
	return "Sorry! This is not Base64"
