n=int(input("enter any binary number : "))
nc=n
i=0
s=0
while(nc>0):
	i=i+1
	nc=int(nc/10)
for x in range(0,i):
	s=s+((n%10)*(2**x))
	n=int(n/10)
print(s)