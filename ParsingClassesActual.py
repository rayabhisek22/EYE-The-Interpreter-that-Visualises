from rply.token import *
import sys
#from headersForDataStructures import SinglyLinkedList, Queue, Stack, BinarySearchTree
from dataStructures import *
from executionStack import VisualArray, Graphics, canvas, codeText, drawCodeText

def changetext(s):
	codeText.setText(s)
	drawCodeText()
funcDict = {}
array_dict={}
exec_stack = Graphics()
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
hashx=750
hashy=80

##@brief Looks up for a variable name in the variable dictionary
#
#The variable is searched for in the scope before the current scope and finally in
#the list of global variables. An exception is raised if variable is not found
#@param name The name of the variable to be searched
#@return class: class corresponding to the variable name
def variableLookup(name):
	#high possiblity of a bug roaming around here
	for i in range(len(list_variable_dict[funcIndex]) - 1, -1 , -1):
		if name in list_variable_dict[funcIndex][i]:
			return [list_variable_dict[funcIndex][i][name],[funcIndex,i]]
	if name in list_variable_dict[0][0]:
		return [list_variable_dict[0][0][name],[0,0]]
	raise Exception("variable "+ name + " not found")
# Creates classes for basic data types which can be evaluated and updated(mainly for arrays)

##@brief The class to store a number
class Number():
	##the constructor
	#@param self the object pointer
	#@param value The value to be stored in the class
	def __init__(self, value):
		self.value = value

	## the eval function that returns the number stored
	def eval(self):
		return self.value

##@brief The basic class which stores values of basic data structures like numbers,strings and boolean
#
#Some of the operations are similar for all datatypes, which have been inherired from PrimitiveDT. basic datatypes that
#appear as it is in an expression are stored as subclass of primitiveDT. eg. x=7+x; 7 is stored as primitive DT
class PrimitiveDT():
	##The constructor which takes a value and stores it
	def __init__(self, value):
		self.value = value

	##the evaluate function which returns the value
	def eval(self):
		return self.value

	##The update function which updates the value stored
	#@param val The value to which it is to be updated
	def update(self, val):
		self.value = val


##@brief The class which stores an array as a variable
#
#It is the basic class which holds the array value and the index which has to be either updated or
#evaluated acoording to the index at which it is
class ArrayVariable():
	##The constructor which stores relevant parameters
	#@param name The name of the array variable
	#@param index The index(a class that can be evaluated) of the array
	#@param snippet The relevant code snippet
	def __init__(self, name, index, snippet):
		self.name = name
		self.index = index
		self.snippet = snippet

	##The function which gives the value at that index
	def eval(self):
		return variableLookup(self.name)[0].get(self.index.eval()).eval()

	##the function which updates the value at the stored index
	#@param value The value(class that can be evaluated) to which the upation occurs
	def update(self, value):
		variableLookup(self.name)[0].update(self.index.eval(), value.eval())


##The class which stores a variable as a class,with relevant functions like eval and update
class Variable():
	##the constructor
	#@param name The name of the variable being stored
	def __init__(self,name):
		self.name=name

	##The value of the the variable is given after looking up the dictionary
	def eval(self):
		return variableLookup(self.name)[0].eval()

	##It updates the value of the variable
	#@param obj2 The value(a class to be evaluated) to which the updation has to occur
	def update(self,obj2):
		y = obj2.eval()
		var = variableLookup(self.name)
		var[0].update(y)
		exec_stack.modifyData(self.name,y,len(list_variable_dict[funcIndex])-var[1][1]-1,var[1][0])
#################################################################

##the executable class for assignment which contains the variable and the expression
class Assignment():
	##the constructor
	#@param left The Variable class to be updated
	#@param right the expression to be evaluated
	#@param snippet The relevant code snippet
	def __init__(self,left,right, snippet):
		self.left=left
		self.right=right
		self.snippet = snippet

	##The function which actually carries out the updation
	def exec(self):
		changetext(self.snippet)
		self.left.update(self.right)
		return None
##the  executable declaration for basic variables 
class PrimitiveDeclaration():
	##The constructor
	#@param varName The name of the variable to be declared
	#@param varType The type of the variable to be initialized
	#@param varValue The value of the class to which variable is initialized
	#@param snippet The relevant snippet
	def __init__(self, varName, varType, varValue, snippet):
		self.varType=varType
		self.varValue=varValue
		self.varName = varName
		self.snippet = snippet

	##The function which actually adds the variable to the dictionary with the relevant value
	def exec(self):
		if self.varName in list_variable_dict[funcIndex][-1]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.varValue.eval()
		currFunc = list_variable_dict[funcIndex]
		currFunc[-1][self.varName] = self.varType(x)
		changetext(self.snippet)
		exec_stack.addData(self.varName,x,funcIndex)
		return None

##the executable array declarartion
class ArrayDeclaration():
	##the constructor
	#@param varName The name of the array
	#@param varType The type of the array elements
	#@param length Length of the array
	#@param varValue The value to which each element of array is to be initialized
	#@param snippet the relevant snippet
	def __init__(self, varName, varType, length, varValue, snippet):
		self.varType = varType
		self.length = length
		self.varValue = varValue
		self.varName = varName
		self.snippet = snippet

	##The function which actually executes it
	def exec(self):
		if self.varName in list_variable_dict[funcIndex][-1]:
			raise Exception("Variable "+self.varName + " already declared")
		x=self.length.eval()
		array_dict[self.varName]=VisualArray(x,self.varName)
		changetext(self.snippet)
		exec_stack.addData(self.varName,"Array",funcIndex)
		list_variable_dict[funcIndex][-1][self.varName] = Array(self.varType(self.varValue.eval()), x,self.varName)
		return None

modelTypeDict = {'int':10, 'float':0.2, 'string':"as", 'bool':True}

##function declarations class which pushes an executable function class to the dictionary
class FuncDeclaration():
	def __init__(self, funcName, funcParameters, executableBlock,snippet):
		##the constructor
		#@paramfuncName : name of function
		#@paramfuncParameters : list of tuples containing name followed by type(class) ex. [('count', Int())]
		#@paramexecutableBlock : the block of the function
		#@param snippet The relevant code snippet
		self.name = funcName
		self.parameters = funcParameters
		self.executable = executableBlock
		self.snippet = snippet

	##The exectuable which pushes FunctionClass to func_dict
	def exec(self):
		if self.name in funcDict:
			raise Exception("Function " + self.name + " already declared")
		funcDict[self.name] = FunctionClass(self.parameters, self.executable)
		return None

##The class which when given the arguments calls the functions
class FunctionClass():
	##the constructor
	#@param parameters A list of tuples containg the parameter name and type
	#@param excutable The body of the function which can be executed 
	def __init__ (self, parameters,executable):
		self.parameters = parameters
		self.executable = executable


	##The executable which on getting the list of arguments initializes the parametrs to respective values and then
	#executes the body, and returns some value on encountering return
	#@param arguemnets The list of arguments
	def exec(self,arguements,name):
		global funcIndex
		val = []
		for i in range(len(self.parameters)):
			val.append(arguements[i].eval())
		funcIndex = funcIndex + 1
		exec_stack.makeFunctionFrame(name)
		list_variable_dict.append([{}])
		for i in range(len(self.parameters)):  #high probability of presence of a bug here.....
			PrimitiveDeclaration(self.parameters[i][0], self.parameters[i][1], Unknown_type(val[i]), "	").exec()

		l=len(arguements)
		if l!=len(self.parameters):
			raise Exception("wrong number of parameters given to the function: expected " + str(l) + " given "+ str(len(self.parameters)))
		"""for i in range(l):
			if arguements[i].__name__ != self.parameters.__name__:
				raise Exception("expected " + self.parameters.__name__ + "object, given " + arguements[i].__name__)"""
		temp = self.executable.exec()
		exec_stack.deleteFunctionFrame()
		funcIndex = funcIndex - 1
		list_variable_dict.pop()
		return temp

##The class which actually calls the function		
class FunctionCall():
	##The constructor
	#@param name The name of the function
	#@param values The values to be passed to the function
	#@param The relevant code snippet
	def __init__(self,name,values, snippet):
		self.name=name
		self.value=values
		self.snippet = snippet

	##the executable
	def exec(self):
		self.eval() 

	##The function which actually calls the functionClass with list of values
	def eval(self):
		changetext("Calling the function"+self.name)
		return funcDict[self.name].exec(self.value,self.name)

##initialization for our data structures
class DataStructureDeclaration():
	##The constructor
	#@param className The name of datatype to be initialized
	#@param name The name of datatype variable
	#@param vartype The type of data which is stored in this datatype
	#@param snippet The relevant code snippet
	def __init__(self,className,name,vartype, snippet):
		self.name=name
		self.vartype=vartype
		self.theClass=className
		self.snippet = snippet

	##The executable function
	def exec(self):
		global numberoflinkedlist
		global numberofstacks
		global numberofqueues
		if self.name in list_variable_dict[funcIndex][-1]:
			raise Exception("varialble" +self.name + "already declared")
		else:
			changetext(self.snippet)
			if self.theClass==Stack:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(stackx-numberofstacks*stackwidth,\
				 stacky, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"Stack",funcIndex)
				numberofstacks=numberofstacks+1
			elif self.theClass==Queue:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(queuex,\
				 queuey+numberofqueues*queueheight, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"Queue",funcIndex)
				numberofqueues=numberofqueues+1
			elif self.theClass==SinglyLinkedList or self.theClass==DoublyLinkedList:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(linkedlistx,\
				 linkedlisty+numberoflinkedlist*linkedlistheight, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"LinkedList",funcIndex)
				numberoflinkedlist=numberoflinkedlist+1
			elif self.theClass==BinarySearchTree:
				list_variable_dict[funcIndex][-1][self.name]=self.theClass(treex,\
				 treey, modelTypeDict[self.vartype], self.name)
				exec_stack.addData(self.name,"BST",funcIndex)
		return None

class HashDeclaration():
	def __init__(self,className,name,vartype,exp,snippet):
		self.name=name
		self.vartype=vartype
		self.theClass=className
		self.exp=exp
		self.snippet=snippet

	def exec(self):
		changetext(self.snippet)
		list_variable_dict[funcIndex][-1][self.name]=self.theClass(self.exp.eval(),hashx,\
		 hashy, modelTypeDict[self.vartype], self.name)
		exec_stack.addData(self.name,"HashTable",funcIndex)


##variable class of array which can be probed and updated
class Array(): 
	##the constructor
	#@param initClass The type of variable in array
	#@param length The length of array
	#@param name Name of array
	def __init__(self, initClass, length,name):
		self.name=name
		self.array = []
		for i in range(length):
			self.array.append(initClass.__class__(initClass.eval()))
		self.length = length


	##Gives the value of a variable at a particular index
	#@param i The index
	def get(self, i):
		if i >= self.length:
			raise Exception("You are trying to accesss index " + str(i) + " of array " + str(self.name)\
				+ " which is of length " + str(self.length))
		array_dict[self.name].probe(i)
		return self.array[i]
	##Updates the value at a particular index
	#@param i the index to be updated
	#@param value the updated value
	def update(self, i, value):
		array_dict[self.name].update(i,value)
		self.array[i].update(value)

##the basic block containing list of executable statements that can be run
class Block():
	##the constructor
	#@param the list of executable statement
	def __init__(self, listExecutables):
		self.listExecutables = listExecutables


	##the executable which exectutes all statement in a list until a return statement is encountered,
	#on which that value is returned
	def exec(self):
		global mainIndex, list_variable_dict
		mainIndex = mainIndex + 1
		list_variable_dict[funcIndex].append({})
		exec_stack.push({},funcIndex)
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
				exec_stack.pop(funcIndex)
				return temp
		mainIndex = mainIndex - 1
		list_variable_dict[funcIndex].pop()
		exec_stack.pop(funcIndex)

##the class for for-loop containing declaration,conditions,block and updation
class ForLoop():
	##the constructor
	#@param declare the list of declaration statements
	#@param express The condition to be checked
	#@param assign The updation statement
	#@param statementList The body of the for loop
	#@param snippet The relevant code snippet 
	def __init__(self, declare, express, assign, statementList, snippet):
		self.declare = declare
		self.express = express
		self.assign = assign
		self.statementList = statementList
		self.snippet = snippet


	##The executable which implements the ForLoop in correct order
	def exec(self):
		changetext("Starting a for loop")
		for declareStatement in self.declare:
			declareStatement.exec()
		while self.express.eval():
			temp = self.statementList.exec()
			if (temp != None):
				for declareStatement in self.declare:
					#variable lookup doesn't returns index anymore
					#exec_stack.deleteData(declareStatement.varName,len(list_variable_dict[funcIndex])-variableLookup(declareStatement.varName,mainIndex)-1)
					try:
						del list_variable_dict[funcIndex][-1][declareStatement.varName]
					except:
						pass
				return temp
			self.assign.exec()
		for declareStatement in self.declare:
			v=variableLookup(declareStatement.varName)
			#variable lookup doesn't returns index anymore
			exec_stack.deleteData(declareStatement.varName,len(list_variable_dict[funcIndex])-v[1][1]-1,v[1][0])
			try:
				del list_variable_dict[funcIndex][-1][declareStatement.varName]
			except:
				pass
		return None

##similar to for-loop having required arguements
class WhileLoop():
	##the constructor
	#@param express The condition to be checked
	#@param statementList The body of the for loop
	#@param snippet The relevant code snippet 
	def __init__(self, express, statementList, snippet):
		self.express = express
		self.statementList = statementList
		self.snippet = snippet


	##the ecutable implementing While-loop
	def exec(self):
		changetext("Starting a while loop")
		while self.express.eval():
			temp = self.statementList.exec()
			if (temp != None):
				return temp
		return None

##class representing control flow which executes first statement whose condition is found true
class IfStatement():
	##the constructor
	#@param listofConditionals List of tuples containing the condition and the statemnetList to be implemented if it is true
	def __init__(self, listofConditionals):
		self.listofConditionals = listofConditionals

	##The executable which runs until it finds the first true condtion, following which that block is executed
	def exec(self):
		snipp="If statement being executed"
		changetext(snipp)
		for pair in self.listofConditionals:
			if pair[0].eval():
				return pair[1].exec()
		return None

##class for cout statement
class CoutStatement():
	##the constructor
	#@param listOfExpress The expressions that have to be printed
	#@param snippet The relevant code snippet
	def __init__(self, listOfExpress, snippet):
		self.listOfExpress = listOfExpress
		self.snippet = snippet

	##The executable which prints the evaluated expressions
	def exec(self):
		changetext("cout statement being executed")
		changetext(self.snippet)
		for expresses in self.listOfExpress:
			print(expresses.eval(), end='')

##class for cin statement
class CinStatement():
	##the constructor
	#@param listOfVars The variables that have to be taken for input
	#@param snippet The relevant code snippet
	def __init__(self, listOfVars, snippet):
		self.listOfVars = listOfVars
		self.snippet = snippet

	##the executable that takes the input
	def exec(self):
		global input_list
		changetext("cin statement being executed")
		changetext(self.snippet)
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
##class for int datatype
class Int(PrimitiveDT):
	##the constructor
	#@param the value of datatype
	def __init__(self, value=0):
		self.value = value

	##returns the type of value
	def giveType(self):
		return int

	##updates the stored value by typecasting it
	def update(self, val):
		self.value = int(val)

##class for float datatype
class Float(PrimitiveDT):
	##the constructor
	#@param the value of datatype
	def __init__(self, value=0.0):
		self.value = value
	##returns the type of value
	def giveType(self):
		return float
	##updates the stored value by typecasting it
	def update(self, val):
		self.value = float(val)

##class for string datatype
class String(PrimitiveDT):
	##the constructor
	#@param the value of datatype
	def __init__(self, value='""'):
		self.value = value[1:-1]
	##returns the type of value
	def giveType(self):
		return str
	##updates the stored value by typecasting it
	def update(self, val):
		self.value = str(val)

##class for bool datatype
class Bool(PrimitiveDT):
	##the constructor
	#@param the value of datatype
	def __init__(self, value=False):
		self.value = value
	##returns the type of value
	def giveType(self):
		return bool
	##updates the stored value by typecasting it
	def update(self, val):
		self.value = bool(val)
######################################################
##class for binary operator containg operands and the relevant function
class BinaryOp():
	##The constructor
	#@param operator The operation to be done between the values
	#@param left Left side of operand
	#@param right right side of operand
	#@param snippet The relavant code snippet
	def __init__(self, operator, left, right, snippet):
		self.operator = operator
		self.left = left
		self.right = right
		self.snippet = snippet

	##The function that returns the value on evaluating the expression
	def eval(self):
		return self.operator(self.left.eval(), self.right.eval())

	##it evaluates expression
	def exec(self):
		return self.eval()

	##returns the type of operator
	def getOperator(self):
		return self.operator
##functions for addition
def myAdd(x, y):
	return x + y

##functions for subtraction
def mySub(x, y):
	return x - y

##functions for multiplication
def myMult(x, y):
	return x*y

##functions for division
def myDiv(x, y):
	return x/y

##functions for modulo
def myMod(x, y):
	return x%y

##functions for or operator
def myOr(x, y):
	return x or y

##functions for and operator
def myAnd(x, y):
	return x and y

##functions for < operator
def myLessThan(x, y):
	return x < y

##functions for <= operator
def myLessThanEqualTo(x, y):
	return x <= y

##functions for > operator
def myGreaterThan(x, y):
	return x > y

##functions for >= operator
def myGreaterThanEqualTo(x, y):
	return x >= y

##functions for = operator
def myIsEqual(x, y):
	return x == y

##functions for != operator
def myIsNotEqual(x, y):
	return x != y

###############################################################
##class for unary op with function and operand
class UnaryOp():
	##the constructor
	#@param operator The unary op
	#@param operand The operand
	#@param snippet The relevant code snippet 
	def __init__(self, operator, operand, snippet):
		self.operator = operator
		self.operand = operand
		self.snippet = snippet

	##Evaluates the expression
	def eval(self):
		return self.operator(self.operand.eval())

	##Gives the type of operator
	def getOperator(self):
		return self.operator

##function for unary addition
def myPlus(x):
	return x

##function for unary subtraction
def myMinus(x):
	return -x

##function for unary !
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
	def __init__(self,exp, snippet):
		self.exp =exp
		self.snippet = snippet

	def exec(self):
		return self.exp.eval()


class Member_function():
	def __init__(self,reqData, snippet):
		self.name = reqData[0]
		self.functname = reqData[1]
		self.snippet = snippet

	def eval(self):
		return getattr(variableLookup(self.name)[0], self.functname)()

	def exec(self):
		self.eval()

class Multiple_member_function():
	def __init__(self,reqData, snippet):
		self.name=reqData[0]
		self.functname=reqData[1]
		self.arguements=reqData[2]
		self.snippet = snippet

	def eval(self):
		return getattr(variableLookup(self.name)[0], self.functname)(*map(lambda x: x.eval(),self.arguements))

	def exec(self):
		self.eval()

class Unknown_type():
	def __init__(self,value):
		self.value=value

	def eval(self):
		return self.value
##class for making dummy statements in the for loop
class dummyStatements:
## @constructor nothing useful
	def __init__(self):
		pass
## @return True always indicating the case of absence of condition in for loop
	def eval(self):
		return True
## @return nothing... just passes
	def exec(self):
		pass
##/endcond
