# Everywhere, you have to pass arguments to decide where yu wanna define each data structure on the canvas
# and when yu delete call the delete function explicitly.

import graphics

canvas = graphics.GraphWin("My Interpreter", 1300, 1000)
boxLength = 20
arrowLength = 10

class rightArrow:
	def __init__(self, x, y):
		self.line = graphics.Line(graphics.Point(x,y), graphics.Point(x + arrowLength, y))
		self.arrowhead1 = graphics.Line(graphics.Point(x+arrowLength,y), graphics.Point(x + arrowLength - 5,\
		 y-4))
		self.arrowhead2 = graphics.Line(graphics.Point(x+arrowLength,y), graphics.Point(x + arrowLength - 5,\
		 y+4))
	
	def draw(self):
		self.line.draw(canvas)
		self.arrowhead1.draw(canvas)
		self.arrowhead2.draw(canvas)

	def delete(self):
		self.line.undraw()
		self.arrowhead1.undraw()
		self.arrowhead2.undraw()

class SinglyLinkedListNode:
	def __init__(self, val, x1, y1, nxt):
		self.next = nxt
		self.data = val
		self.rectangle = graphics.Rectangle(graphics.Point(x1, y1), graphics.Point(x1 + boxLength\
			, y1 + boxLength))
		self.rectangle.draw(canvas)
		self.rectangle.setFill("light green")
		self.text = graphics.Text(graphics.Point(x1 + boxLength/2, y1 + boxLength/2), str(self.data))
		self.text.setSize(10)
		self.text.draw(canvas)
		self.arrow = rightArrow(x1 + boxLength,y1 + boxLength/2 )
		self.arrow.draw()

	def update(self, newVal):
		if type(self.data == type(newVal)):
			self.data = newVal
			text.undraw()
			text.setText(str(newVal))
			text.draw()
		else:
			raise Exception("The new value: " + str(newVal) + " and the old value: " + str(self.data)\
			 + " are not of the same type")

	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()
		del self

class SinglyLinkedList:
	def __init__(self, x, y, modelType): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times
		self.stackType = type(modelType)
		self.head = None
		self.size = 0
		self.startingPoint = graphics.Point(x, y)
		self.baseRectangle = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x + 2*boxLength,\
		 y + boxLength))
		self.baseText = graphics.Text(graphics.Point(x + boxLength, y + boxLength/2), "NULL")
		self.baseText.setSize(11)
		self.baseRectangle.setFill("green")
		self.baseRectangle.draw(canvas)
		self.baseText.draw(canvas)

	def size(self):
		return self.size

	def top(self):
		return self.head.data

	def push(self, val):
		if type(val) == self.stackType:
			temp = SinglyLinkedListNode(val, self.startingPoint.x + arrowLength - 2*boxLength- \
				self.size*(arrowLength + boxLength), self.startingPoint.y, self.head)
			self.size += 1
			self.head = temp
		else:
			raise Exception("The new value: " + str(newVal) + " and the old value: " + str(self.data)\
			 + " are not of the same type")			


a = SinglyLinkedList(1000, 100, 10)
a.push(9)
a.push(10)
b = input()