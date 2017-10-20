from headersForDataStructures import *

textHeight = 20
textWidth = 20
boxWidth = 15
boxHeight = 15

class Node:
	def __init__(self, x, y, val, nxt):
		self.arrow = rightArrow(x, y)
		if val != "NULL":
			self.rectangle = graphics.Rectangle(graphics.Point(x + arrowLength, y - boxHeight/2), graphics.Point\
				(x + arrowLength + boxWidth, y + boxHeight/2))
			self.rectangle.setFill("lightgreen")
			self.text = graphics.Text(graphics.Point(x + arrowLength + boxWidth/2, y), str(val))
			self.data = val
		else:
			self.rectangle = graphics.Rectangle(graphics.Point(x + arrowLength, y - boxHeight/2), graphics.Point\
				(x + arrowLength + 2*boxWidth, y + boxHeight/2))
			self.rectangle.setFill("lightgreen")
			self.text = graphics.Text(graphics.Point(x + arrowLength + boxWidth, y), "NULL")
			self.text.setSize(10)
			self.data = None
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.draw()
		self.next = nxt

	def undraw(self):
		self.rectangle.undraw()
		self.text.undraw()

	def draw(self):
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def changeColor(self, color):
		self.undraw()
		self.rectangle.setFill(color)
		self.draw()

	def probe(self):
		self.changeColor("lightblue")
		wait()
		self.changeColor("lightgreen")

	def successful(self):
		self.changeColor("blue")
		wait()
		self.changeColor("lightgreen")

	def toDelete(self):
		self.changeColor("red")
		wait()

	def shiftBehind(self):
		self.rectangle.move(boxWidth + arrowLength, 0)
		self.text.move(boxWidth + arrowLength, 0)
		self.arrow.shift(boxWidth + arrowLength, 0)

	def shiftAhead(self):
		self.rectangle.move(- boxWidth - arrowLength, 0)
		self.text.move(- boxWidth - arrowLength, 0)
		self.arrow.shift(- boxWidth - arrowLength, 0)

	def delete(self):
		self.arrow.undraw()
		self.text.undraw()
		self.rectangle.undraw()
		del self

class List:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.head = Node(x, y, "NULL", None)

	def push(self, val):
		self.head = Node(self.x, self.y, val, self.head)
		temp = self.head.next
		while temp:
			temp.shiftBehind()
			temp = temp.next
		wait()

	def find(self, val):
		temp = self.head
		while temp and temp.data != val:
			temp.probe()
			temp = temp.next
		if temp:
			temp.successful()
		return temp

	def erase(self, val):
		temp = self.head
		if temp.data == val:
			temp.toDelete()
			self.head = self.head.next
			temp.delete()
			temp = self.head
			while temp != None:
				temp.shiftAhead()
				temp = temp.next
		else:
			while temp.next and temp.next.data != val:
				temp = temp.next
			if temp.next:
				temp.next.toDelete()
				temp2 = temp.next
				temp.next = temp2.next
				temp2.delete()
				temp = temp.next
				while temp:
					temp.shiftAhead()
					temp = temp.next
			else:
				headerText.setText(str(val) + " is not present in the hash table")
				drawHeader()
				wait()
				headerText.undraw()

	def delete(self):
		temp = self.head
		while temp:
			temp.delete()
			temp = temp.next
		del self

class Component:
	def __init__(self, x, y, val):
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x+textWidth, y+textHeight))
		self.rectangle.setFill("light blue")
		self.text = graphics.Text(graphics.Point(x + textWidth/2 , y + textHeight/2), str(val))
		self.list = List(x + textWidth, y + textHeight/2)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def highlight(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.rectangle.setFill("blue")
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		wait()
		self.rectangle.undraw()
		self.text.undraw()
		self.rectangle.setFill("light blue")
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.list.delete()
		del self

class HashTable:
	def __init__(self, divisor, x, y, modelType, name):
		self.components = []
		if divisor > 30:
			raise Exception("The divisor with which the hash table " + name + " is being created is too large. Please select a"+\
				"value that is lesser than 30 for ease of graphical representation.")
		if divisor > 15:
			for i in range(15):
				self.components.append(Component(x, y + i*textHeight, i))
			for i in range(divisor - 15):
				self.components.append(Component(x + 200, y + i*textHeight, i + 15))
		else:
			for i in range(divisor):
				self.components.append(Component(x, y +  i*textHeight, i))
		self.divisor = divisor
		self.size = 0
		self.type = type(modelType)
		self.name = name
		self.nameText = graphics.Text(graphics.Point(x + 200, y - 12), self.name)
		self.nameText.draw(canvas)

	def push(self, val):
		if type(val) != self.type:
			raise Exception("The type of value you are trying to push into the hash table :" + str(type(val)) + " \
				is different from the values supposed to be stored in the hash table named "+self.name+": " + str(self.type))
		else:
			headerText.setText("Inserting value: " + str(val) + " with key: " + str(val%self.divisor) + " into the hash table " + \
				str(self.name))
			drawHeader()
			key = val % self.divisor
			self.components[key].highlight()
			self.components[key].list.push(val)
			headerText.undraw()

	def find(self, val):
		if type(val) != self.type:
			raise Exception("The type of value you are trying to find in the hash table :" + str(type(val)) + " \
				is different from the values supposed to be stored in the hash table named "+self.name+": " + str(self.type))
		else:
			headerText.setText("Searching for value: " + str(val) + " with key: " + str(val%self.divisor) + " in the hash table " + \
				str(self.name))
			drawHeader()
			key = val % self.divisor
			self.components[key].highlight()
			if self.components[key].list.find(val):
				return False
			else:
				return True
			headerText.undraw()

	def erase(self, val):
		if type(val) != self.type:
			raise Exception("The type of value you are trying to erase from the hash table :" + str(type(val)) + " \
				is different from the values supposed to be stored in the hash table named "+self.name+": " + str(self.type))
		else:
			headerText.setText("Erasing value: " + str(val) + " with key: " + str(val%self.divisor) + " from the hash table " + \
				str(self.name))
			drawHeader()
			key = val % self.divisor
			self.components[key].highlight()
			self.components[key].list.erase(val)
			headerText.undraw()

	def delete(self):
		for component in self.components:
			component.delete()
		self.nameText.undraw()
		del self
