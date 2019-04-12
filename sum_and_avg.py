#sumand average of first n terms
lim=int(input())
i=0
n=0
while(i<lim):
	i=i+1
	n=n+i
print("sum of first ",lim," terms:", n)
avg=n/lim
print("average of first ",lim," terms:", avg)