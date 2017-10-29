##@file
#This file contains the definition of Queue and its data members and methods.

from .headersForDataStructures import *
#######################################################################################################################
# 															QUEUE

numberofqueues=[0]

##Class which contains all the graphics and data needed by a node in the queue
class QueueNode:
	##Constructor for the class
	#
	#@param x - the x coordinate of the bottom left corner of the node
	#@param y - the y coordinate of the bottom left corner of the node
	#@param val - the value to be stored in the node
	#@param nxt - the node that comes after this in the queue
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

	##Function to change the background color of the node
	#
	#@param color - the color to which the node has to be changed
	def changeColor(self, color):
		self.circle.undraw()
		self.circle.setFill(color)
		self.text.undraw()
		self.circle.draw(canvas)
		self.text.draw(canvas)

	##Function to shift the node ahead in the queue
	def shiftAhead(self):
		self.circle.move(arrowLength + 2*circleRadius, 0)
		self.text.move(arrowLength + 2*circleRadius, 0)
		self.arrow.shiftInQueue()

	##Function to shift the node behind in the queue
	def shiftBehind(self):
		self.circle.move(-(arrowLength + 2*circleRadius), 0)
		self.text.move(-(arrowLength + 2*circleRadius), 0)
		self.arrow.shiftBehindInQueue()

	##Function to undraw the node and then delete its contents
	def delete(self):
		self.circle.undraw()
		self.text.undraw()
		self.arrow.undraw()
		del self

##@brief Pre-defined data structure to represent a Double sided queue
#
#Contians all the data members and member functions to represent a standard singly linked list Abstract Data Type
#In addition to this, it contains all the needed data members and functions to represent the data structure on the canvas.
#Usual functions have been modified to allow for the required changes to the graph as well.
class Queue:
	#stack...to check and raise errors at appropriate times

	##Constructor for the class
	#
	#@param x - the x coordinate of the rightmost corner of the queue.
	#@param y - the y coordinate of the rightmost corner of the queue.
	#@param modelType - An object of the type to be stored in the queue, to ensure that all elements in the list are of the same type
	#as in C++
	#@param name - The name given by the user to an instance of this class.
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
		self.startingPoint = graphics.Point(x, y)
		self.nameText = graphics.Text(graphics.Point(self.startingPoint.x + 65, self.startingPoint.y\
			), name)
		self.nameText.draw(canvas)
		self.name = name
		self.type = type(modelType)
		self.head = None
		self.tail = None
		self.size = 0
		self.text = graphics.Text(graphics.Point(self.startingPoint.x + 25, self.startingPoint.y), "QUEUE")
		self.text.setSize(10)
		self.text.draw(canvas)

	##Function which returns true if the queue is empty and false otherwise
	def empty(self):
		return self.size == 0

	##Function which returns the size of the queue
	def size(self):
		return self.size

	##Function which pushes a new node to the end of the queue
	#
	#@param val - the value to be stored in the node that is to be pushed.
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

	##Function to push a node to the front of the queue
	#
	#@param val - the value to be stored in the node that is to be pushed.
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

	##Function to return the element that is at the front of the queue. It raises an error if the queue is empty.
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

	##Function to return the element at the back of the queue. It raises an error if the queue is empty.
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

	##Function to pop the element at the front of the queue. If queue is empty, then raise an error:
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

	##Function to pop the element at the back of the queue. If the queue is empty, then raise an error:
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

	##Function to undraw all the graphics related to the queue and then delete all the data members.
	def delete(self):
		global numberofqueues
		numberofqueues[0]-=1
		temp = self.head
		while temp:
			self.head = temp.next
			temp.delete()
			temp = self.head
		self.text.undraw()
		self.nameText.undraw()
		del self
		