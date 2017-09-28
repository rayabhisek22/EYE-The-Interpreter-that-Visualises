from lexer import lexer
from parserClasses import *
from rply import ParserGenerator
lines = []
while True:
	try:
		line = input()
		if line:
			lines.append(line)
		else:
			break
	except:
		break

initial = ''.join(lines)
del lines
parser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
    'COMMA','SEMICOLON','PLUS','MINUS','MUL','DIV','OR','AND','MOD','NOT','LESSEQUAL','GREATEREQUAL',
    'LESS','GREATER','EQUAL','ISEQUAL','NOTEQUAL','OPEN_PARENS','CLOSE_PARENS','OPEN_BRACES','CLOSE_BRACES',
    'OPEN_SQUARE','CLOSE_SQUARE','keyINT','keyINT','keyINT','keyINT','keyINT','keyINT','keyFLOAT','keyFLOAT',
    'keySTRING','keyBOOL','FLOAT','INT','STRING','CHAR','BOOL','VARIABLE', 'keyIF', 'keyFOR', 'keyWHILE'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    #still don't know how it works
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)
variable_dictionary = {}
oper_to_funcname_dict = {'==': myIsEqual, '!=' : myIsNotEqual, '>=': myGreaterThanEqualTo, '<':myLessThan, '>':myGreaterThan, '<=': myLessThanEqualTo}
keyword_dictionary = {'int' : Int, 'bool' : Bool, 'float' : Float, 'string' : String } 
keyword_default_value_dict = {'int' : 0, 'bool' : False, 'float' : 0.0, 'string' : "" } 
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

 												#START POINT OF PARSER

# all parser rules for main
@parser.production('main : block') #block for now... will change it as we proceed
def main_p(argList):
	return argList[0]

#########################################################################################################################


#########################################################################################################################

 												#BLOCKS AND STATEMENTS STARTS

#########################################################################################################################


# all parser rules for block
@parser.production('block : OPEN_BRACES statements CLOSE_BRACES')
def exec_all_statements(argList):
	"""executes all the statements inside a given block"""
	return;

#########################################################################################################################
# all parser rules for statements
@parser.production('statements : statement statements')
@parser.production('statements : statement')
def exec_curr_statement(argList):
	"""execute current statement"""
	return

#@parser.production('statements : ')
#def corner_case_block(argList):
#	raise Exception("Please enter something in the braces or else remove them")

#########################################################################################################################
# all parser rules for a single statement
@parser.production('statement : declaration SEMICOLON')
@parser.production('statement : assignment SEMICOLON')
#@parser.production('statement : if-block elif-blocks else-block')
#@parser.production('statement : if-block else-block')
@parser.production('statement : if-block')
def exec_type_of_statement(argList):
	""" executes particualar type of statement"""
	return

#########################################################################################################################

 												#BLOCKS AND STATEMENTS ENDS

#########################################################################################################################



#########################################################################################################################

 												#IF-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('if-block : keyIF OPEN_PARENS expression CLOSE_PARENS block')
def block_of_if(argList):
	""" function for if with a block"""
	if not argList[2].eval():
		return 5


#@parser.production('if-block : keyIF OPEN_PARENS expression CLOSE_PARENS statement')





#########################################################################################################################

 												#IF-BLOCK ENDS

#########################################################################################################################



#########################################################################################################################

 												#DECLARATION STARTS

#########################################################################################################################
# all parser rules for a single declaration
@parser.production('declaration : keyword default_assigns')
def declare_variables(argList):
	""" declares one or more than one variables
		keyword is a string which contains name of type
		default_assigns is a list of tuples
		each tuple is a 2 element tuple which
		contains a string of name and value"""
	for eachVar in argList[1]:
		if eachVar[0] in variable_dictionary:
			raise Exception("\n\nVariable " + eachVar[0] + " already declared")
		elif eachVar[1] == None:
			variable_dictionary[eachVar[0]] = keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]])
		else:
			variable_dictionary[eachVar[0]] = keyword_dictionary[argList[0]](eachVar[1])
	return

#########################################################################################################################
# all parser rules for a keyword
@parser.production('keyword : keyINT')
@parser.production('keyword : keyFLOAT')
@parser.production('keyword : keyBOOL')
@parser.production('keyword : keySTRING')
def keyword_to_string(argList):
	"""converts the keyword to its correponding string which
		is to be give to the declaration block"""
	if argList[0].gettokentype() == 'keyINT':
		return 'int'
	elif argList[0].gettokentype() == 'keyFLOAT':
		return 'float'
	elif argList[0].gettokentype() == 'keyBOOL':
		return 'bool'
	if argList[0].gettokentype() == 'keySTRING':
		return 'string'

#########################################################################################################################
# all parser rules for default_assigns

@parser.production('default_assigns : VARIABLE EQUAL expression COMMA default_assigns')
def default_assign_with_value(argList):
	"""appends the variable along with value in the list of default_assigns"""
	return argList[4] + [(argList[0].getstr(), argList[2].eval())]


@parser.production('default_assigns : VARIABLE COMMA default_assigns')
def default_assign_without_value(argList):
	"""appends the variable without value in the list of default_assigns"""
	return argList[2] + [(argList[0].getstr(), None)]


@parser.production('default_assigns : VARIABLE EQUAL expression')
def default_assign_without_value(argList):
	"""returns a list of variable with value tuple"""
	return [(argList[0].getstr(), argList[2].eval())]


@parser.production('default_assigns : VARIABLE')

	
def default_assign_without_value(argList):
	"""returns a list of variable without value tuple"""
	return [(argList[0].getstr(), None)]




#########################################################################################################################

 												#DECLARATION ENDS

#########################################################################################################################




#########################################################################################################################

 												#ASSIGNMENT STARTS

#########################################################################################################################
#########################################################################################################################
# all parser rules for assignment

@parser.production('assignment : VARIABLE EQUAL expression')
def assign_variable(argList):
	if argList[0].getstr() not in variable_dictionary:
		raise Exception("\n\nVariable "+argList[0].getstr() + " needs to be declared before initialization")
	else:
		variable_dictionary[argList[0].getstr()].update(argList[2].eval())
	return None

#########################################################################################################################

 												#ASSIGNMENT ENDS

#########################################################################################################################





#########################################################################################################################

 												#EXPRESSION STARTS

#########################################################################################################################


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

 												#EXPRESSION ENDS

#########################################################################################################################



#########################################################################################################################

 												#VARIABLE STARTS

#########################################################################################################################


#all parser rules for variables:: still not used mostly

#@parser.production('variable : variable OPEN_SQUARE expression CLOSE_SQUARE')
#def search_array_varialbe(argList):

@parser.production('variable : VARIABLE')
def search_variable(argList):
	"""searches for the variable in the variable dictionary and if found
		return the corresponding object"""
	var_name = argList[0].getstr()
	if  var_name not in variable_dictionary:
		raise Exception('\n\nVariable '+var_name+' not declared')
	return variable_dictionary[var_name]


#########################################################################################################################

 												#VARIABLE ENDS

#########################################################################################################################




#########################################################################################################################

 												#ERROR HANDLER

@parser.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

#########################################################################################################################

#########################################################################################################################


mainparser = parser.build()
print(mainparser.parse(lexer.lex(initial)))
for item in variable_dictionary:
	print(item, variable_dictionary[item].eval())




