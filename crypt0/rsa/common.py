def common_attack(c1, c2, e1, e2, n):
    def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    gcd,s1,s2 = egcd(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = modinv(chipher_text_1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = modinv(chipher_text_2, n)
    return (pow(c1, s1, n) * pow(c2, s2, n))
