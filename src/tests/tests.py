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

def poker(num):
    bn = bin(int(num,16))[2:]
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

def findf2(s,sf,cg):
    c =0
    index = 0
    t=0
    st =True
    while(index<len(s)):
        if(s[index] == cg):
            t+=1
        else:
            st=True
            t=0
        if(t == len(sf)):
            if(index!=len(s)-1):
                if(s[index+1] !=cg and st):
                    c+=1
                else:
                    st=False
            else:
                c+=1
        index+=1    
    return c

def runs(num):
    bn = bin(int(num,16))[2:]
    n = len(bn)
    # get k
    e=6
    es = []
    i=0
    while e>5:
        e = (n-i+3)/(2**(i+2))
        es.append(e)
        i+=1
    es.pop(0)
    k=int(i-1)
    z =[]
    o =[]
    for i in range(1,k+1):
        zs = '0'*i
        os = '1'*i
        z.append(findf2(bn,zs,'1'))
        o.append(findf2(bn,os,'0'))
    s1 =0
    s2 =0
    print(es)
    for i in range(k):
        s1 += (((o[i]-es[i])**2)/es[i])
        s2 += (((z[i]-es[i])**2)/es[i])
    s = s1+s2
    return s
num = 'e3114ef249e3114ef249e3114ef249e3114ef249'
print(runs(num))