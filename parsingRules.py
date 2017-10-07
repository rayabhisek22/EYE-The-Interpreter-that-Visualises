from lexer import lexer
from parserClasses import *
from rply import ParserGenerator
import sys
lines = []
for line in sys.stdin:
    lines.append(line)
initial = ''.join(lines)
del lines

parser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
    'COMMA','SEMICOLON','PLUS','MINUS','MUL','DIV','OR','AND','MOD','NOT','LESSEQUAL','GREATEREQUAL',
    'LESS','GREATER','EQUAL','ISEQUAL','NOTEQUAL','OPEN_PARENS','CLOSE_PARENS','OPEN_BRACES','CLOSE_BRACES',
    'OPEN_SQUARE','CLOSE_SQUARE','keyINT','keyINT','keyINT','keyINT','keyINT','keyINT','keyFLOAT','keyFLOAT',
    'keySTRING','keyBOOL','FLOAT','INT','STRING','CHAR','BOOL','VARIABLE', 'keyIF', 'keyFOR', 'keyWHILE',
    'keyELSE', 'keyELIF', 'keyCIN', 'keyCOUT', 'CINOPER', 'COUTOPER', 'ENDL','LINKEDLIST', 'DOT','STACK','QUEUE','BST'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    #still don't know how it works
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)
oper_to_funcname_dict = {'==': myIsEqual, '!=' : myIsNotEqual, '>=': myGreaterThanEqualTo, '<':myLessThan, '>':myGreaterThan, '<=': myLessThanEqualTo}
keyword_dictionary = {'int' : Int, 'bool' : Bool, 'float' : Float, 'string' : String } 
data_struct_dictionary={'linkedList':SinglyLinkedList, 'queue':Queue, 'stack':Stack, 'binarySearchTree':BinarySearchTree}
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
	return Block(argList[1])

#########################################################################################################################
# all parser rules for statements
@parser.production('statements : statement statements')
def multiple_statement(argList):
	return argList[0] + argList[1]
@parser.production('statements : statement')
def single_statement(argList):
	return argList[0]
def exec_curr_statement(argList):
	"""execute current statement"""
	return

#@parser.production('statements : ')
#def corner_case_block(argList):
#	raise Exception("Please enter something in the braces or else remove them")

#########################################################################################################################
# all parser rules for a single statement
@parser.production('statement : block')
def statement_block(argList):
	return argList[0]
@parser.production('statement : declaration SEMICOLON')
def declaration_statement(argList):
	return argList[0]
@parser.production('statement : assignment SEMICOLON')
def assignment_statement(argList):
	return [argList[0]]
@parser.production('statement : for-block')
@parser.production('statement : while-block')
def exec_type_of_statement(argList):
	""" executes particualar type of statement"""
	return [argList[0]]

@parser.production('statement : if-block elif-blocks else-block')
def if_elifs_else(argList):
	return [IfStatement(argList[0] + argList[1] + argList[2])]
@parser.production('statement : if-block elif-blocks')
def if_elifs(argList):
	return [IfStatement(argList[0] + argList[1])]
@parser.production('statement : if-block else-block')
def if_else(argList):
	return [IfStatement(argList[0] + argList[1])]
@parser.production('statement : if-block')
def if_only(argList):
	return [IfStatement(argList[0])]

# @parser.production('statement : input-stream')
# def take_input(argList):

@parser.production('statement : output-stream SEMICOLON')
def output_stream(argList):
	return [CoutStatement(argList[0])]
@parser.production('statement : class-functions SEMICOLON')
def make_exec(argList):
	if len(argList[0])==2:
		return [Member_function(argList[0])]
	else:
		return [Multiple_member_function(argList[0])]


#########################################################################################################################

 												#BLOCKS AND STATEMENTS ENDS

#########################################################################################################################

@parser.production('class-functions : VARIABLE DOT VARIABLE OPEN_PARENS CLOSE_PARENS')
def function_call(argList):
	return [argList[0].getstr(),argList[2].getstr()]

@parser.production('class-functions : VARIABLE DOT VARIABLE OPEN_PARENS expressions CLOSE_PARENS')
def function_call_2(argList):
	return [argList[0].getstr(),argList[2].getstr(),argList[4]]

@parser.production('expressions : expression COMMA expressions')
def list_of_expression(argList):
	return [argList[0]]+ argList[2]

@parser.production('expressions : expression')
def list_of_expression(argList):
	return [argList[0]]




#########################################################################################################################

 												#FOR-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('for-block : keyFOR OPEN_PARENS declaration SEMICOLON expression SEMICOLON assignment CLOSE_PARENS block')
def block_of_for(argList):
	return ForLoop(argList[2], argList[4], argList[6], argList[8])

#########################################################################################################################

 												#FOR-BLOCK ENDS

#########################################################################################################################


#########################################################################################################################

 												#WHILE-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('while-block : keyWHILE OPEN_PARENS expression CLOSE_PARENS block')
def block_of_for(argList):
	return WhileLoop(argList[2], argList[4])

#########################################################################################################################

 												#WHILE-BLOCK ENDS

#########################################################################################################################

#########################################################################################################################

 												#COUT-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('output-stream : keyCOUT coutopers')
def output_stream(argList):
	return argList[1]
@parser.production('coutopers : COUTOPER ENDL coutopers')
def coutoper_endl_coutopers(argList):
	return [String("\n")] + argList[2]
@parser.production('coutopers : COUTOPER expression coutopers')
def coutoper_expression_coutopers(argList):
	return [argList[1]] + argList[2]
@parser.production('coutopers : COUTOPER ENDL')
def coutoper_endl(argList):
	return [String('"\n"')]
@parser.production('coutopers : COUTOPER expression')
def coutoper_expression(argList):
	return [argList[1]]

#########################################################################################################################

 												#COUT-BLOCK ENDS

#########################################################################################################################


#########################################################################################################################

 												#IF-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('if-block : keyIF OPEN_PARENS expression CLOSE_PARENS block')
def if_statement_runner(argList):
	return [[argList[2], argList[4]]]

@parser.production('elif-blocks : elif-block elif-blocks')
def elif_blocks1(argList):
	return argList[0] + argList[1]
@parser.production('elif-blocks : elif-block')
def elif_blocks2(argList):
	return argList[0]
@parser.production('elif-block : keyELIF OPEN_PARENS expression CLOSE_PARENS block')
def elif_block(argList):
	return [[argList[2], argList[4]]]
@parser.production('else-block : keyELSE block')
def else_block(argList):
	return [[Bool(True), argList[1]]]

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
	executionList = []
	for eachVar in argList[1]:
		if len(eachVar) == 3:
			executionList.append(ArrayDeclaration(eachVar[0], keyword_dictionary[argList[0]], eachVar[1], keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]]))) #list_variable_dict[mainIndex][eachVar[0]] = Array(keyword_dictionary[argList[0]](), eachVar[1])
		elif eachVar[1] == None:
			executionList.append(PrimitiveDeclaration(eachVar[0], keyword_dictionary[argList[0]], keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]]))) #list_variable_dict[mainIndex][eachVar[0]] = keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]])
		else:
			executionList.append(PrimitiveDeclaration(eachVar[0], keyword_dictionary[argList[0]], eachVar[1])) #list_variable_dict[mainIndex][eachVar[0]] = keyword_dictionary[argList[0]](eachVar[1])
	return executionList

@parser.production('declaration : LINKEDLIST LESS keyword GREATER new_variables')
@parser.production('declaration : STACK LESS keyword GREATER new_variables')
@parser.production('declaration : QUEUE LESS keyword GREATER new_variables')
@parser.production('declaration : BST LESS keyword GREATER new_variables')
def data_structure_init(argList):
	executionList=[]
	for eachVar in argList[4]:
		executionList.append(DataStructureDeclaration(data_struct_dictionary[argList[0].getstr()], eachVar,argList[2]))
	return executionList

@parser.production('new_variables : VARIABLE COMMA new_variables')
def list_of_variables(argList):
	return argList[2]+[argList[0].getstr()]

@parser.production('new_variables : VARIABLE')
def list_of_variables(argList):
	return [argList[0].getstr()]



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
	elif argList[0].gettokentype() == 'keySTRING':
		return 'string'

#########################################################################################################################
# all parser rules for default_assigns

@parser.production('default_assigns : VARIABLE OPEN_SQUARE expression CLOSE_SQUARE COMMA default_assigns')
def default_assign_array(argList):
	return argList[4] + [(argList[0].getstr(), argList[2], [])]
@parser.production('default_assigns : VARIABLE EQUAL expression COMMA default_assigns')
def default_assign_with_value(argList):
	"""appends the variable along with value in the list of default_assigns"""
	return argList[4] + [(argList[0].getstr(), argList[2])]


@parser.production('default_assigns : VARIABLE COMMA default_assigns')
def default_assign_without_value(argList):
	"""appends the variable without value in the list of default_assigns"""
	return argList[2] + [(argList[0].getstr(), None)]

@parser.production('default_assigns : VARIABLE OPEN_SQUARE expression CLOSE_SQUARE')
def default_assign_array(argList):
	return [(argList[0].getstr(), argList[2], [])]

@parser.production('default_assigns : VARIABLE EQUAL expression')
def default_assign_without_value(argList):
	"""returns a list of variable with value tuple"""
	return [(argList[0].getstr(), argList[2])]


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

@parser.production('assignment : variable EQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],argList[2])

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
@parser.production('variable : VARIABLE OPEN_SQUARE expression CLOSE_SQUARE')
def search_array_variable(argList):
	""" searches for the array element at the given index"""
	result = argList[2]
	return ArrayVariable(argList[0].getstr(), result)

@parser.production('variable : VARIABLE')
def search_variable(argList):
	"""searches for the variable in the variable dictionary and if found
		return the corresponding object"""
	var_name = argList[0].getstr()
	return Variable(var_name)
	#return [var_name, list_variable_dict[mainIndex][var_name]] #one


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
mainparser.parse(lexer.lex(initial)).exec()
# for item in list_variable_dict[mainIndex]:
# 	if type(list_variable_dict[mainIndex][item]).__name__ == 'Array':
# 		for i in range(list_variable_dict[mainIndex][item].length):
# 			print(item + " at index " + str(i) + " = " + str(list_variable_dict[mainIndex][item].get(i).eval()))
# 	else:
# 		print(item, list_variable_dict[mainIndex][item].eval())


