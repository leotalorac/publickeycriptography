from aes import AES 
import binascii
k1 = ['C09AEC75','90471F73','D71D3609','4C4CDBE3']
k2 = ['EB23FD5C','7B64E22F','AC79D426','E0350FC5']
v = bytes.fromhex('5D662BF1CC92E0679C568182F5FD11C4')
c =bytes.fromhex('D36524DA10554ECA597B98341234D1CC6B009BFDEBE0046CA8433A27A5F0B1D5')

key = bytes.fromhex('10CF6B6150DDF306475A297A9B51EDEA')
aes = AES(key).decrypt_cbc(c,v)
print(aes)

