from .headersForDataStructures import *

textHeight = 20
textWidth = 20
boxWidth = 25
boxHeight = 15

##Class which stored all data related to one node in one list of the hash table including the value to be stored, the node that comes next
#an arrow pointing from the previous node to this one and a rectangle with the value stored in the node displayed inside it
class Node:
	##Constructor for the node
	#
	#@param x - the y coordinate of the start of the arrow from the previous node
	#@param y - the x coordinate of the start of the arrow from the previous node
	#@param val - the value to be stored in the node
	#@param nxt - the node that comes after it in the list
	def __init__(self, x, y, val, nxt):
		self.arrow = rightArrow(x, y)
		if val != "NULL":
			self.rectangle = graphics.Rectangle(graphics.Point(x + arrowLength, y - boxHeight/2), graphics.Point\
				(x + arrowLength + boxWidth, y + boxHeight/2))
			self.rectangle.setFill("lightgreen")
			self.text = graphics.Text(graphics.Point(x + arrowLength + boxWidth/2, y), str(val))
			self.data = val
			self.text.setSize(10)
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

	##Function to undraw the rectangle and the text
	def undraw(self):
		self.rectangle.undraw()
		self.text.undraw()

	##Function to redraw the rectangle and the text
	def draw(self):
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	##Function to change the background color of the rectangle
	#
	#@param color - the color to which the background is to be changed
	def changeColor(self, color):
		self.undraw()
		self.rectangle.setFill(color)
		self.draw()

	##Function to graphically denoted that we are probing this node
	def probe(self):
		self.changeColor("lightblue")
		wait()
		self.changeColor("lightgreen")

	##Function to graphically denote that the search for a given node is successful and this is the selected node
	def successful(self):
		self.changeColor("blue")
		wait()
		self.changeColor("lightgreen")

	##Function to graphically denote that we have found a node that is to be deleted
	def toDelete(self):
		self.changeColor("red")
		wait()

	##Function to shift the node behind in the list
	def shiftBehind(self):
		self.rectangle.move(boxWidth + arrowLength, 0)
		self.text.move(boxWidth + arrowLength, 0)
		self.arrow.shift(boxWidth + arrowLength, 0)

	##Function to graphically shift the node ahead in the list
	def shiftAhead(self):
		self.rectangle.move(- boxWidth - arrowLength, 0)
		self.text.move(- boxWidth - arrowLength, 0)
		self.arrow.shift(- boxWidth - arrowLength, 0)

	##Function to undraw and then delete the node
	def delete(self):
		self.arrow.undraw()
		self.text.undraw()
		self.rectangle.undraw()
		del self

##Class to store the list associated with one element of the hash table
class List:
	##Constructor for the given class
	#
	#@param x - the x coordinate for the starting point of the list
	#@param y - the y coordinate for the starting point of the list
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.head = Node(x, y, "NULL", None)

	##Function to push a new value in the list
	#
	#@param val - the value that is to be pushed into the list
	def push(self, val):
		self.head = Node(self.x, self.y, val, self.head)
		temp = self.head.next
		while temp:
			temp.shiftBehind()
			temp = temp.next
		wait()

	##Function to find some value in the list
	#
	#@param val - the value to be searched for
	def find(self, val):
		temp = self.head
		while temp and temp.data != val:
			temp.probe()
			temp = temp.next
		if temp:
			temp.successful()
		return temp

	##Function to delete some value from the list. Does nothing if the value is not found
	#
	#@param val - the value to be deleted from the list
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

	##Function to undraw the list and delete all the data stored in it
	def delete(self):
		temp = self.head
		while temp:
			temp.delete()
			temp = temp.next
		del self

##Class that stored a key and a list associated with it
class Component:
	##Constructor for the class
	#
	#@x - the x coordinate of the left top of the key
	#@y - the y coordinate of the left top of the key
	#@val - the key associated with the class
	def __init__(self, x, y, val):
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x+textWidth, y+textHeight))
		self.rectangle.setFill("light blue")
		self.text = graphics.Text(graphics.Point(x + textWidth/2 , y + textHeight/2), str(val))
		self.list = List(x + textWidth, y + textHeight/2)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	##Function to highlight that this is the key corresponding to the value in question
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

	##Function to undraw and delete the entire component
	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.list.delete()
		del self

##Class to represent the actual hash table itself. This includes open hasing using the remainder function as a has function
#The user has the liberty to choose the divisor. The divisor has been limited to 30 for ease of representation
class HashTable:
	##Constructor for the class
	#
	#@param divisor - the divisor for the remainder function that serves as the has function 
	#@param x - the x coordinate of the top left corner of the hash table
	#@param y - the y coordinate of the top left corner of the hash table
	#@param modelType - a number denoting the model type that is to be stored in the has table
	#@param name - the name that the user has given for the hash table
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

	##Function to add a new value in the hash table. This does not check if the value is already there and hence, allows for repitition
	#
	#@param val - the new value that is to be pushed into the hash table
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

	##Function to search for a given value in the hash table. Returns true if the value is found and false if it is not
	#
	#@param val - the value that is being searched for
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
				return True
			else:
				return False
			headerText.undraw()

	##Function to erase a given value from the hash table. Does nothing if the value is not found
	#
	#@param val - the value that is to be erased from the hash table
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

	##Function to undraw the hash table and deletes its components when it goes out of scope.
	def delete(self):
		for component in self.components:
			component.delete()
		self.nameText.undraw()
		del self
