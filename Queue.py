from headersForDataStructures import *
#######################################################################################################################
# 															QUEUE

def drawHeader():
	try:
		headerText.draw(canvas)
	except:
		headerText.undraw()
		headerText.draw(canvas)

class QueueNode:
	def __init__(self, x, y, val, nxt):
		self.data = val
		self.next = nxt
		self.circle = graphics.Circle(graphics.Point(x, y), circleRadius)
		self.circle.setFill("light green")
		self.text = graphics.Text(graphics.Point(x, y), str(val))
		self.text.setSize(10)
		self.arrow = rightArrow(x + circleRadius, y)
		self.circle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.draw()

	def changeColor(self, color):
		self.circle.undraw()
		self.circle.setFill(color)
		self.text.undraw()
		self.circle.draw(canvas)
		self.text.draw(canvas)

	def shiftAhead(self):
		self.circle.move(arrowLength + 2*circleRadius, 0)
		self.text.move(arrowLength + 2*circleRadius, 0)
		self.arrow.shiftInQueue()

	def shiftBehind(self):
		self.circle.move(-(arrowLength + 2*circleRadius), 0)
		self.text.move(-(arrowLength + 2*circleRadius), 0)
		self.arrow.shiftBehindInQueue()

	def delete(self):
		self.circle.undraw()
		self.text.undraw()
		self.arrow.undraw()
		del self

class Queue:
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times
		self.name = name
		self.type = type(modelType)
		self.head = None
		self.tail = None
		self.size = 0
		self.startingPoint = graphics.Point(x, y)
		self.text = graphics.Text(graphics.Point(self.startingPoint.x + 25, self.startingPoint.y), "FRONT")
		self.text.setSize(10)
		self.text.draw(canvas)

	def empty(self):
		return self.size == 0

	def size(self):
		return self.size

	def pushBack(self, val):
		#push to the end of the queue
		headerText.setText("Pushing " + str(val) + " to the back of the queue " + self.name)
		drawHeader()
		if self.type == type(val):
			temp = QueueNode(self.startingPoint.x - self.size*(2*circleRadius + arrowLength) - circleRadius - arrowLength\
			, self.startingPoint.y, val, self.head)
			self.head = temp
			wait()
			self.size += 1
			if self.size == 1:
				self.tail = self.head
			headerText.undraw()
			return
		else:
			wait()
			headerText.undraw()
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and the type of values stored in \
				the queue " + self.name + " : " + str(self.type) + " are not the same")

	def pushFront(self, val):
		#push to the front of the queue
		headerText.setText("Pushing " + str(val) + " to the front of the queue " + self.name)
		drawHeader()
		if self.type == type(val) and self.size > 0:
			current = self.head
			while current != None:
				current.shiftBehind()
				current = current.next
			temp = QueueNode(self.startingPoint.x - circleRadius - arrowLength, self.startingPoint.y, val, None)
			self.tail.next = temp
			self.tail = temp
			wait()
			self.size += 1
			headerText.undraw()
			return
		if self.type == type(val) and self.size == 0:
			self.head = QueueNode(self.startingPoint.x - circleRadius - arrowLength, self.startingPoint.y, val, None)
			self.tail = self.head
			self.size += 1
			wait()
			headerText.undraw()
		else:
			wait()
			headerText.undraw()
			raise Exception("The new value: " + str(val) + " - " + str(type(val)) + " and the type of values stored in \
				the queue " + self.name + " : " + str(self.type) + " are not the same")

	def front(self):
		#return the element at the front of the queue, if queue is empty then raise an error
		headerText.setText("Access the element at the beginning of the queue " + self.name)
		drawHeader()
		if self.size == 0:
			wait()
			headerText.undraw()
			raise Exception("You are trying to access the front element of the empty queue " + self.name )
		else:
			self.tail.changeColor("blue")
			wait()
			self.tail.changeColor("light green")
			headerText.undraw()
			return self.tail.data

	def back(self):
		#return the element at the end of the queue, if queue is empty then raise an error
		headerText.setText("Access the element at the end of the queue " + self.name)
		drawHeader()
		if self.size == 0:
			wait()
			headerText.undraw()
			raise Exception("You are trying to access the last element of the empty queue " + self.name )
		else:
			self.head.changeColor("blue")
			wait()
			self.head.changeColor("light green")
			headerText.undraw()
			return self.head.data

	def popFront(self):
		#pop the element at the front of the queue, if queue is empty, then raise an error:
		headerText.setText("Pop the element at the front of the queue " + self.name)
		drawHeader()
		if self.size == 0:
			wait()
			headerText.undraw()
			raise Exception("You are trying to pop the front element of the empty queue " + self.name)
		else:
			self.tail.changeColor("light blue")
			wait()
			current = self.head
			while current != self.tail:
				current.shiftAhead()
				prev = current
				current = current.next
			ans = self.tail.data
			self.tail.delete()
			wait()
			headerText.undraw()
			self.size -= 1
			if (self.size == 0):
				self.head = self.tail = None
			else:
				self.tail = prev
			return ans

	def popBack(self):
		#pop the element at the back of the queue, if the queue is empty, then raise an error:
		headerText.setText("Pop the element at the back of the queue " + self.name)
		drawHeader()
		if self.size == 0:
			wait()
			headerText.undraw()
			raise Exception("You are trying to pop the front element of the empty queue " + self.name)
		else:
			self.head.changeColor("light blue")
			wait()
			temp = self.head
			self.head = self.head.next
			ans = temp.data
			temp.delete()
			self.size -= 1
			if self.size == 0:
				self.head = self.tail = None
			wait()
			headerText.undraw()
			return ans