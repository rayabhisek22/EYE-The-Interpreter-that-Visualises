from headersForDataStructures import *
##################################################################################################################

numberoflinkedlist=[0]

##@brief Class which denotes a single node of a singly linked list
#
# Contains all the data members required to store the value in each node, the node that comes after it in the list and 
# all the graphical elements needed to represent each node, along with the required functions.
class SinglyLinkedListNode:
	#data and next is stored
	##The constructor for a node
	#
	#@param val - the values to be stored in the node
	#@param nxt - the node that will come after it in the list
	#@param x1 - the x coordinate of where the node is to be drawn on the graph
	#@param y1 - the y coordinate of where the node is to be drawn on the graph
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

	##Update the value that is stored in the node
	#
	#@param newVal - the new value that is to be stored in the node
	def update(self, newVal):
		if type(self.data == type(newVal)):
			self.data = newVal
			text.undraw()
			text.setText(str(newVal))
			text.draw(canvas)
		else:
			raise Exception("The new value: " + str(newVal) + " and the old value: " + str(self.data)\
			 + " are not of the same type")

	##Delete the node after undrawing all the graphical elements representing the node.
	def delete(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.arrow.undraw()
		del self

	##Change the color of the node to indicate if it is being probed, deleted or is the one we are looking for
	#
	#We change the color to light blue if it is being probed, red if it is to be deleted and dark blue if it is the one we are looking for
	#@param color - the new color to which the node is to be changed
	def changeColor(self, color):
		self.rectangle.undraw()
		self.rectangle.setFill(color)
		self.rectangle.draw(canvas)
		self.text.undraw()
		self.text.draw(canvas)

	##Change the color to light blue to indicate the node is being probed
	def probe(self):
		self.changeColor("light blue")

	##Change the color back to light green once the node has been probed
	def unprobe(self):
		self.changeColor("light green")

	##Change the color to blue to indicate that we have found the node we were looking for
	def success(self):
		self.changeColor("blue")

	##Function to shift the node ahead in the list
	def shiftAhead(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.text.anchor.x += (boxLength + arrowLength)
		self.rectangle.p1.x += (boxLength + arrowLength)
		self.rectangle.p2.x += (boxLength + arrowLength)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.shiftAhead()

	##Function to shift the node behing in the list
	def shiftBehind(self):
		self.rectangle.undraw()
		self.text.undraw()
		self.text.anchor.x -= (boxLength + arrowLength)
		self.rectangle.p1.x -= (boxLength + arrowLength)
		self.rectangle.p2.x -= (boxLength + arrowLength)
		self.rectangle.draw(canvas)
		self.text.draw(canvas)
		self.arrow.shiftBehind()


##@brief Pre-defined data structure to represent a Singly Linked List
#
#Contians all the data members and member functions to represent a standard singly linked list Abstract Data Type
#In addition to this, it contains all the needed data members and functions to represent the data structure on the canvas.
#Usual functions have been modified to allow for the required changes to the graph as well.
class SinglyLinkedList:
	#head and size is stored

	##Constructor for the class
	#
	#@param x - the x coordinate of the rightmost corner of the list.
	#@param y - the y coordinate of the rightmost corner of the list.
	#@param modelType - An object of the type to be stored in the list, to ensure that all elements in the list are of the same type
	#as in C++
	#@param name - The name given by the user to an instance of this class.
	def __init__(self, x, y, modelType, name): # modelType is an object of the type that is to be stored in the 
	#stack...to check and raise errors at appropriate times
		self.name = name
		self.type = type(modelType)
		self.head = None
		self.size = 0
		self.startingPoint = graphics.Point(x, y)
		self.baseRectangle = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x + 2*boxLength,\
		 y + boxLength))
		self.baseText = graphics.Text(graphics.Point(x + boxLength, y + boxLength/2), "TAIL")
		self.baseText.setSize(11)
		self.baseRectangle.setFill("green")
		self.baseRectangle.draw(canvas)
		self.baseText.draw(canvas)
		self.nameText = graphics.Text(graphics.Point(x + 70, y + boxLength/2), "List " + self.name)
		self.nameText.draw(canvas)
		wait()

	##Return the number of elements in the list - no graphical changes.
	def size(self):
		return self.size

	##Returns the value at the front of the list - no graphical chnages
	def top(self):
		return self.head.data

	##Push a value to the front of a list. It raises an exception is the value to be inserted is not of the correct type.
	#
	#@param val - the value to be inserted into the list
	def push(self, val):
		headerText.setText("Inserting " + str(val) + " at index 0 in the singly linked list " + self.name)
		drawHeader()
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

	##Return true if the list is empty and false otherwise - no graphical changes
	def empty(self):
		return self.size == 0

	##Change the color of the rectangle at the front of the list to indicate is being visited.
	#
	#@param color - the color to which the rectangle's background will change
	def changeBaseRectangleColor(self, color):
		self.baseRectangle.undraw()
		self.baseRectangle.setFill(color)
		self.baseRectangle.draw(canvas)
		self.baseText.undraw()
		self.baseText.draw(canvas)

	##Find and return the node that contains the value that is being searched for
	#Returns None if there is no node containg the given value
	#
	#@param val - the value of the node that we are searching for.
	def get(self, val):#returns None is not found, else returns the node.
		headerText.setText("get(" + str(val) + ") in singly linked list " + self.name)
		drawHeader()
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

	##Returns the index of at which an element is present in a list. Returns -1 if the element is not found in the list.
	#
	#@param val - the value being searched for in the list.
	def indexOf(self, val):#returns -1 if not found
		headerText.setText("indexOf(" + str(val) + ") in singly linked list " + self.name)
		drawHeader()
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

	##Searches for a given value in the list. It performs the same function as get(), but is without the graphics and is used 
	#as a helper function
	def find(self, val):
		#same as get but without the graphics
		temp = self.head
		while (temp and temp.data != val):
			temp = temp.next
		return temp

	##Erases the node that contains a particular value from the list. Does nothing is the value is not found 
	#
	#@param val - the value that is to be deleted from the list.
	def erase(self, val):
		headerText.setText("erase(" + str(val) + ") in a singly linked list " + self.name)
		wait()
		drawHeader()
		target = self.find(val)
		if target == None:
			headerText.undraw()
			headerText.setText(str(val) + " not in the singly linked list " + self.name + " => do nothing")
			drawHeader()
			wait()
			headerText.undraw()
			return
		else:
			target.changeColor("red")
			wait()
			temp = self.head
			temp2 = None
			while temp != target:
				temp.shiftAhead()
				temp2 = temp
				temp = temp.next
			if temp2:
				temp2.next = target.next
			headerText.undraw()
			self.size -= 1
			if target == self.head:
				self.head = self.head.next
			temp.delete()
			return 

	##Removes the front element of the list and raises an error if you try to pop from an empty list.
	def pop(self):
		if self.size == 0:
			raise Exception("You are trying to pop from the empty list: " + self.name)
		else:
			headerText.setText("Popping the first element of the list: " + self.name)
			wait()
			drawHeader()
			self.head.changeColor("red")
			wait()
			temp = self.head
			self.head = temp.next
			self.size -= 1
			temp.delete()		

	##Insert a given element at a given index in the list. Raises an exception if the index is out of the range or if the 
	#element to be inserted is not of the same type as the rest of the elements in the list. It increases the indices of all elements
	#following the new one by 1.
	#
	#@param index - the index at which the new node is to be inserted
	#@param val - the value to be stored in the new node.
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
		drawHeader()
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

	##Deletes the entire list if it goes out of scope. Explicitly undraws all the graphics.
	def delete(self):
		global numberoflinkedlist
		numberoflinkedlist[0]-=1
		temp = self.head
		while temp :
			self.head = temp.next
			temp.delete()
			temp = self.head
		self.nameText.undraw()
		self.baseRectangle.undraw()
		self.baseText.undraw()
		del self

		