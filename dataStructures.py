# Everywhere, you have to pass arguments to decide where yu wanna define each data structure on the canvas
# and when yu delete call the delete function explicitly.

#####    					TODO:
#Add names of the data structures underneath them

import graphics
import time

canvas = graphics.GraphWin("My Interpreter", 1300, 1000)
boxLength = 20
arrowLength = 10
headerPoint = graphics.Point(650, 50)#point where current action will be displayed
headerText = graphics.Text(headerPoint, "")#header text

def wait():
	#define how to wait...sleep or mouse click or something else
	#canvas.getMouse()
	time.sleep(1)

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

	def undraw(self):
		self.line.undraw()
		self.arrowhead1.undraw()
		self.arrowhead2.undraw()

	def shiftAhead(self):
		self.undraw()
		self.line.p1.x += (boxLength + arrowLength)
		self.arrowhead1.p1.x += (boxLength + arrowLength)
		self.arrowhead2.p1.x += (boxLength + arrowLength)
		self.line.p2.x += (boxLength + arrowLength)
		self.arrowhead1.p2.x += (boxLength + arrowLength)
		self.arrowhead2.p2.x += (boxLength + arrowLength)
		self.draw()

	def shiftBehind(self):
		self.undraw()
		self.line.p1.x -= (boxLength + arrowLength)
		self.arrowhead1.p1.x -= (boxLength + arrowLength)
		self.arrowhead2.p1.x -= (boxLength + arrowLength)
		self.line.p2.x -= (boxLength + arrowLength)
		self.arrowhead1.p2.x -= (boxLength + arrowLength)
		self.arrowhead2.p2.x -= (boxLength + arrowLength)
		self.draw()

class SinglyLinkedListNode:
	#data and next is stored
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
			text.draw(canvas)
		else:
			raise Exception("The new value: " + str(newVal) + " and the old value: " + str(self.data)\
			 + " are not of the same type")

	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.arrow.undraw()
		del self

	def changeColor(self, color):
		self.rectangle.undraw()
		self.rectangle.setFill(color)
		self.rectangle.draw(canvas)
		self.text.undraw()
		self.text.draw(canvas)

	def probe(self):
		self.changeColor("light blue")

	def unprobe(self):
		self.changeColor("light green")

	def success(self):
		self.changeColor("blue")

	def shiftAhead(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.text.anchor.x += (boxLength + arrowLength)
		self.rectangle.p1.x += (boxLength + arrowLength)
		self.rectangle.p2.x += (boxLength + arrowLength)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.shiftAhead()

	def shiftBehind(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.text.anchor.x -= (boxLength + arrowLength)
		self.rectangle.p1.x -= (boxLength + arrowLength)
		self.rectangle.p2.x -= (boxLength + arrowLength)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.shiftBehind()

class SinglyLinkedList:
	#head and size is stored
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times
		self.name = name
		self.type = type(modelType)
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
		headerText.setText("Inserting " + str(val) + " at index 0 in the singly linked list " + self.name)
		headerText.draw(canvas)
		if type(val) == self.type:
			wait()
			temp = SinglyLinkedListNode(val, self.startingPoint.x + arrowLength - 2*boxLength- \
				self.size*(arrowLength + boxLength), self.startingPoint.y, self.head)
			self.size += 1
			self.head = temp
			headerText.undraw()
			return
		else:
			wait()
			headerText.undraw()
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and the old value: "\
			 + str(self.type) + " are not of the same type in the singly linked list " + self.name)		

	def empty(self):
		return self.size == 0

	def changeBaseRectangleColor(self, color):
		self.baseRectangle.undraw()
		self.baseRectangle.setFill(color)
		self.baseRectangle.draw(canvas)
		self.baseText.undraw()
		self.baseText.draw(canvas)

	def get(self, val):#returns None is not found, else returns the node.
		headerText.setText("get(" + str(val) + ") in singly linked list " + self.name)
		headerText.draw(canvas)
		temp = self.head
		if (temp == None):
			self.changeBaseRectangleColor("light blue")
			wait()
			self.changeBaseRectangleColor("green")
			headerText.undraw()
			return None
		while (temp and temp.data != val):
			temp.probe()
			wait()
			temp.unprobe()
			temp = temp.next
		if temp:
			temp.success()
			wait()
			temp.unprobe()
			headerText.undraw()
			return temp
		else:
			self.changeBaseRectangleColor("light blue")
			wait()
			self.changeBaseRectangleColor("green")
			headerText.undraw()
			return None	

	def indexOf(self, val):#returns -1 if not found
		headerText.setText("indexOf(" + str(val) + ") in singly linked list " + self.name)
		headerText.draw(canvas)
		temp = self.head
		if (temp == None):
			self.changeBaseRectangleColor("light blue")
			wait()
			self.changeBaseRectangleColor("green")
			headerText.undraw()
			return -1
		count = 0
		while (temp!= None and temp.data != val):
			temp.probe()
			wait()
			temp.unprobe()
			count += 1
			temp = temp.next
		if temp:
			temp.success()
			wait()
			temp.unprobe()
			headerText.undraw()
			return count
		else:
			self.changeBaseRectangleColor("light blue")
			wait()
			self.changeBaseRectangleColor("green")
			headerText.undraw()
			return -1		

	def find(self, val):
		#same as get but without the graphics
		temp = self.head
		while (temp and temp.data != val):
			temp = temp.next
		return temp

	def erase(self, val):
		headerText.setText("erase(" + str(val) + ") in a singly linked list " + self.name)
		time.sleep(1)
		headerText.draw(canvas)
		target = self.find(val)
		if target == None:
			headerText.undraw()
			headerText.setText(str(val) + " not in the singly linked list " + self.name + " => do nothing")
			headerText.draw()
			wait()
			headerText.undraw()
			return
		else:
			target.changeColor("red")
			wait()
			temp = self.head
			while temp != target:
				temp.shiftAhead()
				temp = temp.next
			temp.delete()
			headerText.undraw()
			self.size -= 1
			return 

	def insert(self, index, val):
		if (index > self.size):
			wait()
			raise Exception("The index " + str(index) + " is out of range in the singly linked list " + self.name)
		if (type(val) != self.type):
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and type of values stored in \
				the singly linked list " + sel.name + ": "+ str(self.type) + " are not of the same type")
		if index == 0:
			self.push(val)
			return
		ogIndex = index
		headerText.setText("Inserting " + str(val) + " at index " + str(index) + " in the singly linked list "+self.name)
		headerText.draw(canvas)
		wait()
		temp = self.head
		self.size += 1
		while (index > 0):
			index -= 1
			temp.shiftBehind()
			temp = temp.next
			wait()
		newNode = SinglyLinkedListNode(val, self.startingPoint.x - (self.size - ogIndex - 1) * (boxLength + \
			arrowLength) - 2*boxLength + arrowLength, self.startingPoint.y, temp.next)
		temp.next = newNode
		wait()
		headerText.undraw()
		return

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

#######################################################################################################################
# 															QUEUE





a = Stack(500, 500, 10, "myStack")
a.push(40)
a.push(100)
a.top()
a.pop()
a.pop()
for i in range(2):
	wait()
"""
a = SinglyLinkedList(1000, 100, 10)
a.insert(0,9)
a.insert(0,10)
a.insert(0,13)
a.insert(0, 20)
print (a.get(10))
#print(a.indexOf(20))
a.erase(9)
a.insert(2, 1)
b = input()"""