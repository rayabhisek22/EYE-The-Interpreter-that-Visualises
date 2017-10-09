from headersForDataStructures import *

def drawHeader():
	try:
		headerText.draw(canvas)
	except:
		headerText.undraw()
		headerText.draw(canvas)
	

nodeSpace = 3*circleRadius
verticalGap = 3*circleRadius

def displacementAtLevel(height, level):
	return (2**(height - level - 2))*3*circleRadius

class BinaryTreeNode:
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

	def changeColor(self, color):
		self.circle.undraw()
		self.text.undraw()
		self.circle.setFill(color)
		self.circle.draw(canvas)
		self.text.draw(canvas)

	def delete(self):
		if (self.leftLine):
			self.leftLine.undraw()
		if (self.rightLine):
			self.rightLine.undraw()
		self.circle.undraw()
		self.text.undraw()

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

	def probe(self):
		self.changeColor("light blue")
		wait()
		self.changeColor("light green")

	def redraw(self):
		self.circle.undraw()
		self.circle.draw(canvas)
		self.text.undraw()
		self.text.draw(canvas)

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



class BinarySearchTree:
	def __init__(self, x, y, modelType, name):
		self.rootLocation = graphics.Point(x, y)
		self.type = type(modelType)
		self.name = name
		self.height = 0
		self.root = None
		self.rootText = graphics.Text(graphics.Point(x, y - 30), "ROOT")
		self.rootText.setSize(10)
		self.rootText.draw(canvas)

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

	def redraw(self):
		if self.height != 0:
			self.relocate(self.root, self.rootLocation.x, self.rootLocation.y, 1)
			self.makeLines(self.root)
			self.overDraw(self.root)

	def overDraw(self, node):
		if node:
			node.redraw()
			self.overDraw(node.left)
			self.overDraw(node.right)

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

	def relocate(self, node, x, y, level):
		#relocates the node to the new x value and adjusts the children accordingly. deletes all lines which will be
		#made by makeLines()
		if node != None:
			node.relocate(x, y)
			self.relocate(node.left, x - displacementAtLevel(self.height, level), y + verticalGap, level + 1)
			self.relocate(node.right, x + displacementAtLevel(self.height, level), y + verticalGap, level + 1)

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

	def findHeight(self, node):
		if node == None:
			return 0
		else:
			return 1 + max(self.findHeight(node.left), self.findHeight(node.right))

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

	def findLeftmost(self, node):
		if node.left == None:
			return node
		else:
			return self.findLeftmost(node.left)

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


# bst =BinarySearchTree(500, 100, 10, "asa")
# bst.insert(0)
# bst.insert(3)
# bst.insert(1)
# bst.insert(4)
# bst.insert(2)
