a=int(input())
sum1=0
while(a>0):
	number=a%10
	sum1=sum1+number
	a=a//10
print(sum1)