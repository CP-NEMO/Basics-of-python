import re
p="HEllo World This is Aabhas!"

s=re.search("Aabhas",p)
if s:
	print("found")
else:
	print("not found")