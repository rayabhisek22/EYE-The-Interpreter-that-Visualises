from graphics import *
def main():
	win = GraphWin("My Circle", 1000, 700)
	#c = Circle(Point(50,50), 10)
	#c.draw(win)
	def stack(x, y):
		r = [Rectangle(Point(100,100), Point(400,400)), Rectangle(Point(100,200), Point(400,400)), Rectangle(Point(100,300), Point(400,400))]
		#r.setFill("Red")
		r[0].setFill("Red")
		r[1].setFill("Blue")
		r[2].setFill("#ffffff")
		for i in range(len(r)):
			r[i].draw(win)

		t = Text(Point(250,150), "This is the current activation frame")
		t.setSize(19)
		t.draw(win)

		ta = Text(Point(250,250), "The Previous Function")
		ta.setSize(19)
		ta.draw(win)

		tb = Text(Point(250,350), "The Main Function")
		tb.setSize(19)
		tb.draw(win)
		win.getMouse() # pause for click in window
		r[0].undraw()
		t.move(0,100)
		win.getMouse() # pause for click in window
		r[1].undraw()
		t.move(0,100)
		win.getMouse() # pause for click in window
		r[2].undraw()
		t.undraw()
		win.getMouse()

	def binTree(a, b):
		lineList = []
		def makeNode(alpha, level, dir = "left"):
			x = alpha[0]
			y=alpha[1]
			if dir == "left":
				lineList.append((Point(x,y), Point(x-int(100/level),y+50)))
				return (x-int(100/level),y+50)
			else:
				lineList.append((Point(x,y), Point(x+int(100/level),y+50)))
				return (x+int(100/level), y+50)
		c=[(a,b)]*10
		c[1] = makeNode(c[0],1, "left")
		c[2] = makeNode(c[0],1,"right")
		c[3] = makeNode(c[1], 2, "left")
		c[4] = makeNode(c[1], 2, "right")
		c[5] = makeNode(c[2], 2, "left")
		c[6] = makeNode(c[2], 2, "right")
		c[7] = makeNode(c[3], 3, "right")
		c[8] = makeNode(c[4], 3, "left")
		c[9] = makeNode(c[5], 3, "right")
		radius = 15
		circle = []

		for i in range(len(lineList)):
			lineList[i] = Line(lineList[i][0], lineList[i][1])
			lineList[i].draw(win)
		for i in range(len(c)):
			circle.append(Circle(Point(c[i][0], c[i][1]), radius))
			circle[-1].draw(win)
			circle[-1].setFill("Green")
			Text(Point(c[i][0], c[i][1]), str(i)).draw(win)
	binTree(750,150)
	t1 = Text(Point(250,430), "The Execution stack")
	t1.setSize(25)
	t1.draw(win)
	t1.setStyle("bold")
	t2 = Text(Point(750,400), "binaryTree<int> bt")
	t2.setSize(20)
	t2.draw(win)
	t2.setStyle("bold")
	stack(250, 50)
	win.close()

main()
