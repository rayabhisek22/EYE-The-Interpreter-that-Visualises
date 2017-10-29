# Everywhere, you have to pass arguments to decide where yu wanna define each data structure on the canvas
# and when yu delete call the delete function explicitly.

#####    					TODO:
# in the binary tree, when node is dark blue, line comes on top

#makeFunctionFrame()	
#exec_stacl->addData(varname, x, funcIndex)
#exec_stack->modifyData(varname, value, funcIndex, index (lowest is 0 and upper is length of stack))


##@file
#This file contains the code for showing the header text for every operation on data strucutres.
from . import graphics
import time


def drawHeader():
	try:
		headerText.draw(canvas)
	except:
		headerText.undraw()
		headerText.draw(canvas)

def drawCodeText():
	try:
		codeText.draw(canvas)
	except:
		codeText.undraw()
		codeText.draw(canvas)


canvas = graphics.GraphWin("My Interpreter", 1300, 700)
boxLength = 20
circleRadius = 15
arrowLength = 10
headerPoint = graphics.Point(650, 20)#point where current action will be displayed
headerText = graphics.Text(headerPoint, "")#header text
codeText = graphics.Text(graphics.Point(headerPoint.x, headerPoint.y + 25), "")
headerText.setSize(15)

##@brief Defines how much to wait before the execution of two steps
def wait():
	#define how to wait...sleep or mouse click or something else
	#canvas.getMouse()
	time.sleep(0.4)

##@brief Class contaning arrows to make a pointer between objects on the canvas
class rightArrow:
	##The constructor, with the coordinates of where to make the arrow
	def __init__(self, x, y):
		self.line = graphics.Line(graphics.Point(x,y), graphics.Point(x + arrowLength, y))
		self.arrowhead1 = graphics.Line(graphics.Point(x+arrowLength,y), graphics.Point(x + arrowLength - 5,\
		 y-4))
		self.arrowhead2 = graphics.Line(graphics.Point(x+arrowLength,y), graphics.Point(x + arrowLength - 5,\
		 y+4))

	##Function to actually draw the arrow on the canvas
	def draw(self):
		self.line.draw(canvas)
		self.arrowhead1.draw(canvas)
		self.arrowhead2.draw(canvas)

	##Function to undraw the arrow
	def undraw(self):
		self.line.undraw()
		self.arrowhead1.undraw()
		self.arrowhead2.undraw()

	##Function to shift the arrow ahead so that if the elements of a lsit are deleted, we can update the structure
	def shiftAhead(self):
		self.undraw()
		self.line.p1.x += (boxLength + arrowLength)
		self.arrowhead1.p1.x += (boxLength + arrowLength)
		self.arrowhead2.p1.x += (boxLength + arrowLength)
		self.line.p2.x += (boxLength + arrowLength)
		self.arrowhead1.p2.x += (boxLength + arrowLength)
		self.arrowhead2.p2.x += (boxLength + arrowLength)
		self.draw()

	##Function to shift the arrow behind so that if the elements of a list are deleted, we can update the structure
	def shiftBehind(self):
		self.undraw()
		self.line.p1.x -= (boxLength + arrowLength)
		self.arrowhead1.p1.x -= (boxLength + arrowLength)
		self.arrowhead2.p1.x -= (boxLength + arrowLength)
		self.line.p2.x -= (boxLength + arrowLength)
		self.arrowhead1.p2.x -= (boxLength + arrowLength)
		self.arrowhead2.p2.x -= (boxLength + arrowLength)
		self.draw()

	##Function to shift the whole arrow on the canvas by dx along the x axis and dy along the y axis
	#
	#@param dx - the amount by which the arrow is to shifted along the x axis
	#@param dy - the amount by which the arrow is to shifted along the y axis
	def shift(self, dx, dy):
		self.line.move(dx, dy)
		self.arrowhead1.move(dx, dy)
		self.arrowhead2.move(dx, dy)

	##Function to move the arrow when the queue is updated
	def shiftInQueue(self):
		self.line.move((2*circleRadius + arrowLength),0)
		self.arrowhead1.move((2*circleRadius + arrowLength),0)
		self.arrowhead2.move((2*circleRadius + arrowLength),0)	

	##Function to move the arrow behind in the queue when an element is added to the front of the queue
	def shiftBehindInQueue(self):
		self.line.move(-(2*circleRadius + arrowLength),0)
		self.arrowhead1.move(-(2*circleRadius + arrowLength),0)
		self.arrowhead2.move(-(2*circleRadius + arrowLength),0)	
