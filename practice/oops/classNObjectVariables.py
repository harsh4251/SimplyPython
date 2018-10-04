class Account(object):
	counter = 0
	def __init__(self, holder, number, balance,credit_line=1500): 
		Account.counter += 1
		self.__Holder = holder 
		self.__Number = number 
		self.__Balance = balance
		self.__CreditLine = credit_line
	def __del__(self):
		Account.counter -= 1

a = Account("Homer Simpson", 2893002, 2325.21)
print(a.counter)

b = Account("Fred Flintstone", 2894117, 755.32)
print(b.counter)


del a
print(Account.counter)


del b
print(Account.counter)
