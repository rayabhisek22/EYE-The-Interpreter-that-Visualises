#from rply.token import 

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class PrimitiveDT():
    def __init__(self, value):
        self.value = value

    def getValue():
        return self.value

class Int(PrimitiveDT):
    def value():
        return self.value

    def giveType():
        return int

class Float(PrimitiveDT):
    def value():
        return self.value

    def giveType():
        return float

class String(PrimitiveDT):
    def value():
        return self.value

    def giveType():
        return str

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Rem(BinaryOp):
    def eval(self):
        return self.left.eval.eval() % self.right.eval()