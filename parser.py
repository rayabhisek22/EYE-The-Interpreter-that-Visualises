#from rply.token import 

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class PrimitiveDT():
    def __init__(self, value):
        self.value = value

    def eval():
        return self.value

class Variable():
    def __init__(self,name):
        self.name=name


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

class Expression():
    def __init__(self):
        self.elements = []

class Simplex():
    def __init__(self):
        self.elements = []

class Term():
    def __init__(self):
        self.elements = []

clas Factor():
    def __init__(self):
        self.elements = []