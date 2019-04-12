a=int(input("Enter the number:"))
f=0
i=0
while(a>0):
	e=int(a%2)
	a=a//2
	f=int(e*(10**i)+f)
	i=i+1 
print(f)