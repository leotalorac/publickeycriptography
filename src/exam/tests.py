from aes import AES 
import binascii
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
    m=4
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









k =bytes.fromhex('CFBF50935CE44C197D1459E8483A38FA')
k = bytearray.fromhex('C6CAB7B7B9D584450D0609112FD5F39A')
vi = bytes.fromhex('69F67F1AE5349D250000000000000000')
vi = bytes.fromhex('AF92750E273C5EE60000000000000000')
s = ''
aes = AES(k)
for i in range(64):
    v = bytes.fromhex(hex(int(binascii.hexlify(vi),16) | i)[2:])
    st =str(binascii.hexlify(aes.encrypt_block(v)))
    s += st[2:len(st)-1]
print(poker(s))

