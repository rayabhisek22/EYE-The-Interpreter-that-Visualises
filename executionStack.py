import graphics
from headersForDataStructures import canvas, wait, headerText, codeText, drawCodeText

bottomx = 20
bottomy = 650
nodeWidth = 400	
nodeHeight = 10
textHeight = 15

functionsx = 440
functionsy = 660
funcnodeWidth = 80
funcnodeHeight = nodeHeight
deafaultFunctionHeight = 175
gap = 10

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

class Graphics:
	def __init__(self):
		self.estack = ExecutionStack()
		self.functions = []

	def makeFunctionFrame(self, name):
		number = len(self.functions)
		self.functions.append(FunctionStack(functionsx + (number%3)*(gap+funcnodeWidth), functionsy - (number//3)*deafaultFunctionHeight))
		self.functions[number].push({})
		self.functions[number].displayName(name)

	def deleteFunctionFrame(self):
		self.functions[-1].delete()
		self.functions.pop()

	def push(self, dictionary, funcIndex):
		if funcIndex == 0:
			self.estack.push(dictionary)
		else:
			self.functions[funcIndex-1].push(dictionary)

	def modifyData(self, key, val, index, funcIndex):
		if funcIndex==0:
			self.estack.modifyData(key, val, index)
		else:
			#print(funcIndex)
			self.functions[funcIndex - 1].modifyData(key, val, index)

	def pop(self, funcIndex):
		if funcIndex == 0:
			self.estack.pop()
		else:
			self.functions[funcIndex - 1].pop()

	def addData(self, key, val, funcIndex):
		if funcIndex == 0:
			self.estack.addData(key, val)
		else:
			self.functions[funcIndex - 1].addData(key, val)


class FuncNode:
	def __init__(self, x, y, nxt):
		self.x = x
		self.y = y
		self.rectangle = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + funcnodeWidth, y + funcnodeHeight))
		self.next = nxt
		self.rectangle.draw(canvas)
		self.data = {} #key->variable name, value->Text object

	def modifyDictionary(self, dictionary):
		for element in dictionary:
			self.data[element] = graphics.Text(graphics.Point(self.x + funcnodeWidth/2, self.y + textHeight/2 + \
				len(self.data)*textHeight), str(element) + " = " + str(dictionary[element]))

	def showDictionary(self):
		for element in self.data:
			self.data[element].draw(canvas)
		wait()

	def addData(self, key, val):
		size = len(self.data)
		self.data[key] = graphics.Text(graphics.Point(self.x + funcnodeWidth/2, self.y + textHeight/2 + \
			size*textHeight), str(key) + " = " + str(val))
		self.data[key].draw(canvas)
		self.rectangle.p1.y-=textHeight
		self.rectangle.undraw()
		self.rectangle.draw(canvas)
		self.y-=textHeight
		for element in self.data:
			self.data[element].move(0, -textHeight)
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


class FunctionStack:
	def __init__(self, x, y):
		self.head = None
		self.x = x
		self.y = y
		self.size = 0

	def displayName(self, name):
		self.nameText = graphics.Text(graphics.Point(self.x + funcnodeWidth/2, self.y + 15), name)
		self.nameText.draw(canvas)

	def push(self, dictionary):
		headerText.setText("Creating a new activation frame")
		drawHeader()
		temp = self.head
		if self.size!= 0:
			self.head = FuncNode(self.x, temp.y-nodeHeight, temp)
		else:
			self.head = FuncNode(self.x, self.y - nodeHeight, temp)
		self.size += 1
		self.head.modifyDictionary(dictionary)
		self.head.showDictionary()

	def addData(self, key, val):
		headerText.setText("Creating variable " + str(key) + " with initial value " + str(val))
		drawHeader()
		self.head.addData(key, val)

	def modifyData(self, key, val, index):
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

	def delete(self):
		while self.size > 0:
			self.pop()
		self.nameText.undraw()

	def pop(self):
		headerText.setText("Deleting the activation frame at the top of the stack")
		drawHeader()
		temp = self.head
		self.size -= 1
		if self.head:
			self.head = self.head.next
		temp.delete()
		wait()

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
		self.y-=textHeight/2
		self.rectangle.p1.y-=textHeight/2
		self.rectangle.undraw()
		self.rectangle.draw(canvas)
		self.data["global"] = graphics.Text(graphics.Point(self.x + nodeWidth/2, self.y + textHeight/2 + \
				len(self.data)*textHeight), str("GLOBAL VARIABLES"))
		self.data["global"].draw(canvas)
		self.data["1filler"] = graphics.Text(graphics.Point(-100, -100), "")

	def showDictionary(self):
		for element in self.data:
			self.data[element].draw(canvas)
		wait()

	def addData(self, key, val):
		size = len(self.data)
		self.data[key] = graphics.Text(graphics.Point(self.x + ((size%2)*(nodeWidth)/2)+(nodeWidth)/4, self.y + textHeight/2 + \
			(size//2)*textHeight), str(key) + " = " + str(val))
		self.data[key].draw(canvas)
		if (size%2 == 0):
			self.rectangle.p1.y-=textHeight
			self.rectangle.undraw()
			self.rectangle.draw(canvas)
			self.y-=textHeight
			for element in self.data:
				self.data[element].move(0, -textHeight)
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
		self.head = Node(bottomx, temp.y-nodeHeight, temp)
		self.size += 1
		self.head.modifyDictionary(dictionary)
		self.head.showDictionary()

	def addData(self, key, val):
		headerText.setText("Creating variable " + str(key) + " with initial value " + str(val))
		drawHeader()
		self.head.addData(key, val)

	def modifyData(self, key, val, index):
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











# f = Graphics()
# f.makeFunctionFrame()
# f.addData("qwerty", 100, 0)
# f.addData("dfb ddcc", 1200, 1)
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# f.makeFunctionFrame()
# wait()
# f.deleteFunctionFrame()
# wait()
# wait()








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
