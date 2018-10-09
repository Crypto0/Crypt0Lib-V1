def hasted_attack(n1,n2,n3,c1,c2,c3,e):
    def mulinv(a,b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a / b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    def powinv(x,n):
        high = 1
        while high ** n < x:
            high *= 2
        low = high/2
        while low < high:
            mid = (low + high) // 2
            if low < mid and mid**n < x:
                low = mid
            elif high > mid and mid**n > x:
                high = mid
            else:
                return mid
        return mid + 1
    n = [n1,n2,n3]
    a = [c1,c2,c3]
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mulinv(p, n_i) * p
    return powinv(sum % p,e)
