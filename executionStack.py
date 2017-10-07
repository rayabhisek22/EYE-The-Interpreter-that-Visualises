import graphics
from headersForDataStructures import canvas, wait, headerText

bottomx = 20
bottomy = 500
nodeWidth = 600
nodeHeight = 100
textHeight = 14

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

	def delete(self):
		for element in self.data:
			self.data[element].undraw()
		self.rectangle.undraw()
		del self


class ExecutionStack:
	def __init__(self):
		self.head = Node(bottomx, bottomy, None)
		self.size = 1

	def push(self, dictionary):
		temp = self.head
		self.head = Node(bottomx, bottomy - self.size*nodeHeight, temp)
		self.size += 1
		self.head.modifyDictionary(dictionary)
		self.head.showDictionary()

	def addData(self, key, val):
		self.head.addData(key, val)

	def modifyData(self, key, val, index):
		temp = self.head
		while (index > 0):
			temp = temp.next
			index -=1
		temp.modifyData(key, val)

	def pop(self):
		temp = self.head
		self.size -= 1
		self.head = self.head.next
		temp.delete()
		wait()
