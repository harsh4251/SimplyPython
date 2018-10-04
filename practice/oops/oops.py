class a():
	def greetings(self,greeting):
		print(greeting)
	def __init__(self): #constructor
		print('this is constructor')
	def __del__(self): #destructor will be called when instance/object is deleted
		print("Destructor started")

b = a()
b.greetings('Good morning')

del b
