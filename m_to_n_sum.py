#sum of numbers from m to n
m=int(input())
n=int(input())
sum=0
for i in range(m,n+1):
	sum=sum+i
print("Sum of number from", m,"to", n,"is", sum)