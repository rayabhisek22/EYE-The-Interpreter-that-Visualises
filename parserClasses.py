from rply.token import *

list_variable_dict = [{}]
mainIndex = 0

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
        if  self.name not in list_variable_dict[mainIndex]:
            raise Exception('\n\nVariable '+ self.name +' not declared')
        return list_variable_dict[mainIndex][self.name].get(self.index.eval()).eval()

    def update(self, value):
        if  self.name not in list_variable_dict[mainIndex]:
            raise Exception('\n\nVariable '+ self.name +' not declared')
        list_variable_dict[mainIndex][self.name].update(self.index.eval(), value.eval())

class Variable():
    def __init__(self,name):
        self.name=name

    def eval(self):
        if  self.name not in list_variable_dict[mainIndex]:
            raise Exception('\n\nVariable '+ self.name +' not declared')
        return list_variable_dict[mainIndex][self.name].eval()

    def update(self,obj2):
        if  self.name not in list_variable_dict[mainIndex]:
            raise Exception('\n\nVariable '+ self.name +' not declared')
        list_variable_dict[mainIndex][self.name].update(obj2.eval())
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
        list_variable_dict[mainIndex][self.varName] = self.varType(self.varValue.eval())

class ArrayDeclaration():
    def __init__(self, varName, varType, length, varValue):
        self.varType = varType
        self.length = length
        self.varValue = varValue
        self.varName = varName

    def exec(self):
        list_variable_dict[mainIndex][self.varName] = Array(self.varType(self.varValue.eval()), self.length.eval())

class Array(): #variable class of array
    def __init__(self, initClass, length):
        self.array = []
        for i in range(length):
            self.array.append(initClass.__class__(initClass.eval()))
        self.length = length

    def get(self, i):
        return self.array[i]

    def update(self, i, value):
        self.array[i].update(value)

class Block():
    def __init__(self, listExecutables):
        self.listExecutables = listExecutables

    def exec(self):
        for executable in self.listExecutables:
            # if type(executable) is list:
            #     if executable[0] == 'FOR':
            #         executable[1].exec()
            #         while(executable[1].eval()):
            #             for item in executable[2]:
            #                 item.exec()
            #             executable[3].eval()
            executable.exec()

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
