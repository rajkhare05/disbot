class market:
	def __init__(self):
		# self.listOfItems = {'apple' : 50, 'bun' : 10,'cell phone' : 5000, 'ball' : 10}
		self.listOfItems = {}
	
	def addItems(self, name, price):
		self.listOfItems[name] = price
	
	def showItems(self):
		return self.listOfItems
	
	def removeItems(self, name):
		self.listOfItems.pop(name)
	
	def changePrice(self, name, price):
		self.listOfItems[name] = price

items = market()
items.addItems('apple', 100)
items.addItems('fidget-spinner', 1000)
items.addItems('cake', 200)
items.addItems('duck', 20)