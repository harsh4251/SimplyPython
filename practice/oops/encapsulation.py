class Encapsulation():
	def __init__(self, a, b, c):
		self.public = a
		self._protected = b
		self.__private = c
		print("Private can only be accessed inside a class {}".format(self.__private))

e = Encapsulation(1,2,3)
print("Public & protacted can be access outside class{},{} ".format(e.public,e._protected))

"""Name
Notation
Behaviour
name	Public
Can be accessed from inside and outside
_name	Protected
Like a public member, but they shouldn't be directly accessed from outside.
__name	Private
Can't be seen and accessed from outside"""
