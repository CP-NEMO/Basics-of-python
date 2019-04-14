class Call_me:
	def __init__(self,Pn,CN,rsn):
		self.Phone_number=Pn
		self.Caller_name=CN
		self.calling_reason=rsn
	def Machine(self):
		print("Hey Please Leave a message")
	def Pick_up(self):
		print("hey Man say what")

class why_call(Call_me):
	def __init__(self,rsnn):
		self.Not_call_rsn=rsnn
	def reason_denied(self):
		Call_me.Machine(self)
		print("HA HA nice Joke")

A=why_call("I am busy")
A.reason_denied()