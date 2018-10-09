def decimal_ascii(decimal):
    from base import decimal_ascii
    return decimal_ascii.decimal_to_ascii(decimal)
def decimal_hex(decimal):
    from base import decimal_hex
    return decimal_hex.decimal_to_hex(decimal)
def decimal_binary(decimal):
    from base import decimal_binary
    return decimal_binary.decimal_to_binary(decimal)
def hex_ascii(hex):
    from base import hex_ascii
    return hex_ascii.hex_to_ascii(hex)
def hex_decimal(hex):
    from base import hex_decimal
    return hex_decimal.hex_to_decimal(hex)
def hex_binary(hex):
    from base import hex_binary
    return hex_binary.hex_to_binary(hex)
def binary_ascii(binary):
    from base import binary_ascii
    return binary_ascii.binary_to_ascii(binary)
def binary_hex(binary):
    from base import binary_hex
    return binary_hex.binary_to_hex(binary)
def binary_decimal(binary):
    from base import binary_decimal
    return binary_decimal.binary_to_decimal(binary)
def ascii_decimal(ascii):
    from base import ascii_decimal
    return ascii_decimal.ascii_to_decimal(ascii)
def ascii_hex(ascii):
    from base import ascii_hex
    return ascii_hex.ascii_to_hex(ascii)
def ascii_binary(ascii):
    from base import ascii_binary
    return ascii_binary.ascii_to_binary(ascii)
def base64_decode(text):
    from base import base64_decode
    return base64_decode.base64_decode(text)
def base64_encode(text):
    from base import base64_encode
    return base64_encode.base64_encode(text)
def base32_decode(text):
    from base import base32_decode
    return base32_decode.base32_decode(text)
def base32_encode(text):
    from base import base32_encode
    return base32_encode.base32_encode(text)
def caesar_cipher(text):
    from base import caesar_cipher
    for rot in range(26):
        return caesar_cipher.caesar_cipher(text)
def rev(text):
    from base import rev
    return rev.rev(text)
def chinese(p,q,dp,dq,c):
    from rsa import chinese
    return chinese.chinese_attack(p,q,dp,dq,c)
def cube_root(x):
    from rsa import cube_root
    return cube_root.cuberoot(x)
def common(c1, c2, e1, e2, n):
    from rsa import common
    return common.common_attack(c1, c2, e1, e2, n)
def factor(n):
    from rsa.factor import Factor
    f = Factor(n)
    f.connect()
    return f.get_factor_list()
def wiener(n,e):
    from rsa import wiener
    return wiener.wiener_attack(n,e)
def d(e,phi):
    from rsa import d_calculate
    return d_calculate.d(e,phi)
def modinv(a,m):
    from rsa import mod_inverse
    return mod_inverse.modinv(a,m)
def fermat(n,limit):
    from rsa import fermat
    return fermat.fermat(n,limit)
def hasted(n1,n2,n3,c1,c2,c3,e):
    from rsa import hasted
    return hasted.hasted_attack(n1,n2,n3,c1,c2,c3,e)
def hash(hashType,userHash,wordlist):
    from base import hash
    return hash.hash(hashType,userHash,wordlist)
def zipcrack(filename,wordlist):
    from base import zipcrack
    return zipcrack.zipcrack(filename,wordlist)
def aes256_encrypt(raw,key,BLOCK_SIZE):
    from aes import aes256_encrypt
    return aes256_encrypt.aes256(raw,key,BLOCK_SIZE)
def aes256_decrypt(raw,key,BLOCK_SIZE):
    from aes import aes256_decrypt
    return aes256_decrypt.aes256(raw,key,BLOCK_SIZE)
