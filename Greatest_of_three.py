#which number amoung 3 are greatest
x=int(input())
y=int(input())
z=int(input())

if(x>y and x>z):
	print(x,"is greatest")
elif(y>x and y>z):
	print(y,"is greatest")
else:
	print(z,"is greatest")