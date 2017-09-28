####################################################################################################################
#                                    STACKS

class StackNode:
	def __init__(self, x, y, val, nxt):
		self.data = val
		self.next = nxt
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + 3*boxLength, y + boxLength))
		self.rectangle.setFill("light green")
		self.text = graphics.Text(graphics.Point(x + 3*boxLength/2, y + boxLength/2), str(val))
		self.text.setSize(10)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def changeColor(self, color):
		self.rectangle.undraw()
		self.text.undraw()
		self.rectangle.setFill(color)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def delete(self):
		self.text.undraw()
		self.rectangle.undraw()
		del self

class Stack:
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times
		self.name = name
		self.type = type(modelType)
		self.head = None
		self.size = 0
		self.startingPoint = graphics.Point(x, y)
		self.baseRectangle = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x + 3*boxLength,\
		 y - boxLength/2))
		self.baseRectangle.setFill("brown")
		self.baseRectangle.draw(canvas)
		
	def size(self):
		return self.size

	def empty(self):
		return self.size == 0

	def push (self, val):
		if (self.type != type(val)):
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and type of values stored in \
				the stack " + self.name + ": "+ str(self.type) + " are not of the same type")
		headerText.setText("Pushing value " + str(val) + " into the stack " + self.name)
		headerText.draw(canvas)
		wait()
		temp = StackNode(self.startingPoint.x, self.startingPoint.y - self.size*boxLength - 3*boxLength/2, val, self.head)
		self.head = temp
		self.size += 1
		wait()
		headerText.undraw()
		return 

	def top(self):
		if self.size == 0:
			raise Exception("Stack " + self.name + " is empty and you are trying to access its top element")
		headerText.setText("Find the value at the top of the stack " + self.name)
		headerText.draw(canvas)
		self.head.changeColor("blue")
		wait()
		self.head.changeColor("light green")
		headerText.undraw()
		return self.head.data

	def pop(self):
		if self.size == 0:
			raise Exception("Stack " + self.name + " is empty and you are trying to access its top element")
		headerText.setText("Pop the element at the top of the stack " + self.name)
		headerText.draw(canvas)
		self.head.changeColor("red")
		wait()
		temp = self.head
		self.head = temp.next
		self.size -= 1
		temp.delete()
		wait()
		headerText.undraw()
		return 
