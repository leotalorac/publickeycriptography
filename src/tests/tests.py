import math
def frecuencia(n):
    b = bin(int(n,16))[2:]
    ones = b.count('1')
    zeros = b.count('0')
    n = len(b)
    return (((zeros-ones)**2)/n)
def serial(n):
    bn = bin(int(n,16))[2:]
    n = len(bn)
    zz = 0
    oz= 0
    oo= 0
    zo= 0
    ones = bn.count('1')
    zeros = bn.count('0')
    for i in range(len(bn)-1):
        if(bn[i:i+2] == '00'):
            zz+=1
        if(bn[i:i+2] == '01'):
            zo+=1
        if(bn[i:i+2] == '10'):
            oz+=1
        if(bn[i:i+2] == '11'):
            oo+=1
    tr = (4/(n-1))*((zz**2)+(zo**2)+(oz**2)+(oo**2))
    tr = tr - (2/n)*(ones**2 + zeros**2)+1
    return tr
def findf(s,sf):
    c =0
    for i in range(0,len(s)-len(sf),len(sf)):
        if(s[i:i+len(sf)] == sf):
            c+=1
    return c
def poker(n):
    bn = bin(int(n,16))[2:]
    n = len(bn)
    # get m
    m =1
    while (int(n/m) >= 5*(2**m)):
        m+=1
    m-=1
    k = int(n/m)
    # generate strings
    s = []
    for i in range(2**m):
        st = bin(i)[2:]
        s.append(str('0'*(m-len(st))+st))
    f =[]
    # get frecuency
    for i in s:
        f.append(findf(bn,i))
    sf = 0
    for i in f:
        sf += i**2
    pt = (((2**m)/k)*(sf))-k
    return pt

num = 'e3114ef249e3114ef249e3114ef249e3114ef249'
print(poker(num))