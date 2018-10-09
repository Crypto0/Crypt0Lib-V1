# Crypt0Lib V1 :

- Cryptography Lib for CTF.

# Install :

```
$ sudo python setup.py install
```
# Initialization :

```
from crypt0 import lib
```

# Manual :

```
- lib.ascii_decimal("ascii")
- lib.ascii_hex("ascii")
- lib.ascii_binary("ascii")
- lib.decimal_ascii("decimal")
- lib.decimal_hex("decimal")
- lib.decimal_binary("decimal")
- lib.hex_ascii("hex")
- lib.hex_decimal("hex")
- lib.hex_binary("hex")
- lib.binary_ascii("binary")
- lib.binary_decimal("binary")
- lib.binary_hex("binary")
- lib.base64_encode("text")
- lib.base64_decode("b64_text")
- lib.base32_encode("text")
- lib.base32_decode("b32_text")
- lib.caesar_cipher("text")
- lib.rev("text")
- lib.cuberoot(x)
- lib.chinese(p,q,dp,dq,c)
- lib.common(c1, c2, e1, e2, n)
- lib.wiener(n,e)
- lib.hasted(n1,n2,n3,c1,c2,c3,e)
- lib.fermat(n,limit)
- lib.factor(n)
- lib.d(e,phi)
- lib.modinv(a,m)
- lib.hash(hashType,userHash,wordlist)
- lib.zipcrack(filename,wordlist)
- lib.aes256_encrypt(raw,key,BLOCK_SIZE)
- lib.aes256_decrypt(enc,key,BLOCK_SIZE)
```
# RSA Example :

```
fermat :
n=14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
fermat = lib.fermat(n,999999)
q = fermat['q']
p = fermat['p']
# p = 121588253559534573498320028934517990374721243335397811413129137253981502291631
# q = 121588253559534573498320028934517990374721243335397811413129137253981502291629
```

```
factor n :
n = 245841236512478852752909734912575581815967630033049838269083
factor = lib.factor(n)
p = factor[0]
q = factor[1]
# p = 416064700201658306196320137931
# q = 590872612825179551336102196593
```

# Hash Bruteforce Example:

```
hashType = "md5"
userHash = "5f4dcc3b5aa765d61d8327deb882cf99"
wordlist = "/usr/share/wordlists/rockyou.txt"
lib.hash(hashType,userHash,wordlist)
# password                    '\n\n[+] HASH IS CRACKED SUCCESSFUL : [ password ]'
```

# Zip file crack Example:

```
filename = "text.zip"
wordlist = "/usr/share/wordlists/rockyou.txt"
lib.zipcrack(filename,wordlist)
#PASSWORD FOUND!!!!: pw == secret
```

#AES 256 CBC Example:

```
raw = "test"
key = "123"
lib.aes256_encrypt(raw,key,32)
# Encrypted: zb4GNDpsaWVj+AGXhuWWF2vrfhvuEy3iUJiuDZrDWgeMmZR19tmz4vSQg1ob33qF
```

```
enc = "zb4GNDpsaWVj+AGXhuWWF2vrfhvuEy3iUJiuDZrDWgeMmZR19tmz4vSQg1ob33qF"
key = "123"
lib.aes256_decrypt(enc,key,32)
# Decrypted Message: test
```

# TODO:

- i will keep update this Lib
- [Facebook](https://www.facebook.com/crypto8)
