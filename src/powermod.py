def power(a,b,n):
	curr = a%n
	res = 1
	while b>0:
		if(b%2 == 1):
			res = res*curr %n
		curr = curr*curr % n
		b = int(b/2)
	return res
a = int(input())
b = int(input())
n = int(input())
print(power(a,b,n))