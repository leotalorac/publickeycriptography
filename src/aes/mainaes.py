from aes import AES
import binascii
# k     = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# k = '2b7e151628aed2a6abf7158809cf4f3c'
# key =bytearray.fromhex(k)
# aes = AES(key)
# m = aes._key_matrices
# index = 4
# for i in range(1,11):
#     for j in m[i]:
#         print(str(index) + " " + str(binascii.hexlify(bytearray(j))))
#         index+=1
# examplo od aes
# FUNTION TO PASS THE MESSAGE TO BYTES AND PUT ON THE AES
def stringToBytes(s):
    b =''
    for i in range(len(s)):
        b += hex(ord(s[i]))[2:]
    if(len(b)%16 == 0):
        return b
    else:
        b = b + '0'*((((len(b)//16)*16)+16)-len(b))
        return b
def encrypt_ecb(message,k):
    aes = AES(k)
    c = ''
    blocks = [message[i:i+16] for i in range(0, len(message), 16)]
    for i in blocks:
        m = bytes(i, 'raw_unicode_escape')
        ci = aes.encrypt_block(m)
        hexc = str(binascii.hexlify(ci))
        print(hexc)
        c += hexc[2:len(hexc)-1]
    return c
m ="AES es un algoritmo muy importante en la seguridad de la informacion actual"
k = bytes.fromhex('0123456789abcdef0123456789abcdef')
mb =stringToBytes(m)
print(encrypt_ecb(mb,k))

# USE THIS
#  m = bytes(i, 'raw_unicode_escape')


# -------------------- EXAMPLE -----------------
def example():
    k = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
    m =bytes.fromhex('414553206573206d757920666163696c')
    aes = AES(k)
    ma = aes._key_matrices
    index = 4
    # print the keys
    for i in range(1,11):
        for j in ma[i]:
            print(str(index) + " " + str(binascii.hexlify(bytearray(j))))
            index+=1
    # answer
    c = aes.encrypt_block(m)
    print(binascii.hexlify(c))
    print(stringToBytes("AES es muy facil"))


