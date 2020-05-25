import math
class Tests:
    def __init__(self):
        pass
    def frequency(self,s):
        bs = bin(s)[2:];     
        print(bs)
        n = len(bs)
        zeros = bs.count('0')
        ones = bs.count('1')   
        s = abs(ones-zeros)
        x = ((zeros-ones)**2) / n
        print("x:" + str(x))
        p = math.erfc(float (s)/(math.sqrt (float(n)) * math.sqrt(2.0)))
        print("p: " + str(p))
        return p
