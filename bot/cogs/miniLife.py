class life:
	def __init__(self, name, nick):
		self.newPlayer = self.person(name, nick)

	class person:
		def __init__(self, name, nick):
			self.__name = name
			self.__nick = nick
			self.wallet = 100
			self.__bank = 100
			self.userItems = {}
		
		def setNick(self, newNick):
			self.__nick = newNick

		def balance(self):
			return (self.wallet, self.__bank)
		
		def spend(self, amount):
			if self.wallet >= amount:
				self.wallet -= amount
			return False

		def inventory(self):
			return self.userItems

		def withdraw(self, amount: int):
			self.__bank -= amount
			self.wallet += amount
		
		def addMoney(self, amount: int):
			self.wallet += amount
		
		def buyItem(self, name, quantity):
			if self.wallet >= items.listOfItems[name]:
				self.spend(items.listOfitems[name])
				return 'Bought !'
			return 'Low balance !'

		# def buyItem()

		# def sellItem(self, item):
		# 	if item in self.items:
		# 		for i in len(self.items):
		# 			if self.items[i] == item:
		# 				self.items.pop(i)
		# 				self.addMoney()
		# 				return 'Item sold'			
		# 	return 'Item not found !'

		class items:
			def __init__(self):
				# self.listOfItems = {'apple' : 50, 'bun' : 10,'cell phone' : 5000, 'ball' : 10}
				self.listOfItems = {}
			
			def addItems(self, name, items):
				self.listOfItems[name] = items
			
			def removeItems(self, name):
				self.listOfItems.pop(name)
			
			def changePrice(self, name, price):
				self.listOfItems[name] = price
		
	
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
