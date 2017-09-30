# Everywhere, you have to pass arguments to decide where yu wanna define each data structure on the canvas
# and when yu delete call the delete function explicitly.

#####    					TODO:
#Add names of the data structures underneath them
#Add delete function to all classes
# in the binary tree, when node is dark blue, line comes on top
# can try to make delet in the bst more efficient, it calculates height everytime yu delete anything

import graphics
import time

canvas = graphics.GraphWin("My Interpreter", 1300, 1000)
boxLength = 20
circleRadius = 15
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

	def shiftInQueue(self):
		self.line.move((2*circleRadius + arrowLength),0)
		self.arrowhead1.move((2*circleRadius + arrowLength),0)
		self.arrowhead2.move((2*circleRadius + arrowLength),0)	

	def shiftBehindInQueue(self):
		self.line.move(-(2*circleRadius + arrowLength),0)
		self.arrowhead1.move(-(2*circleRadius + arrowLength),0)
		self.arrowhead2.move(-(2*circleRadius + arrowLength),0)	
