def addition(a,b):
	c=a+b
	print(c)
addition(1,2)
#inserting value in list
def new_var(d):
	d.append(int(input()))
	return d
d=[1,2,3,4,10,55,66,184]
print(d)
new_var(d)
print(d)
#swaping values in list
def swap(d):
	temp= d[0]
	d[0]=d[len(d)-1]
	d[len(d)-1]=temp
swap(d)
print(d)
#pop the last variable of list
def popping(d):
	d.pop()
popping(d)
#sort list
def sort(d):
	d.sort()
sort(d)
print(d)
#delete element in list
def delete(d):
	del d[3]
delete(d)
print(d)
#inverse list
def inverse(d):
	d.reverse()
inverse(d)
print(d)