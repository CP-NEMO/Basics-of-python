import re

s="Hello World This is AABHAS!"
p=re.match("Hello",s)
q=re.match("AABHAS",s)
if q:
	print('q matched')
elif p:
	print('p matched')
else:
	print('not matched')