from lexer import lexer
from parserClasses import *
from rply import ParserGenerator
initial = input("Enter the code\n")
parser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['COMMA','SEMICOLON','PLUS','MINUS','MUL','DIV','OR','AND','MOD','NOT','LESSEQUAL','GREATEREQUAL','LESS','GREATER','EQUAL','ISEQUAL','NOTEQUAL','OPEN_PARENS','CLOSE_PARENS','OPEN_BRACES','CLOSE_BRACES','OPEN_SQUARE','CLOSE_SQUARE','keyINT','keyINT','keyINT','keyINT','keyINT','keyINT','keyFLOAT','keyFLOAT','keySTRING','keyBOOL','FLOAT','INT','STRING','CHAR','BOOL','BOOL','VARIABLE'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)
variable_dictionary = {}
oper_to_funcname_dict = {'==': myIsEqual, '!=' : myIsNotEqual, '>=': myGreaterThanEqualTo, '<':myLessThan, '>':myGreaterThan, '<=': myLessThanEqualTo}
                        
"""
@parser.production('expression : simplex ISEQUAL simplex')
@parser.production('expression : simplex NOTEQUAL simplex')
@parser.production('expression : simplex GREATER simplex')
@parser.production('expression : simplex GREATEREQUAL simplex')
@parser.production('expression : simplex LESS simplex')
@parser.production('expression : simplex LESSEQUAL simplex')

def expression_symb_expression(p):
	#p is the list of all tokens matched
	#to handle the case of expression followed by an expression
	BinOp = BinaryOp(oper_to_funcname_dict[p[1].getstr()])
	print(p[0])
	print(p[2])

@parser.production('expression : simplex PLUS simplex')
def function(p):
	print(type(p[0]), type(p[1]), type(p[2]))
	return
@parser.production('simplex : INT PLUS INT')
def second(p):
	return int(p[2].getstr()) + int(p[0].getstr())


"""

#########################################################################################################################
# all parser rules for Expression
@parser.production('main : assignment')
@parser.production('main : expression')
@parser.production('main : variable')
def main_p(argList):
	return argList[0]


@parser.production('assignment : VARIABLE EQUAL INT')
def assign_variable(argList):
	if argList[0].getstr() not in variable_dictionary:
		raise Exception("Variable "+argList[0].getstr() + " needs to be declared before initialization")
	else:
		variable_dictionary[argList[0].getstr()].update(expression.eval())
	return None
#########################################################################################################################
# all parser rules for Expression

@parser.production('expression : simplex ISEQUAL simplex')
@parser.production('expression : simplex LESS simplex')
@parser.production('expression : simplex LESSEQUAL simplex')
@parser.production('expression : simplex GREATER simplex')
@parser.production('expression : simplex GREATEREQUAL simplex')
@parser.production('expression : simplex NOTEQUAL simplex')
def simplex_isequal_simplex(argList):
	return BinaryOp(oper_to_funcname_dict[argList[1].getstr()], argList[0], argList[2])


@parser.production('expression : simplex')
def simplex_to_expression(argList):
	return argList[0]


#########################################################################################################################
# all parser rules for Simple Expression

@parser.production('simplex :  PLUS term PLUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, UnaryOp(myPlus, argList[1]), argList[3])

@parser.production('simplex :  PLUS term MINUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, UnaryOp(myPlus, argList[1]), argList[3])

@parser.production('simplex :  MINUS term PLUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, UnaryOp(myMinus, argList[1]), argList[3])

@parser.production('simplex :  MINUS term MINUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, UnaryOp(myMinus, argList[1]), argList[3])
	
@parser.production('simplex : term PLUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, argList[0], argList[2])

@parser.production('simplex : term MINUS simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, argList[0], argList[2])

@parser.production('simplex :  term OR simplex')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myOr, argList[0], argList[2])

@parser.production('simplex :  PLUS term')
def plus_term_to_simplex(argList):
	return UnaryOp(myPlus, argList[1])

@parser.production('simplex :  MINUS term')
def plus_term_to_simplex(argList):
	return UnaryOp(myMinus, argList[1])


@parser.production('simplex : term')
def plus_term_to_simplex(argList):
	return argList[0]
#########################################################################################################################
# all parser rules for term

@parser.production('term : factor MUL term')
@parser.production('term : factor DIV term')
def factor_mul_to_term(argList):
	if argList[1].getstr() == '*':
		return BinaryOp(myMult, argList[0], argList[2])
	else:
		return BinaryOp(myDiv, argList[0], argList[2])

@parser.production('term : factor MOD term')
def factor_mod_to_term(argList):
	return BinaryOp(myMod, argList[0], argList[2])

@parser.production('term : factor AND term')
def factor_and_to_term(argList):
	return BinaryOp(myAnd, argList[0], argList[2])

@parser.production('term : factor')
def factor_to_term(argList):
	return argList[0]


#########################################################################################################################
# all parser rules for factor

@parser.production('factor : variable')
def variable_to_factor(argList):
	return argList[0]

@parser.production('factor : INT')
def int_to_factor(argList):
	return Int(int(argList[0].getstr()))

@parser.production('factor : FLOAT')
def float_to_factor(argList):
	return Float(float(argList[0].getstr()))

@parser.production('factor : STRING')
def string_to_factor(argList):
	return String(argList[0].getstr())

@parser.production('factor : BOOL')
def bool_to_factor(argList):
	if argList[0].getstr() == 'true':
		return Bool(True)

	return Bool(False)

@parser.production('factor : NOT factor')
def notfactor_to_factor(argList):
	return UnaryOp(myNot,argList[1])

@parser.production('factor : OPEN_PARENS expression CLOSE_PARENS')

def paren_expression_to_factor(argList):
	return argList[1]

#########################################################################################################################

#all parser rules for variables

@parser.production('variable : keyINT VARIABLE')
def store_variable(argList):
	dtObject = Int(0)
	variable_dictionary[argList[1].getstr()] = dtObject
	return dtObject

@parser.production('variable : keyFLOAT VARIABLE')
def store_variable(argList):
	dtObject = Float(0.0)
	variable_dictionary[argList[1].getstr()] = dtObject
	return dtObject

@parser.production('variable : keyBOOL VARIABLE')
def store_variable(argList):
	dtObject = Bool(False)
	variable_dictionary[argList[1].getstr()] = dtObject
	return dtObject

@parser.production('variable : keySTRING VARIABLE')
def store_variable(argList):
	dtObject = String(0)
	variable_dictionary[argList[1].getstr()] = dtObject
	return dtObject

@parser.production('variable : VARIABLE')
def search_variable(argList):
	var_name = argList[0].getstr()
	if  var_name not in variable_dictionary:
		raise Exception('Variable '+var_name+' not declared')
	return variable_dictionary[var_name]

@parser.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())
#########################################################################################################################
mainparser = parser.build()
#stream = lexer.lex(initial)
#print(stream.next())
#print(stream.next())
#print(stream.next())
print(mainparser.parse(lexer.lex(initial)).eval())