from itertools import combinations_with_replacement 
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

def gf(p,n):
    nbig = p**n
    multiplications = list()
    sums = list()
    numbers = list()
    for i in range(nbig):
        numbers.append(numberToBase(i,p,n))
    for i in numbers:
        ltem = []
        ltem2 = []
        for j in numbers:
            ltem.append(sum(i,j,p))
            ltem2.append(mul(i,j,p))
        print(ltem2)
        sums.append(ltem)
        multiplications.append(ltem2)
    return [multiplications,sums]

gfs = gf(2,4)
print("multiplications")
print(gfs[0])
print("sums")
print(gfs[1])