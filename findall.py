import re
s="Hello world This is Aabhas!"
p=re.findall("This",s)
if p:
	print("found it!")
else:
	print("not foud")