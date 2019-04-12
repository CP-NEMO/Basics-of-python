a=int(input("enter the number to find factorial :"))
fact=1
for i in range(0,a):
	fact=fact*a
	a=a-1
print("factorial =", fact)