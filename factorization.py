import math as m

a = int(input("Please enter the number you want to factorize.\n>>> "))
b = []
c = m.sqrt(a)
c = int(c)+1

for i in range(2,c,1):
	while 1:
		if a % i == 0:
			b.append(i)
			a = a // i
			continue
		else:
			break

if a != 1:
	b.append(a)

print(b)
