class HEY:
	 class_var=1
	 def __init__(self,color,name,height):
		 HEY.class_var += 1
		 self.name= name
		 self.color=color
		 self.height=height
		 print("value =", HEY.class_var)
	 def print_all(self):
		 print("My name is ", self.name)
		 print("my fav color is ", self.color)
		 print("My height is ", self.height)

r1=HEY("black","Batman",52)
r2=HEY("Blue","doraemon",22)
def call_print(R):
	R.print_all()
call_print(r1)
call_print(r2)

class Person:
	def __init__(self,n,p,i):
		self.name=n
		self.personality=p
		self.in_sitting=i
	def stand_up(self):
		self.in_sitting= False
	def Sit_down(self):
		self.in_sitting = True
	def __del__(self):
		print("Distrocter is called")

p1=Person("Jude","aggresive",False)
p2=Person("Adam", " Talkative", True)

p1.friended_to = r2
p2.friended_to = r1
print()
p1.friended_to.print_all()
p2.friended_to.print_all()
p1.Sit_down()
