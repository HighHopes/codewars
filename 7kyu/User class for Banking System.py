"""A company is opening a bank, but the coder who is designing the user class made some errors. They need you to help them.

You must include the following:

A withdraw method
Subtracts money from balance
One parameter, money to withdraw
Raise ValueError if there isn't enough money to withdraw
Return a string with name and balence(see examples)
A check method
Adds money to baleance
Two parameters, other user and money
Other user will always be valid
Raise a ValueError if other user doesn't have enough money
Raise a ValueError if checking_account isn't true for other user
Return a string with name and balance plus other name and other balance(see examples)
An add_cash method
Adds money to balance
One parameter, money to add
Return a string with name and balance(see examples)
Additional Notes:

Checking_account should be stored as a boolean
No input numbers will be negitive
Output must end with period
Float numbers will not be used so, balance should be integer
No currency will be used"""


class User(object):
	def __init__(self, name, balance, checking_account):
		self.name = name
		self.balance = balance
		self.checking_account = checking_account

	# Happy Coding

	def withdraw(self, cash):
		try:
			if cash > self.balance:
				err = self.name + " can't withdraw " + str(cash) + ", he only has " + str(self.balance) + "."
				raise ValueError()
		except ValueError:
			return ValueError(err)
		else:
			self.balance -= cash
			return self.name + ' has ' + str(self.balance) + '.'

	def add_cash(self, add_cash):
		self.balance += add_cash
		return self.name + ' has ' + str(self.balance) + '.'

	def check(self, other, cash):
		try:
			if not other.checking_account:
				err = other.name + "'s account is not validated."
				raise ValueError()
			elif cash > other.balance:
				err = other.name + " has only " + str(other.balance) + " cash in his account. Transfer is not possible."
				raise ValueError()
		except ValueError:
			return ValueError(err)
		else:
			self.add_cash(cash)
			other.withdraw(cash)
			return self.name + ' has ' + str(int(self.balance)) + ' and ' + other.name + ' has ' + str(
				int(other.balance)) + '.'


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Jeff.name + "'s account:", Jeff.balance)
print(Joe.name + "'s account:", Joe.balance)

print(Jeff.withdraw(2))  # 'Jeff has 68.'
print(Joe.check(Jeff, 50))  # 'Joe has 120 and Jeff has 18.'

print(Jeff.name + "'s account:", Jeff.balance)
print(Joe.name + "'s account:", Joe.balance)

Joe.checking_account = False
print(Jeff.check(Joe, 801231))  # 'Jeff has 98 and Joe has 40.'
print(Jeff.add_cash(20))  # 'Jeff has 118.'
