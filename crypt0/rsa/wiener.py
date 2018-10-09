import math
def wiener_attack(N,E) :
    def DevContinuedFraction(num, denum) :
	    partialQuotients = []
	    divisionRests = []
	    for i in range(int(math.log(denum, 2)/1)) :
		    divisionRests = num % denum
		    partialQuotients.append(num / denum)
		    num = denum
		    denum = divisionRests
		    if denum == 0 :
			    break
	    return partialQuotients
    def DivergentsComputation(partialQuotients) :
	    (p1, p2, q1, q2) = (1, 0, 0, 1)
	    convergentsList = []
	    for q in partialQuotients :
		    pn = q * p1 + p2
		    qn = q * q1 + q2
		    convergentsList.append([pn, qn])
		    p2 = p1
		    q2 = q1
		    p1 = pn
		    q1 = qn
	    return convergentsList
    def SquareAndMultiply(base,exponent,modulus):
	    binaryExponent = []
	    while exponent != 0:
		    binaryExponent.append(exponent%2)
        	    exponent = exponent/2
	    result = 1
	    binaryExponent.reverse()
	    for i in binaryExponent:
		    if i == 0:
			    result = (result*result) % modulus
		    else:
			    result = (result*result*base) % modulus
	    return result
    testStr = 42
    phi = 0
    C = SquareAndMultiply(testStr, E, N)
    for c in DivergentsComputation(DevContinuedFraction(E, N)) :
            if SquareAndMultiply(C, c[1], N) == testStr :
                pq = __helper(N,E,c)
                pq.update({'d': c[1]})
                return  pq
    return {'q':None,'p':None,'d':None}
