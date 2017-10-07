from rply.token import *
#from headersForDataStructures import SinglyLinkedList, Queue, Stack, BinarySearchTree
from dataStructures import *
from executionStack import ExecutionStack, VisualArray

array_dict={}
exec_stack =ExecutionStack()
list_variable_dict = []
mainIndex = -1

def variableLookup(name, index):
	while index >= 0:
		if name in list_variable_dict[index]:
			return index
		index = index - 1
	raise Exception("Variable " + name + " not in scope")

class Number():
	def __init__(self, value):
		self.value = value

	def eval(self):
		return self.value

class PrimitiveDT():
	def __init__(self, value):
		self.value = value

	def eval(self):
		return self.value

	def update(self, val):
		self.value = val

class ArrayVariable():
	def __init__(self, name, index):
		self.name = name
		self.index = index

	def eval(self):
		return list_variable_dict[variableLookup(self.name, mainIndex)][self.name].get(self.index.eval()).eval()

	def update(self, value):
		list_variable_dict[variableLookup(self.name, mainIndex)][self.name].update(self.index.eval(), value.eval())

class Variable():
	def __init__(self,name):
		self.name=name

	def eval(self):
		return list_variable_dict[variableLookup(self.name, mainIndex)][self.name].eval()

	def update(self,obj2):
		i=variableLookup(self.name, mainIndex)
		y = obj2.eval()
		list_variable_dict[i][self.name].update(y)
		exec_stack.modifyData(self.name,y,len(list_variable_dict)-i-1)
#################################################################
class Assignment():
	def __init__(self,left,right):
		self.left=left
		self.right=right

	def exec(self):
		self.left.update(self.right)

class PrimitiveDeclaration():
	def __init__(self, varName, varType, varValue):
		self.varType=varType
		self.varValue=varValue
		self.varName = varName

	def exec(self):
		if self.varName in list_variable_dict[mainIndex]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.varValue.eval()
		list_variable_dict[mainIndex][self.varName] = self.varType(x)
		exec_stack.addData(self.varName,x)

class ArrayDeclaration():
	def __init__(self, varName, varType, length, varValue):
		self.varType = varType
		self.length = length
		self.varValue = varValue
		self.varName = varName

	def exec(self):
		if self.varName in list_variable_dict[mainIndex]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.length.eval()
		array_dict[self.varName]=VisualArray(x,self.varName)
		list_variable_dict[mainIndex][self.varName] = Array(self.varType(self.varValue.eval()), x,self.varName)

modelTypeDict = {'int':10, 'float':0.2, 'string':"as", 'bool':True}

class DataStructureDeclaration():
	def __init__(self,className,name,vartype):
		self.name=name
		self.vartype=vartype
		self.theClass=className

	def exec(self):
		if self.name in list_variable_dict[mainIndex]:
			raise Exception("varialble" +self.name + "already declared")
		else:
			list_variable_dict[mainIndex][self.name]=self.theClass(1000, 100, modelTypeDict[self.vartype], self.name)

class Array(): #variable class of array
	def __init__(self, initClass, length,name):
		self.name=name
		self.array = []
		for i in range(length):
			self.array.append(initClass.__class__(initClass.eval()))
		self.length = length

	def get(self, i):
		array_dict[self.name].probe(i)
		return self.array[i]

	def update(self, i, value):
		array_dict[self.name].update(i,value)
		self.array[i].update(value)

class Block():
	def __init__(self, listExecutables):
		self.listExecutables = listExecutables

	def exec(self):
		global mainIndex, list_variable_dict
		mainIndex = mainIndex + 1
		list_variable_dict.append({})
		exec_stack.push({})
		for executable in self.listExecutables:
			# if type(executable) is list:
			#     if executable[0] == 'FOR':
			#         executable[1].exec()
			#         while(executable[1].eval()):
			#             for item in executable[2]:
			#                 item.exec()
			#             executable[3].eval()
			executable.exec()
		mainIndex = mainIndex - 1
		list_variable_dict.pop()
		exec_stack.pop()

class ForLoop():
	def __init__(self, declare, express, assign, statementList):
		self.declare = declare
		self.express = express
		self.assign = assign
		self.statementList = statementList

	def exec(self):
		for declareStatement in self.declare:
			declareStatement.exec()
		while self.express.eval():
			self.statementList.exec()
			self.assign.exec()
		for declareStatement in self.declare:
			exec_stack.deleteData(declareStatement.varName,len(list_variable_dict)-variableLookup(declareStatement.varName,mainIndex)-1)
			del list_variable_dict[mainIndex][declareStatement.varName]

class WhileLoop():
	def __init__(self, express, statementList):
		self.express = express
		self.statementList = statementList

	def exec(self):
		while self.express.eval():
			self.statementList.exec()

class IfStatement():
	def __init__(self, listofConditionals):
		self.listofConditionals = listofConditionals

	def exec(self):
		for pair in self.listofConditionals:
			if pair[0].eval():
				pair[1].exec()
				break

class CoutStatement():
	def __init__(self, listOfExpress):
		self.listOfExpress = listOfExpress

	def exec(self):
		for expresses in self.listOfExpress:
			print(expresses.eval(), end='')
#########################################################
class Int(PrimitiveDT):
	def __init__(self, value=0):
		self.value = value
	def giveType():
		return int

class Float(PrimitiveDT):
	def __init__(self, value=0.0):
		self.value = value
	def giveType():
		return float

class String(PrimitiveDT):
	def __init__(self, value='""'):
		self.value = value[1:-1]
	def giveType():
		return str

class Bool(PrimitiveDT):
	def __init__(self, value=False):
		self.value = value
	def giveType():
		return bool
######################################################
class BinaryOp():
	def __init__(self, operator, left, right):
		self.operator = operator
		self.left = left
		self.right = right

	def eval(self):
		return self.operator(self.left.eval(), self.right.eval())

	def getOperator(self):
		return self.operator

def myAdd(x, y):
	return x + y

def mySub(x, y):
	return x - y

def myMult(x, y):
	return x*y

def myDiv(x, y):
	return x/y

def myMod(x, y):
	return x%y

def myOr(x, y):
	return x or y

def myAnd(x, y):
	return x and y

def myLessThan(x, y):
	return x < y

def myLessThanEqualTo(x, y):
	return x <= y

def myGreaterThan(x, y):
	return x > y

def myGreaterThanEqualTo(x, y):
	return x >= y

def myIsEqual(x, y):
	return x == y

def myIsNotEqual(x, y):
	return x != y

###############################################################

class UnaryOp():
	def __init__(self, operator, operand):
		self.operator = operator
		self.operand = operand

	def eval(self):
		return self.operator(self.operand.eval())

	def getOperator(self):
		return self.operator

def myPlus(x):
	return x

def myMinus(x):
	return -x

def myNot(x):
	return not x

#for expressions
class Expression():
	def __init__(self):
		#constructor makes blank list
		self.elements = []

	def addElement(self, element):
		#to add a class to the element
		self.elements.append(element)

	def eval(self):
		#to evaluate, check if there is one or more simplex...if more, call eval of binary operator with args as left 
		#and right operands
		if len(self.elements) == 1:
			return self.elements[0].eval()
		elif len(self.elements) == 3:
			return self.elements[1].eval(self.elements[0].eval(), self.elements[2].eval())
		else:
			print("error")

# for simple expressions
class Simplex():
	#constructor just makes blank list
	def __init__(self):
		self.elements = []

	#to add a class to the list of classes
	def addElement(self, element):
		self.elements.append(element)

	#to evaluate, check if there is a minus at beginning or not, and if there is one or more terms after that
	def eval(self):
		if self.elements[0].__class__ == UnaryOp:
			if len(self.elements) == 2:
				return self.elements[0].eval(self.elements[1].eval())
			elif len(self.elements) == 4:
				return self.elements[0].eval(self.elements[2].eval(self.elements[1], self.elements[3]))
			else:
				print("error")
		else:
			if len(self.elements) == 1:
				return self.elements[0].eval()
			elif len(self.elements) == 3:
				return self.elements[1].eval(self.elements[0], self.elements[2])
			else:
				print("error")

class Term():
	def __init__(self):
		self.elements = []

	def addElement(self, element):
		self.elements.append(element)

	def eval(self):
		#same as Expression
		if len(self.elements) == 1:
			return self.elements[0].eval()
		elif len(self.elements) == 3:
			return self.elements[1].eval(self.elements[0].eval(), self.elements[2].eval())
		else:
			print("error")

class Factor():
	def __init__(self):
		self.elements = []

	def addElement(self, element):
		self.elements.append(element)

	def eval(self):
		if self.elements[0].__class__ == UnaryOp and len(self.elements) == 2:
			return self.elements[0].eval(self.elements[1])
		elif len(self.elements) == 1:
			return self.elements[0].eval()
		else:
			print("error")

class Member_function():
	def __init__(self,reqData):
		self.name = reqData[0]
		self.functname = reqData[1]

	def exec(self):
		getattr(list_variable_dict[variableLookup(self.name,mainIndex)][self.name], self.functname)()

class Multiple_member_function():
	def __init__(self,reqData):
		self.name=reqData[0]
		self.functname=reqData[1]
		self.arguements=reqData[2]

	def exec(self):
		getattr(list_variable_dict[variableLookup(self.name,mainIndex)][self.name], self.functname)(*map(lambda x: x.eval(),self.arguements))

