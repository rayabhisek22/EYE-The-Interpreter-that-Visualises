import graphics
from headersForDataStructures import canvas, wait, headerText

bottomx = 20
bottomy = 600
nodeWidth = 400	
nodeHeight = 115
textHeight = 14

arrayElementWidth = arrayElementHeight = 20
arrayBegy=60
arrayBegx=20
numberOfArrays=0
arrayOffset = 50

def drawHeader():
	try:
		headerText.draw(canvas)
	except:
		headerText.undraw()
		headerText.draw(canvas)

class Node:
	def __init__(self, x, y, nxt):
		self.x = x
		self.y = y
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + nodeWidth, y + nodeHeight))
		self.next = nxt
		self.rectangle.draw(canvas)
		self.data = {} #key->variable name, value->Text object

	def modifyDictionary(self, dictionary):
		for element in dictionary:
			self.data[element] = graphics.Text(graphics.Point(self.x + nodeWidth/2, self.y + textHeight/2 + \
				len(self.data)*textHeight), str(element) + " = " + str(dictionary[element]))

	def addGlobal(self):
		self.data["global"] = graphics.Text(graphics.Point(self.x + nodeWidth/2, self.y + textHeight/2 + \
				len(self.data)*textHeight), str("GLOBAL VARIABLES"))
		self.data["global"].draw(canvas)

	def showDictionary(self):
		for element in self.data:
			self.data[element].draw(canvas)
		wait()

	def addData(self, key, val):
		self.data[key] = graphics.Text(graphics.Point(self.x + nodeWidth/2, self.y + textHeight/2 + \
			len(self.data)*textHeight), str(key) + " = " + str(val))
		self.data[key].draw(canvas)
		wait()

	def modifyData(self, key, newVal):
		self.data[key].undraw()
		self.data[key].setText(str(key) + " = " + str(newVal))
		self.data[key].draw(canvas)
		wait()

	def delt(self,key):
		self.data[key].undraw()
		del self.data[key]

	def delete(self):
		for element in self.data:
			self.data[element].undraw()
		self.rectangle.undraw()
		del self


class ExecutionStack:
	def __init__(self):
		self.head = Node(bottomx, bottomy, None)
		self.head.addGlobal()
		self.size = 1

	def push(self, dictionary):
		headerText.setText("Creating a new activation frame")
		drawHeader()
		temp = self.head
		self.head = Node(bottomx, bottomy - self.size*nodeHeight, temp)
		self.size += 1
		self.head.modifyDictionary(dictionary)
		self.head.showDictionary()

	def addData(self, key, val, funcIndex):
		headerText.setText("Creating variable " + str(key) + " with initial value " + str(val))
		drawHeader()
		self.head.addData(key, val)

	def modifyData(self, key, val, index, funcIndex):
		headerText.setText("Assigning value " + str(val) + " to variable " + str(key))
		drawHeader()
		temp = self.head
		while (index > 0):
			temp = temp.next
			index -=1
		temp.modifyData(key, val)

	def deleteData(self,key,index):
		temp = self.head
		while (index > 0):
			temp = temp.next
			index -=1
		temp.delt(key)


	def pop(self):
		headerText.setText("Deleting the activation frame at the top of the stack")
		drawHeader()
		temp = self.head
		self.size -= 1
		self.head = self.head.next
		temp.delete()
		wait()


######################################################################################################################

												#ARRAYS

######################################################################################################################

class ArrayNode:
	def __init__(self, x, y, val):
		self.data = val
		self.rectangle = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x + arrayElementWidth, y\
		 + arrayElementHeight))
		self.rectangle.setFill("grey")
		self.text = graphics.Text(graphics.Point(x + arrayElementWidth/2, y + arrayElementHeight/2), str(val))
		self.text.setSize(10)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

	def update(self, newVal):
		self.text.undraw()
		self.val = newVal
		self.text.setText(str(newVal))
		self.text.draw(canvas)

	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()

	def changeColor(self, color):
		self.rectangle.undraw()
		self.rectangle.setFill(color)
		self.text.undraw()
		self.rectangle.draw(canvas)
		self.text.draw(canvas)

class VisualArray:
	def __init__(self, size, name):
		global numberOfArrays
		self.name = name
		self.y = arrayBegy + numberOfArrays*3*arrayElementHeight/2
		self.x = arrayBegx + arrayOffset
		self.nameText = graphics.Text(graphics.Point(arrayBegx/2 + arrayOffset/2, self.y + arrayElementHeight/2)\
			, name)
		self.nameText.setSize(11)
		self.nameText.draw(canvas)
		self.size = size
		self.array = []
		for i in range(size):
			self.array.append(ArrayNode(self.x + i*arrayElementWidth, self.y,""))
		numberOfArrays += 1

	def update(self, index, val):
		headerText.setText("Updating the value of " + self.name + "["  + str(index) + "]")
		drawHeader()
		self.array[index].update(val)
		self.probe(index)

	def probe(self, index):
		headerText.setText("Accessing the value of " + self.name + "["  + str(index) + "]")
		drawHeader()
		self.array[index].changeColor("lightblue")
		wait()
		self.array[index].changeColor("gray")

	def delete(self):
		for i in range(self.size):
			self.array[index].delete()
