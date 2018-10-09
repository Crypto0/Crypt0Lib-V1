def chinese_attack(p,q,dp,dq,c):
    def modinv(a, m):
        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    q_inv = modinv(p , q)
    m1 = pow(c,dp,p)
    m2 = pow(c,dq,q)
    h = (q_inv*(m1-m2)) % p
    return m2 + h * q
