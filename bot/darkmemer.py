import sys
sys.path.append('/test/cogs/')
import market

class life:
	def __init__(self, name, nick, market):
		self.person = self.person(name, nick, market)

	class person:
		def __init__(self, name, nick, market):
			self.items = market.items
			self.__name = name
			self.__nick = nick
			self.wallet = 200
			self.__bank = 100
			self.userItems = {}
		
		def profile(self):
			return 'Name : ' + self.__name + '\nNick : ' + self.__nick + '\nWallet : ' + str(self.wallet) + '\nBank : ' + str(self.__bank) + '\nInventory : ' + str(self.userItems)
		
		def setNick(self, newNick):
			self.__nick = newNick

		def balance(self):
			return (self.wallet, self.__bank)
		
		def spend(self, amount):
			if self.wallet >= amount:
				self.wallet -= amount
				return True
			return False

		def inventory(self):
			return self.userItems

		def withdraw(self, amount: int):
			if self.__bank >= amount:
				self.__bank -= amount
				self.wallet += amount
				return True
			return False
		
		def deposit(self, amount: int):
			if self.wallet >= amount:
				self.__bank += amount
				self.wallet -= amount
				return True
			return False
		
		def buyItem(self, name, quantity):
			if self.wallet >= quantity * self.items.listOfItems[name]:
				if not name in [*self.userItems]:
					self.spend(quantity * self.items.listOfItems[name])
					self.userItems[name] = [quantity, self.items.listOfItems[name] * quantity]
					return True
				self.spend(quantity * self.items.listOfItems[name])
				self.userItems[name][0] += quantity
				self.userItems[name][1] += self.items.listOfItems[name] * quantity
				return True
			return False
	
class pet:
	def __init__(self, name):
		self.name = name
	
	def petProfile(self):
		pass

	def details(self):
		pass

	def feed(self, money):
		return 'you fed the pet'
	
	def pat(self):
		return 'you patted pet'

l = life('Superman', 'Clerk', market = market)

def addPlayer(name, nick, market = market):
	l1 = life(name = name, nick = nick, market = market)
	return l1