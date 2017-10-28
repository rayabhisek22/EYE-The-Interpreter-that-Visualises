from headersForDataStructures import *

nodeSpace = 3*circleRadius
verticalGap = 3*circleRadius

##Function to calculate how far a node at a given level in a tree of a given height should be displaced from the centre
#
#@param height - height of the tree in consideration
#@param level - level at which we are insering the node in the tree
def displacementAtLevel(height, level):
	return (2**(height - level - 2))*3*circleRadius

##Class which stores all the graphical information and data related to a node in a binary tree
class BinaryTreeNode:
	##Constructor for the class
	#
	#@param lchild - the left child of the node in the tree
	#@param rchild - the right child of the node in the tree
	#@param val - the value to be stored in the node
	#@param x - the x coordinate of the centre of the node
	#@param y - the y coordinate of the centre of the node
	def __init__(self, lchild, rchild, val, x, y):
		self.left = lchild
		self.right = rchild
		self.data = val
		self.circle = graphics.Circle(graphics.Point(x, y), circleRadius)
		self.circle.setFill("light green")
		self.location = graphics.Point(x, y)
		self.text = graphics.Text(graphics.Point(x, y), str(val))
		if (self.left != None):
			self.leftLine = graphics.Line(self.location, self.left.location)
			self.leftLine.draw(canvas)
		else:
			self.leftLine = None
		if (self.right != None):
			self.rightLine = graphics.Line(self.location, self.right.location)
			self.rightLine.draw(canvas)
		else:
			self.rightLine = None
		self.circle.draw(canvas)
		self.text.draw(canvas)

	##Function to relocate the node to another point on the canvas
	#
	#@param x - the new x coordinate
	#@param y - the new y coordinate
	def relocate(self, x, y):
		dx = x - self.location.x
		dy = y - self.location.y
		self.circle.move(dx, dy)
		self.text.move(dx, dy)
		self.location.x = x
		self.location.y = y
		if self.leftLine:
			self.leftLine.undraw()
		if self.rightLine:
			self.rightLine.undraw()

	##Function to change the color of the node
	#
	#@color - the new color to be set as the background of the node
	def changeColor(self, color):
		self.circle.undraw()
		self.text.undraw()
		self.circle.setFill(color)
		self.circle.draw(canvas)
		self.text.draw(canvas)

	##Function to undraw the node and delete its contents
	def delete(self):
		if (self.leftLine):
			self.leftLine.undraw()
		if (self.rightLine):
			self.rightLine.undraw()
		self.circle.undraw()
		self.text.undraw()

	##Function to change the left child of the node along with all required graphical changes
	#
	#@param lchild - the new left child of the node
	def changeLeft(self, lchild):
		self.left = lchild
		if self.leftLine == None:
			if self.left != None:
				self.leftLine.undraw()
				del self.leftLine
				self.leftLine = None
		else:
			if self.leftLine != None:
				self.leftLine.undraw()
				del self.leftLine
			self.leftLine.p2 = self.left.location
			self.leftLine.draw()

	##Function to change the right child of the node along with all required graphical changes
	#
	#@param rchild - the new right child of the node
	def changeRight(self, rchild):
		self.right = rchild
		if self.right == None:
			if self.rightLine != None:
				self.rightLine.undraw()
				del self.rightLine
				self.rightLine = None
		else:
			if self.rightLine != None:
				self.leftLine.undraw()
				del self.rightLine
			self.rightLine.p2 = self.right.location
			self.rightLine.draw()

	##Function to change the color of a node to show that it is being probed
	def probe(self):
		self.changeColor("light blue")
		wait()
		self.changeColor("light green")

	##Function to redraw the node
	def redraw(self):
		self.circle.undraw()
		self.circle.draw(canvas)
		self.text.undraw()
		self.text.draw(canvas)

	##Function to change the color of the node and then delete it
	def delete(self):
		self.changeColor("red")
		wait()
		self.circle.undraw()
		self.text.undraw()
		if self.leftLine:
			self.leftLine.undraw()
		if self.rightLine:
			self.rightLine.undraw()
		del self


##@brief Pre-defined data structure to represent a Binary Search Tree
#
#Contians all the data members and member functions to represent a standard singly linked list Abstract Data Type
#In addition to this, it contains all the needed data members and functions to represent the data structure on the canvas.
#Usual functions have been modified to allow for the required changes to the graph as well.
class BinarySearchTree:

	##Constructor for the class
	#
	#@param x - the x coordinate of the root of the tree.
	#@param y - the y coordinate of the root of the tree.
	#@param modelType - An object of the type to be stored in the tree, to ensure that all elements in the list are of the same type
	#as in C++
	#@param name - The name given by the user to an instance of this class.
	def __init__(self, x, y, modelType, name):
		self.rootLocation = graphics.Point(x, y)
		self.type = type(modelType)
		self.name = name
		self.height = 0
		self.root = None
		self.rootText = graphics.Text(graphics.Point(x, y - 30), "ROOT")
		self.rootText.setSize(10)
		self.rootText.draw(canvas)

	##Recursive Function to search for a given value in the node and then add it if it is not present
	#
	#@param node - the node considered in this recursive call
	#@param val - the value which we want to search and add if not found
	#@param level - the level at which we have reached currently.
	def searchAdd(self, node, val, level):
		if node.data == val:
			node.probe()
			return 
		else:
			node.probe()
			if node.data < val and node.right == None:
				node.changeColor("blue")
				wait()
				if level == self.height:
					self.height += 1 
					node.right = BinaryTreeNode(None, None, val, -100, node.location.y + verticalGap)
					self.redraw()
				else:
					node.right = BinaryTreeNode(None, None, val, node.location.x + displacementAtLevel(self.height,\
						level), node.location.y + verticalGap)
					self.redraw()
			elif node.data < val and node.right != None:
				self.searchAdd(node.right, val, level + 1)
			elif node.data > val and node.left == None:
				node.changeColor("blue")
				wait()
				if level == self.height:
					self.height += 1
					node.left = BinaryTreeNode(None, None, val, -100, node.location.y + verticalGap)
					self.redraw()
				else:
					newx = node.location.x - displacementAtLevel(self.height, level)
					newy = node.location.y + verticalGap
					node.leftLine = graphics.Line(node.location, graphics.Point(newx, newy))
					node.leftLine.draw(canvas)
					node.left = BinaryTreeNode(None, None, val, newx, newy)
			elif node.data > val and node.left != None:
				self.searchAdd(node.left, val, level + 1)
			wait()
			node.changeColor("light green")

	##Function to redraw the entire binary tree once the coordinates of every node have been updated
	def redraw(self):
		if self.height != 0:
			self.relocate(self.root, self.rootLocation.x, self.rootLocation.y, 1)
			self.makeLines(self.root)
			self.overDraw(self.root)

	##Recursive function to overdraw a given node and then call the same function on both the childred
	#
	#@param node - The node which is currently to be redrawn
	def overDraw(self, node):
		if node:
			node.redraw()
			self.overDraw(node.left)
			self.overDraw(node.right)

	##Recursive function to draw all the lines linking a given node with both its children after checking that they exist
	#
	#@node - the node that we are currently considering
	def makeLines(self, node):
		if node:
			if node.left:
				node.leftLine = graphics.Line(node.location, node.left.location)
				node.leftLine.draw(canvas)
				self.makeLines(node.left)
			if node.right:
				node.rightLine = graphics.Line(node.location, node.right.location)
				node.rightLine.draw(canvas)
				self.makeLines(node.right)

	##relocates the node to the new x value and adjusts the children accordingly. deletes all lines which will be
	#made by makeLines()
	def relocate(self, node, x, y, level):
		#relocates the node to the new x value and adjusts the children accordingly. deletes all lines which will be
		#made by makeLines()
		if node != None:
			node.relocate(x, y)
			self.relocate(node.left, x - displacementAtLevel(self.height, level), y + verticalGap, level + 1)
			self.relocate(node.right, x + displacementAtLevel(self.height, level), y + verticalGap, level + 1)

	##Function to insert a new value into the binary tree, after checking whether the value is apt to add
	#
	#@param val - the new value that is to be added to the binary search tree
	def insert(self, val):
		if type(val) != self.type:
			raise Exception("The type of the values stored in the binary Tree " + self.name + " : " + str(self.type) + \
				" and the type of the value that is to be inserted are not the same")
		else:
			headerText.setText("Inserting " + str(val) + " into the binary tree " + self.name)
			drawHeader()
			if self.root == None:
				self.height = 1
				self.root = BinaryTreeNode(None, None, val, self.rootLocation.x, self.rootLocation.y)
				wait()
				headerText.undraw()
				return
			else:
				self.searchAdd(self.root, val, 1)
				wait()
				headerText.undraw()
				return

	##Recurisve helper function to find a given value in the binary search tree
	#
	#@param node - the node at which the search has currently reached
	#@param val - the value that we are searching for
	def searchHelper(self, node, val):
		if node == None:
			headerText.undraw()
			return None
		else:
			node.probe()
			if node.data == val:
				node.changeColor("blue")
				wait()
				node.changeColor("light green")
				headerText.undraw()
				return node
			if node.data > val:
				return self.searchHelper(node.left, val)
			elif node.data < val:
				return self.searchHelper(node.right, val)

	##Recursive function to find the height of the tree, used to draw the tree correctly
	#
	#@param node - the node that we are currenty considering
	def findHeight(self, node):
		if node == None:
			return 0
		else:
			return 1 + max(self.findHeight(node.left), self.findHeight(node.right))

	##Function to search for a given value in the binary search tree
	#
	#@param val - the value for which the search is being carried out
	def search(self, val):
		if type(val) != self.type:
			raise Exception("The type of value you are searching for: " + str(type(val)) + " and the type of values\
				that are stored in the binary search tree " + self.name + " : " + self.type + " are not the same")
		else:
			headerText.setText("Searching for " + str(val) + " in the binary search tree " + self.name)
			drawHeader()
			if self.height == 0:
				wait()
				headerText.undraw()
				return None
			else:
				return self.searchHelper(self.root, val)

	##Recursive helper function to find a value and delete it from the tree if it is found
	#
	#@param - the node that is currently being considered
	#@param val - the value which is being searched for and is to be deleted
	def searchDelete(self, node, val):
		if node == None:
			return
		node.probe()
		if node.data > val:
			if node.left and node.left.data == val:
				if node.left.right == None:
					temp = node.left.left
					node.left.delete()
					node.left = node.left.left
					self.height = self.findHeight(self.root)
					self.redraw()
					return
				else:
					temp = self.findLeftmost(node.left.right)
					temp.left = node.left.left
					node.left.delete()
					node.left = temp
					self.height = self.findHeight(self.root)
					self.redraw()
					return 
			else:
				self.searchDelete(node.left, val)
		elif node.data < val:
			if node.right and node.right.data == val:
				if node.right.right == None:
					temp = node.right.left
					node.right.delete()
					node.right = node.right.left
					self.height = self.findHeight(self.root)
					self.redraw()
					return
				else:
					temp = self.findLeftmost(node.right.right)
					temp.left = node.right.left
					node.right.delete()
					node.right = temp
					self.height = self.findHeight(self.root)
					self.redraw()
					return 
			else:
				self.searchDelete(node.right, val)

	##Function to find the leftmost child of a given node. A helper function for deletion
	#
	#@param node - the node whose leftmost child is to be found
	def findLeftmost(self, node):
		if node.left == None:
			return node
		else:
			return self.findLeftmost(node.left)

	##Function to erase a value from the binary tree. It raises an error if the type of the value does not match the type of values being 
	#stored in the tree. It does nothing if the value is not found in the tree
	#
	#@param val - the value being searched for that is to be deleted
	def erase(self, val):
		if type(val) != self.type:
			raise Exception("The type of value you are trying to delete: " + str(type(val)) + " and the type of values\
				that are stored in the binary search tree " + self.name + " : " + self.type + " are not the same")
		else:
			headerText.setText("Deleting the value: " + str(val) + " from the binary tree " + self.name)
			drawHeader()
			if self.height == 0:
				wait()
				headerText.undraw()
				return
			elif self.root.data == val:
				self.root.probe()
				self.root.changeColor("red")
				wait()
				if self.root.right:
					oldRoot = self.root
					temp = self.findLeftmost(self.root.right)
					temp.left = self.root.left
					self.root = self.root.right
					self.height = self.findHeight(self.root)
					oldRoot.delete()
					self.redraw()
				else:
					oldHead = self.root
					self.root = self.root.left
					self.height = self.findHeight(self.root)
					oldRoot.delete()
					self.redraw()
			else:
				self.searchDelete(self.root, val)
				headerText.undraw()
				return

	##A recursive helper function to delete the entire tree. It first deletes the children and then undraws the current node
	#
	#@param node - the current node to be delted
	def deleteHelper(self, node):
		if node!=None:
			self.deleteHelper(node.left)
			self.deleteHelper(node.right)
			node.delete()

	##Function to delete the entire tree, by first undrawing it and then deleting all the data.
	def delete(self):
		self.rootText.undraw()
		self.deleteHelper(self.root)
		del self

