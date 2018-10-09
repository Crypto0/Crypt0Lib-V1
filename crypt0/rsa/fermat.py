def fermat(n,limit):
    def isqrt( n):
        if n == 0:
            return 0
        a, b = divmod(n.bit_length(), 2)
        x = 2**(a+b)
        while True:
            y = (x + n//x)//2
            if y >= x:
                return x
            x = y
    a = isqrt(n)
    max = a + limit
    while a < max:
        b2 = a*a - n
        if b2 >= 0:
            b = isqrt(b2)
            if b*b == b2:
                break
        a += 1
    if a < max:
        return {'p':a+b , 'q':a-b}
    else:
        return "Sorry Fermat cant factorize n."
