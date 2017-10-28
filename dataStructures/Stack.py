from .headersForDataStructures import *
####################################################################################################################

#                                    STACKS

numberofstacks=[0]

##Class to represent a node in a stack both graphically and as an Abstract Data Type element.
class StackNode:
	##Constructor for the node
	#
	#@param x - the x coordinate of the bottom left corner of the node on the canvas.
	#@param y - the y coordinate of the bottom left corner of the node on the canvas.
	#@param val - the value to be stored in the node
	#@param nxt - the node that comes after the current one in the stack
	def __init__(self, x, y, val, nxt):
		self.data = val
		self.next = nxt
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + 3*boxLength, y + boxLength))
		self.rectangle.setFill("light green")
		self.text = graphics.Text(graphics.Point(x + 3*boxLength/2, y + boxLength/2), str(val))
		self.text.setSize(10)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	##Change the color of the node
	#
	#@param color - the color to which the node has to be changed.
	def changeColor(self, color):
		self.rectangle.undraw()
		self.text.undraw()
		self.rectangle.setFill(color)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	##Delete the node after undrawing all the graphical components from the canvas.	
	def delete(self):
		self.text.undraw()
		self.rectangle.undraw()
		del self

##@brief Pre-defined data structure to represent a Stack
#
#Contians all the data members and member functions to represent a standard singly linked list Abstract Data Type
#In addition to this, it contains all the needed data members and functions to represent the data structure on the canvas.
#Usual functions have been modified to allow for the required changes to the graph as well.
class Stack:
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times

	##Constructor for the class
	#
	#@param x - the x coordinate of the bottom left corner of the stack.
	#@param y - the y coordinate of the bottom left corner of the stack.
	#@param modelType - An object of the type to be stored in the stack, to ensure that all elements in the list are of the same type
	#as in C++
	#@param name - The name given by the user to an instance of this class.
		self.nameText = graphics.Text(graphics.Point(x + 3*boxLength/2, y + boxLength), name)
		self.nameText.draw(canvas)
		self.name = name
		self.type = type(modelType)
		self.head = None
		self.size = 0
		self.startingPoint = graphics.Point(x, y)
		self.baseRectangle = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x + 3*boxLength,\
		 y - boxLength/2))
		self.baseRectangle.setFill("brown")
		self.baseRectangle.draw(canvas)
		
	##Return the size of the stack - no graphics
	def size(self):
		return self.size

	##Return whether or not the stack is empty - no graphics
	def empty(self):
		return self.size == 0

	##Push a new value to the top of the stack-raises an exception if the new value  is not of the same type as the rest of the elements
	#of the stack
	#
	#@param val - new value to be pushed to the top of the stack
	def push (self, val):
		if (self.type != type(val)):
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and type of values stored in \
				the stack " + self.name + ": "+ str(self.type) + " are not of the same type")
		headerText.setText("Pushing value " + str(val) + " into the stack " + self.name)
		drawHeader()
		wait()
		temp = StackNode(self.startingPoint.x, self.startingPoint.y - self.size*boxLength - 3*boxLength/2, val, self.head)
		self.head = temp
		self.size += 1
		wait()
		headerText.undraw()
		return 

	##Return the value at the top of the stack
	def top(self):
		if self.size == 0:
			raise Exception("Stack " + self.name + " is empty and you are trying to access its top element")
		headerText.setText("Find the value at the top of the stack " + self.name)
		drawHeader()
		self.head.changeColor("blue")
		wait()
		self.head.changeColor("light green")
		headerText.undraw()
		return self.head.data

	##Delete the value at the top of the stack and raises an exception if the stack is empty
	def pop(self):
		if self.size == 0:
			raise Exception("Stack " + self.name + " is empty and you are trying to access its top element")
		headerText.setText("Pop the element at the top of the stack " + self.name)
		drawHeader()
		self.head.changeColor("red")
		wait()
		temp = self.head
		self.head = temp.next
		self.size -= 1
		temp.delete()
		wait()
		headerText.undraw()
		return 

	##Delete the stack if it goes out of scope - explicitly undraws all related graphics
	def delete(self):
		global numberofstacks
		numberofstacks[0] -= 1
		temp = self.head
		while temp:
			self.head = temp.next
			temp.delete()
			temp = self.head
		self.nameText.undraw()
		self.baseRectangle.undraw()
		del self
