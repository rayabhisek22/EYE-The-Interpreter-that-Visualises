from rply.token import *
import sys
#from headersForDataStructures import SinglyLinkedList, Queue, Stack, BinarySearchTree
from dataStructures import *
from executionStack import ExecutionStack, VisualArray

funcDict = {}
array_dict={}
exec_stack = ExecutionStack()
list_variable_dict = [[{}]]
funcIndex = 0
mainIndex = -1
input_list = []
#Looks for the variable in dictionary

stacky=650
stackx=1210
numberofstacks=0
queuex=1150
queuey=300
numberofqueues=0
stackwidth=70
queueheight=40
linkedlistheight=40
linkedlistx=1150
linkedlisty=150
numberoflinkedlist=0
treex=1100
treey=80


def variableLookup(name):
	#high possiblity of a bug roaming around here
	for i in range(len(list_variable_dict[funcIndex]) - 1, -1 , -1):
		if name in list_variable_dict[funcIndex][i]:
			return list_variable_dict[funcIndex][i][name]
	if name in list_variable_dict[0][0]:
		return list_variable_dict[0][0][name]
	raise Exception("variable "+ name + " not found")
# Creates classes for basic data types which can be evaluated and updated(mainly for arrays)
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
		return variableLookup(self.name).get(self.index.eval()).eval()

	def update(self, value):
		variableLookup(self.name).update(self.index.eval(), value.eval())

class Variable():
	def __init__(self,name):
		self.name=name

	def eval(self):
		return variableLookup(self.name).eval()

	def update(self,obj2):
		y = obj2.eval()
		var = variableLookup(self.name)
		var.update(y)
		#exec_stack.modifyData(self.name,y,len(list_variable_dict[funcIndex])-i-1)
#################################################################

#the executable class for assignment which contains the variable and the expression
class Assignment():
	def __init__(self,left,right):
		self.left=left
		self.right=right

	def exec(self):
		self.left.update(self.right)
		return None
#the  executable declaration for basic variables 
class PrimitiveDeclaration():
	def __init__(self, varName, varType, varValue):
		self.varType=varType
		self.varValue=varValue
		self.varName = varName

	def exec(self):
		if self.varName in list_variable_dict[funcIndex][-1]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.varValue.eval()
		currFunc = list_variable_dict[funcIndex]
		currFunc[-1][self.varName] = self.varType(x)
		exec_stack.addData(self.varName,x,funcIndex)
		return None

#the executable array declarartion containing parameters like length and name
class ArrayDeclaration():
	def __init__(self, varName, varType, length, varValue):
		self.varType = varType
		self.length = length
		self.varValue = varValue
		self.varName = varName

	def exec(self):
		if self.varName in list_variable_dict[funcIndex][-1]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.length.eval()
		array_dict[self.varName]=VisualArray(x,self.varName)
		exec_stack.addData(self.varName,"Array", funcIndex)
		list_variable_dict[funcIndex][-1][self.varName] = Array(self.varType(self.varValue.eval()), x,self.varName)
		return None

modelTypeDict = {'int':10, 'float':0.2, 'string':"as", 'bool':True}

#function declarations class
class FuncDeclaration():
	def __init__(self, funcName, funcParameters, executableBlock):
		#funcName : name of function
		#funcParameters : list of tuples containing name followed by type(class) ex. [('count', Int())]
		#executableBlock : the block of the function
		self.name = funcName
		self.parameters = funcParameters
		self.executable = executableBlock

	def exec(self):
		if self.name in funcDict:
			raise Exception("Function " + self.name + " already declared")
		funcDict[self.name] = FunctionClass(self.parameters, self.executable)
		return None

class FunctionClass():
	def __init__ (self, parameters,executable):
		self.parameters = parameters
		self.executable = executable

	def exec(self,arguements):
		global funcIndex
		val = []
		for i in range(len(self.parameters)):
			val.append(arguements[i].eval())
		funcIndex = funcIndex + 1
		list_variable_dict.append([{}])
		for i in range(len(self.parameters)):  #high probability of presence of a bug here.....
			PrimitiveDeclaration(self.parameters[i][0], self.parameters[i][1], Unknown_type(val[i])).exec()

		l=len(arguements)
		if l!=len(self.parameters):
			raise Exception("wrong number of parameters given to the function: expected " + str(l) + " given "+ str(len(self.parameters)))
		"""for i in range(l):
			if arguements[i].__name__ != self.parameters.__name__:
				raise Exception("expected " + self.parameters.__name__ + "object, given " + arguements[i].__name__)"""
		temp = self.executable.exec()
		funcIndex = funcIndex - 1
		list_variable_dict.pop()
		return temp
		
class FunctionCall():
	def __init__(self,name,values):
		self.name=name
		self.value=values

	def exec(self):
		makeFunctionFrame()
		return funcDict[self.name].exec(self.value)

	def eval(self):
		return self.exec()

#initialization for our data structures
class DataStructureDeclaration():
	def __init__(self,className,name,vartype):
		self.name=name
		self.vartype=vartype
		self.theClass=className

	def exec(self):
		global numberoflinkedlist
		global numberofstacks
		global numberofqueues
		if self.name in list_variable_dict[funcIndex][-1]:
			raise Exception("varialble" +self.name + "already declared")
		else:
			if self.theClass==Stack:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(stackx-numberofstacks*stackwidth,\
				 stacky, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"Stack", funcIndex)
				numberofstacks=numberofstacks+1
			elif self.theClass==Queue:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(queuex,\
				 queuey+numberofqueues*queueheight, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"Queue", funcIndex)
				numberofqueues=numberofqueues+1
			elif self.theClass==SinglyLinkedList:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(linkedlistx,\
				 linkedlisty+numberoflinkedlist*linkedlistheight, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"LinkedList", funcIndex)
				numberoflinkedlist=numberoflinkedlist+1
			elif self.theClass==BinarySearchTree:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(treex,\
				 treey, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"BST", funcIndex)
		return None


class Array(): #variable class of array which can be probed and updated
	def __init__(self, initClass, length,name):
		self.name=name
		self.array = []
		for i in range(length):
			self.array.append(initClass.__class__(initClass.eval()))
		self.length = length

	def get(self, i):
		if i >= self.length:
			raise Exception("You are trying to accesss index " + str(i) + " of array " + str(self.name)\
				+ " which is of length " + str(self.length))
		array_dict[self.name].probe(i)
		return self.array[i]

	def update(self, i, value):
		array_dict[self.name].update(i,value)
		self.array[i].update(value)

#the basic block containing list of executable statements that can be run
class Block():
	def __init__(self, listExecutables):
		self.listExecutables = listExecutables

	def exec(self):
		global mainIndex, list_variable_dict
		mainIndex = mainIndex + 1
		list_variable_dict[funcIndex].append({})
		exec_stack.push({})
		returnType = None
		for executable in self.listExecutables:
			# if type(executable) is list:
			#     if executable[0] == 'FOR':
			#         executable[1].exec()
			#         while(executable[1].eval()):
			#             for item in executable[2]:
			#                 item.exec()
			#             executable[3].eval()
			temp = executable.exec()
			if (temp != None):
				mainIndex = mainIndex - 1
				list_variable_dict[funcIndex].pop()
				exec_stack.pop()
				return temp
		mainIndex = mainIndex - 1
		list_variable_dict[funcIndex].pop()
		exec_stack.pop()

#the class for for-loop containing declaration,conditions,block and updation
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
			temp = self.statementList.exec()
			if (temp != None):
				for declareStatement in self.declare:
					#variable lookup doesn't returns index anymore
					#exec_stack.deleteData(declareStatement.varName,len(list_variable_dict[funcIndex])-variableLookup(declareStatement.varName,mainIndex)-1)
					del list_variable_dict[funcIndex][-1][declareStatement.varName]
				return temp
			self.assign.exec()
		for declareStatement in self.declare:
			#variable lookup doesn't returns index anymore
			#exec_stack.deleteData(declareStatement.varName,len(list_variable_dict[funcIndex])-variableLookup(declareStatement.varName,mainIndex)-1)
			del list_variable_dict[funcIndex][-1][declareStatement.varName]
		return None

#similar to for-loop having required arguements
class WhileLoop():
	def __init__(self, express, statementList):
		self.express = express
		self.statementList = statementList

	def exec(self):
		while self.express.eval():
			temp = self.statementList.exec()
			if (temp != None):
				return temp
		return None

#class representing control flow which executes first statement whose condition is found true
class IfStatement():
	def __init__(self, listofConditionals):
		self.listofConditionals = listofConditionals

	def exec(self):
		for pair in self.listofConditionals:
			if pair[0].eval():
				return pair[1].exec()
		return None

#class for cout statement
class CoutStatement():
	def __init__(self, listOfExpress):
		self.listOfExpress = listOfExpress

	def exec(self):
		for expresses in self.listOfExpress:
			print(expresses.eval(), end='')

#class for cout statement
class CinStatement():
	def __init__(self, listOfVars):
		self.listOfVars = listOfVars

	def exec(self):
		global input_list
		for var in self.listOfVars:
			if input_list:
				var.update(PrimitiveDT(input_list[0]))
				input_list = input_list[1:]
			else:
				temp = input()
				input_list = temp.split()
				var.update(PrimitiveDT(input_list[0]))
				input_list = input_list[1:]
		
#########################################################
#class for basic datatypes
class Int(PrimitiveDT):
	def __init__(self, value=0):
		self.value = value
	def giveType(self):
		return int
	def update(self, val):
		self.value = int(val)

class Float(PrimitiveDT):
	def __init__(self, value=0.0):
		self.value = value
	def giveType(self):
		return float
	def update(self, val):
		self.value = float(val)

class String(PrimitiveDT):
	def __init__(self, value='""'):
		self.value = value[1:-1]
	def giveType(self):
		return str
	def update(self, val):
		self.value = str(val)

class Bool(PrimitiveDT):
	def __init__(self, value=False):
		self.value = value
	def giveType(self):
		return bool
	def update(self, val):
		self.value = bool(val)
######################################################
#class for binary operator containg operands and the relevant function
class BinaryOp():
	def __init__(self, operator, left, right):
		self.operator = operator
		self.left = left
		self.right = right

	def eval(self):
		return self.operator(self.left.eval(), self.right.eval())

	def exec(self):
		return self.eval()

	def getOperator(self):
		return self.operator
#functions for binary-ops
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
#class for unary op with function and operand
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

class Return():
	def __init__(self,exp=String()):
		self.exp =exp

	def exec(self):
		return self.exp.eval()


class Member_function():
	def __init__(self,reqData):
		self.name = reqData[0]
		self.functname = reqData[1]

	def eval(self):
		return getattr(variableLookup(self.name), self.functname)()

	def exec(self):
		self.eval()

class Multiple_member_function():
	def __init__(self,reqData):
		self.name=reqData[0]
		self.functname=reqData[1]
		self.arguements=reqData[2]

	def eval(self):
		return getattr(variableLookup(self.name), self.functname)(*map(lambda x: x.eval(),self.arguements))

	def exec(self):
		self.eval()

class Unknown_type():
	def __init__(self,value):
		self.value=value

	def eval(self):
		return self.value