symbols = ['0','1','2','3','4','5','6','7','8','9']
for i in range(26):
    symbols.append(chr(65+i))
# sum polynomials
def sum(a,b,n):
    ac = a[::-1]
    bc = b[::-1]
    c = list()
    l = max(len(a),len(b))
    for i in range(l):
        try:
            c.append((ac[i]+bc[i])%n)
        except:
            c.append(0)
    c = c[::-1]
    return c
def polyToNum(poly,b):
    sp = 0
    poly = poly[::-1]
    
    for i in range(len(poly)):
        sp = sp + (b**i)*(int(poly[i]))
    return symbols[int(sp)]
# shit of bits 
def move(l,i,m):
    lt = l.copy()
    for j in range(i):
        lt.append(0)
    lt= [element * m for element in lt]
    return lt
#multiplications polynomials on base n
def mul(a,b,n): 
    bt = min(a,b)[::-1]
    at = max(a,b)
    ls = []
    size = 0
    for i in range(len(bt)):
        l =move(at,i,bt[i])
        size = max(size,len(l))
        ls.append(l)
    ac = list([0]*size)
    for i in range(len(ls)):
        ac = sum(ac,ls[i],n)
    return ac
# Generate the polynomials
def numberToBase(n, b,m):
    if n == 0:
        return [0]+ [0]*(m-1)
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    digits = digits + [0]*(m-len(digits))
    return digits[::-1]
# taken from https://rosettacode.org/wiki/Polynomial_synthetic_division#Python
def extended_synthetic_division(dividend, divisor):
    '''Fast polynomial division by using Extended Synthetic Division. Also works with non-monic polynomials.'''
    # dividend and divisor are both polynomials, which are here simply lists of coefficients. Eg: x^2 + 3x + 5 will be represented as [1, 3, 5]
 
    out = list(dividend) # Copy the dividend
    normalizer = divisor[0]
    for i in range(len(dividend)-(len(divisor)-1)):
        out[i] /= normalizer # for general polynomial division (when polynomials are non-monic),
                                 # we need to normalize by dividing the coefficient with the divisor's first coefficient
        coef = out[i]
        if coef != 0: # useless to multiply if coef is 0
            for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisor,
                                              # because it's only used to normalize the dividend coefficients
                out[i + j] += -divisor[j] * coef
 
    # The resulting out contains both the quotient and the remainder, the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it's what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = -(len(divisor)-1)
    return out[:separator], out[separator:] # return quotient, remainder.

# generate the fields
def gf(p,n,pol):
    pol = pol
    zero = [0]*n
    nbig = p**n
    multiplications = list()
    sums = list()
    numbers = list()
    for i in range(nbig):
        numbers.append(numberToBase(i,p,n))
    ii =0
    for i in numbers:
        ltem = []
        ltem2 = []
        for j in numbers:
            ltem.append(polyToNum(sum(i,j,p),p))
            m = mul(i,j,p)
            mt = extended_synthetic_division(m,pol)[1]
            mt = sum(mt,zero,p)
            # ltem2.append(mt)
            ltem2.append(polyToNum(mt,p))
        if(ii==9):
            print(ltem2)
        ii=ii+1
        sums.append(ltem)
        multiplications.append(ltem2)
    numbersc = list()
    for i in numbers:
        numbersc.append(polyToNum(i,p))
    return [multiplications,sums,numbersc]

# graphics tables
def graphgf(gf):
    print("multiplications")
    print("n "+str(gf[2]))
    index = 0
    for i in gf[0]:
        print(gf[2][index],end=" ")
        print(i)
        index+=1
    index=0
    print("sum")
    print("n "+str(gf[2]))
    for i in gf[1]:
        print(gf[2][index],end=" ")
        print(i)
        index+=1

gfs = gf(3,3,[1,0,2,1])
graphgf(gfs)