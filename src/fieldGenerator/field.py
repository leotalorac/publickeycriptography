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
def move(l,i,m):
    lt = l.copy()
    for j in range(i):
        lt.append(0)
    lt= [element * m for element in lt]
    return lt
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
a = [1,1,1]    
b =[1,1]
print(mul(b,a,3))
