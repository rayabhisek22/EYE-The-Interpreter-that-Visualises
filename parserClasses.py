#from rply.token import 

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

class Variable():
    def __init__(self,name,obj):
        self.name=name
        self.value=obj

    def eval(self):
        return self.value.eval()

    def update(obj2):
        self.value=obj2

def Assignment():
    def __init__(self,left,right):
        self.left=left
        self.right=right

#########################################################
class Int(PrimitiveDT):
    def giveType():
        return int

class Float(PrimitiveDT):
    def giveType():
        return float

class String(PrimitiveDT):
    def giveType():
        return str

class Bool(PrimitiveDT):
    def giveType():
        return bool
######################################################
class BinaryOp():
    def __init__(self, operator):
        self.operator = operator

    def eval(self, left, right):
        return self.operator(left, right)

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

def myOR(x, y):
    return x or y

def myAND(x, y):
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
    def __init__(self, operator):
        self.operator = operator

    def eval(self, operand):
        return self.operator(operand)

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