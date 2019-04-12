a=int(input("1st side :"))
b=int(input("2nd side :"))
c=int(input("3rd side :"))

s=(a+b+c)/2
print(s)
area=((s*(s-a)*(s-b)*(s-c))**(0.5))
print("area of triangle = ", area)