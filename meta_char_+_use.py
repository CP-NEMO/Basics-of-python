import re
s="Hello World This is Aabhas!"
p=re.findall("is+",s)
print(p)
for i in range(0,len(p)):
	print("hey",end=' ')