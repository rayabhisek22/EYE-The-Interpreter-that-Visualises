from lexer import lexer
from parserClasses import *
from rply import ParserGenerator

import sys
# lines = []
# for line in sys.stdin:
#     lines.append(line)
# initial = ''.join(lines)
# del lines

parser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
    'COMMA','SEMICOLON','PLUS','MINUS','MUL','DIV','OR','AND','MOD','NOT','LESSEQUAL','GREATEREQUAL',
    'LESS','GREATER','EQUAL','ISEQUAL','NOTEQUAL','OPEN_PARENS','CLOSE_PARENS','OPEN_BRACES','CLOSE_BRACES',
    'OPEN_SQUARE','CLOSE_SQUARE','keyINT','keyINT','keyINT','keyINT','keyINT','keyINT','keyFLOAT','keyFLOAT',
    'keySTRING','keyBOOL','FLOAT','INT','STRING','BOOL','VARIABLE', 'keyIF', 'keyFOR', 'keyWHILE',
    'keyELSE', 'keyELIF', 'keyCOUT', 'COUTOPER', 'keyCIN', 'CINOPER', 'ENDL','LINKEDLIST', 'DOT','STACK','QUEUE',
    'BST', 'MAIN', 'RETURN', 'VOID', 'PLUSEQUAL', 'MINUSEQUAL', 'MULTEQUAL', 'DIVEQUAL', 'MODEQUAL', 'COMSTART', 'COMEND'
    ]
)
oper_to_funcname_dict = {'==': myIsEqual, '!=' : myIsNotEqual, '>=': myGreaterThanEqualTo, '<':myLessThan, '>':myGreaterThan,
 '<=': myLessThanEqualTo}
keyword_dictionary = {'int' : Int, 'bool' : Bool, 'float' : Float, 'string' : String } 
data_struct_dictionary={'linkedList':SinglyLinkedList, 'queue':Queue, 'stack':Stack, 'binarySearchTree':BinarySearchTree}
keyword_default_value_dict = {'int' : 0, 'bool' : False, 'float' : 0.0, 'string' : "" } 

 												#START POINT OF PARSER

# all parser rules for main

@parser.production('givenprogram : givencode')
def code_to_program(argList):
	return argList[0]

@parser.production('givencode : globals main')
def code_of_main(argList):
	return argList[0] + [argList[1]]

@parser.production('givencode : main')
def code_of_main(argList):
	return [argList[0]]

@parser.production('globals : func-declaration globals')
def func_declare_in_globals(argList):
	return [argList[0]] + argList[1]

@parser.production('globals : declaration SEMICOLON globals')
def declare_in_globals(argList):
	return argList[0] + argList[2]


@parser.production('globals : func-declaration')
def func_declare(argList):
	return [argList[0]]
@parser.production('globals : declaration SEMICOLON')
def declare_global(argList):
	return argList[0]

@parser.production('main : MAIN block') #block for now... will change it as we proceed
def main_p(argList):
	return argList[1]

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
@parser.production('statement : input-stream SEMICOLON')
def output_stream(argList):
	return [CinStatement(argList[0])]
@parser.production('statement : class-functions-object SEMICOLON')
def make_exec(argList):
	return [argList[0]]

@parser.production('statement : RETURN SEMICOLON')
def void_return(argList):
	return [Return()]

@parser.production('statement : RETURN expression SEMICOLON')
def nonvoid_return(argList):
	return [Return(argList[1])]

@parser.production('statement : function-call SEMICOLON')
def function_call(argList):
	return [argList[0]]
#########################################################################################################################

 												#BLOCKS AND STATEMENTS ENDS

#########################################################################################################################

#########################################################################################################################

 												#FUNCTIONS START

#########################################################################################################################
#declarations
@parser.production('func-declaration : keyword VARIABLE OPEN_PARENS CLOSE_PARENS block')
def func_declaration_to_class (argList):
	return FuncDeclaration(argList[1].getstr(), [], argList[4])

@parser.production('func-declaration : keyword VARIABLE OPEN_PARENS vars CLOSE_PARENS block')
def func_declaration_to_class (argList):
	return FuncDeclaration(argList[1].getstr(), argList[3], argList[5])



@parser.production('vars : var COMMA vars')
def multiple_ar(argList):
	return [argList[0]] + argList[2]

@parser.production('vars : var')
def single_var(argList):
	return [argList[0]]

@parser.production('var : keyword VARIABLE')
def argument_variable(argList):
	return (argList[1].getstr(), keyword_dictionary[argList[0]])


#calls
@parser.production('function-call : VARIABLE OPEN_PARENS CLOSE_PARENS')
def nonparameter_func_call(argList):
	return FunctionCall(argList[0].getstr(), [])

@parser.production('function-call : VARIABLE OPEN_PARENS expressions CLOSE_PARENS')
def parameter_func_call(argList):
	return FunctionCall(argList[0].getstr(), argList[2])
#########################################################################################################################

 												#FUNCTIONS ENDS

#########################################################################################################################



@parser.production('class-functions-object : class-functions')
def class_function_to_object(argList):
	if len(argList[0])==2:
		return Member_function(argList[0])
	else:
		return Multiple_member_function(argList[0])

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

 												#CIN-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('input-stream : keyCIN cinopers')
def input_stream(argList):
	return argList[1]
@parser.production('cinopers : CINOPER variable cinopers')
def cinoper_expression_coutopers(argList):
	return [argList[1]] + argList[2]
@parser.production('cinopers : CINOPER variable')
def cinoper_expression(argList):
	return [argList[1]]

#########################################################################################################################

 												#CIN-BLOCK ENDS

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
	return argList[4] + [(argList[0].getstr(), argList[2], [])] ##check
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

@parser.production('assignment : variable PLUSEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],BinaryOp(myAdd, argList[0], argList[2]))

@parser.production('assignment : variable MINUSEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],BinaryOp(mySub, argList[0], argList[2]))

@parser.production('assignment : variable MULTEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],BinaryOp(myMult, argList[0], argList[2]))

@parser.production('assignment : variable DIVEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],BinaryOp(myDiv, argList[0], argList[2]))

@parser.production('assignment : variable MODEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	return Assignment(argList[0],BinaryOp(myMod, argList[0], argList[2]))

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

@parser.production('simplex :  PLUS simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, UnaryOp(myPlus, argList[1]), argList[3])

@parser.production('simplex :  PLUS simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, UnaryOp(myPlus, argList[1]), argList[3])

@parser.production('simplex :  MINUS simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, UnaryOp(myMinus, argList[1]), argList[3])

@parser.production('simplex :  MINUS simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, UnaryOp(myMinus, argList[1]), argList[3])
	
@parser.production('simplex : simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(myAdd, argList[0], argList[2])

@parser.production('simplex : simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	return BinaryOp(mySub, argList[0], argList[2])

@parser.production('simplex :  simplex OR term')
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

@parser.production('term : term MUL factor')
@parser.production('term : term DIV factor')
def factor_mul_to_term(argList):
	if argList[1].getstr() == '*':
		return BinaryOp(myMult, argList[0], argList[2])
	else:
		return BinaryOp(myDiv, argList[0], argList[2])

@parser.production('term : term MOD factor')
def factor_mod_to_term(argList):
	return BinaryOp(myMod, argList[0], argList[2])

@parser.production('term : term AND factor')
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

@parser.production('factor : class-functions-object')
@parser.production('factor : function-call')
def classFuncobject_to_expression(argList):
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

fileName = sys.argv[1]
file = open(fileName,'r')
initial = ""
for chunk in file:
	initial += chunk
file.close()
mainparser = parser.build()
for item in mainparser.parse(lexer.lex(initial)):
	item.exec()
# for item in list_variable_dict[mainIndex]:
# 	if type(list_variable_dict[mainIndex][item]).__name__ == 'Array':
# 		for i in range(list_variable_dict[mainIndex][item].length):
# 			print(item + " at index " + str(i) + " = " + str(list_variable_dict[mainIndex][item].get(i).eval()))
# 	else:
# 		print(item, list_variable_dict[mainIndex][item].eval())


