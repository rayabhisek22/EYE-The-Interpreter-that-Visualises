##@mainpage Eye, The Interpreter that Visualises
#
#\section Intro_sec Introduction
#
#This is the course project for the team 3 Idiots for CS 251-Software Systems Lab
#<br>
#In this project, we have built an interpeter for a rule-based programming language of our own that is syntactically similar to C++.
#However, this is not just run-of-the-mill interpreter-it has the added feauture of actually allowing you to visualise what is going on
#behind the scenes as your code is being run.
#
#\section running How to run your code?
#
#<running instructions, Bansal ?>
#
#\section tp <add more stuff>
#
#Anyone with any ideas add stuff to this page...the code for this page is at the top of ParsingRulesActual.py
#





from lexer import lexer
from ParsingClassesActual import *
from rply import ParserGenerator

import sys
# lines = []
# for line in sys.stdin:
#     lines.append(line)
# initial = ''.join(lines)
# del lines
##@brief the object of parsergenerator which takes list of all tokens as arguments
#the parser rules are given to 'production' method of this instance
#every parser rules if matched, calls the written just after the rule
#the function has to take a single argument which is the list of all matched patterns
#also the function return a list of two elements, one of which is the main return format and other one the corresponding code snippet
parser = ParserGenerator(
    # a list of all token names, accepted by the parser.
    [
    'COMMA','SEMICOLON','PLUS','MINUS','MUL','DIV','OR','AND','MOD','NOT','LESSEQUAL','GREATEREQUAL',
    'LESS','GREATER','EQUAL','ISEQUAL','NOTEQUAL','OPEN_PARENS','CLOSE_PARENS','OPEN_BRACES','CLOSE_BRACES',
    'OPEN_SQUARE','CLOSE_SQUARE','keyINT','keyINT','keyINT','keyINT','keyINT','keyINT','keyFLOAT','keyFLOAT',
    'keySTRING','keyBOOL','FLOAT','INT','STRING','BOOL','VARIABLE', 'keyIF', 'keyFOR', 'keyWHILE',
    'keyELSE', 'keyELIF', 'keyCOUT', 'COUTOPER', 'keyCIN', 'CINOPER', 'ENDL','LINKEDLIST', 'DOT','STACK','QUEUE',
    'BST', 'MAIN', 'RETURN', 'VOID', 'PLUSEQUAL', 'MINUSEQUAL', 'MULTEQUAL', 'DIVEQUAL', 'MODEQUAL'
    ]
)

##@var oper_to_funcname_dict dictionary to given the class corresponding to the operator
oper_to_funcname_dict = {'==': myIsEqual, '!=' : myIsNotEqual, '>=': myGreaterThanEqualTo, '<':myLessThan, '>':myGreaterThan,
 '<=': myLessThanEqualTo}

##@var keyword_dictionary dictionary to given the class corresponding to the data type
keyword_dictionary = {'int' : Int, 'bool' : Bool, 'float' : Float, 'string' : String } 

##@var data_struct_dictionary dictionary to give the class corresponding to the data structure
data_struct_dictionary={'linkedlist':SinglyLinkedList, 'queue':Queue, 'stack':Stack, 'binarysearchtree':BinarySearchTree}
##@var keyword_default_value_dict gives the default values of every data type
keyword_default_value_dict = {'int' : 0, 'bool' : False, 'float' : 0.0, 'string' : "" } 

 												#start point of parser

##@brief all parser rules for all global variables , functions and main_program 
##@brief the first parser rule which is checked first
@parser.production('givenprogram : givencode')
##@brief function to return the code as a list of global variables, functions and main_program
def code_to_program(arglist):
	print(arglist[0][1])
	return arglist[0][0]

##@brief 'globals' contain all global variables and functions but not the main program 
@parser.production('givencode : globals main')
##@return the list of all global variables, functions and main program
def code_of_main(arglist):
	return [arglist[0][0] + [arglist[1][0]], arglist[0][1] + arglist[1][1]]

##@brief checks for main program
@parser.production('givencode : main')
##@return the list containing code of main_program
def code_of_main(arglist):
	return [[arglist[0][0]], arglist[0][1]]

@parser.production('globals : func-declaration globals')
##@return the function_declaration code
def func_declare_in_globals(arglist):
	return [[arglist[0][0]] + arglist[1][0], arglist[0][1] + arglist[1][1]]

@parser.production('globals : declaration SEMICOLON globals')
##@return the global variable declaration
def declare_in_globals(arglist):
	return [arglist[0][0] + arglist[2][0], arglist[0][1] + arglist[1].getstr() + arglist[2][1]]

@parser.production('globals : func-declaration')
##@return function declaration code
def func_declare(arglist):
	return [[arglist[0][0]], arglist[0][1]]
@parser.production('globals : declaration SEMICOLON')
##@return the global declaration
def declare_global(argList):
	return [argList[0][0], argList[0][1] + argList[1].getstr()]

@parser.production('main : MAIN block') #block for now... will change it as we proceed
##@return the block of code in main program 
def main_p(argList):
	return [argList[1][0], argList[0].getstr() + argList[1][1]]

#########################################################################################################################


#########################################################################################################################
 												#BLOCKS AND STATEMENTS STARTS

#########################################################################################################################

# all parser rules for block
@parser.production('block : OPEN_BRACES statements CLOSE_BRACES')
##@return return the block object containing the statements 
def exec_all_statements(argList):
	"""executes all the statements inside a given block"""
	return [Block(argList[1][0]), argList[0].getstr() + argList[1][1] + argList[2].getstr()]

#########################################################################################################################
# all parser rules for statements
@parser.production('statements : statement statements')
##@return list of statements 
def multiple_statement(argList):
	return [argList[0][0] + argList[1][0], argList[0][1] + argList[1][1]]
@parser.production('statements : statement')
##@return one single statement 
def single_statement(argList):
	return [argList[0][0], argList[0][1]]

#########################################################################################################################
# all parser rules for a single statement
@parser.production('statement : block')
##@return a statement can be a block, returns the block object 
def statement_block(argList):
	return [argList[0][0], argList[0][1]]
@parser.production('statement : declaration SEMICOLON')
##@return the list of declaration objects in a statement 
def declaration_statement(argList):
	return [argList[0][0], argList[0][1] + argList[1].getstr()]
@parser.production('statement : assignment SEMICOLON')
##@return the assignment statement object 
def assignment_statement(argList):
	return [[argList[0][0]], argList[0][1] + argList[1].getstr()]
@parser.production('statement : for-block')
@parser.production('statement : while-block')
##@return the list of objects for for-loops and while-loops 
def exec_type_of_statement(argList):
	""" executes particualar type of statement"""
	return [[argList[0][0]], argList[0][1]]

@parser.production('statement : if-block elif-blocks else-block')
##@return the if statement object list when if followed by one or more elif followed by else blocks are present
def if_elifs_else(argList):
	return [[IfStatement(argList[0][0] + argList[1][0] + argList[2][0])], argList[0][1] + argList[1][1] + argList[2][1]]
@parser.production('statement : if-block elif-blocks')
##@return if statement object when if followed by elifs but no else 
def if_elifs(argList):
	return [[IfStatement(argList[0][0] + argList[1][0])], argList[0][1] + argList[1][1]]
@parser.production('statement : if-block else-block')
##@return if statement object when if followed by else 
def if_else(argList):
	return [[IfStatement(argList[0][0] + argList[1][0])], argList[0][1] + argList[1][1]]
@parser.production('statement : if-block')
##@return if statement object when only if 
def if_only(argList):
	return [[IfStatement(argList[0][0])], argList[0][1]]

@parser.production('statement : output-stream SEMICOLON')
##@return list of cout objects  
def output_stream(argList):
	snippet =  argList[0][1] + argList[1].getstr()
	return [[CoutStatement(argList[0][0], snippet)],snippet]
@parser.production('statement : input-stream SEMICOLON')
##@return list of input objects 
def input_stream(argList):
	snippet =  argList[0][1] + argList[1].getstr()
	return [[CinStatement(argList[0][0], snippet)],snippet]
@parser.production('statement : class-functions-object SEMICOLON')
##@return object representing call to a member function of a class 
def make_exec(argList):
	return [[argList[0][0]], argList[0][1] + argList[1].getstr()]

@parser.production('statement : RETURN SEMICOLON')
##@return the object 'Return' in case of void function 
def void_return(argList):
	snippet = argList[0].getstr()+" " + argList[1].getstr()
	return [[Return(String(),snippet)], snippet]

@parser.production('statement : RETURN expression SEMICOLON')
##@return the 'Return' object followed by expression 
def nonvoid_return(argList):
	snippet = argList[0].getstr() +" "+ argList[1][1]  + argList[2].getstr()
	return [[Return(argList[1][0], snippet)], snippet]

@parser.production('statement : function-call SEMICOLON')
##@return object representing call to a user defined function 
def function_call(argList):
	return [[argList[0][0]], argList[0][1] + argList[1].getstr()]
#########################################################################################################################

 												#BLOCKS AND STATEMENTS ENDS

#########################################################################################################################

#########################################################################################################################

 												#FUNCTIONS START

#########################################################################################################################
#declarations
@parser.production('func-declaration : keyword VARIABLE OPEN_PARENS CLOSE_PARENS block')
##@return functionDeclaration object of function with no parameters 
def func_declaration_to_class (argList):
	snippet = argList[0] + argList[1].getstr() + argList[2].getstr()\
	+ argList[3].getstr() + argList[4][1]
	return [FuncDeclaration(argList[1].getstr(), [], argList[4][0], snippet), snippet]

@parser.production('func-declaration : keyword VARIABLE OPEN_PARENS vars CLOSE_PARENS block')
##@return functinonDeclaration object of function with parameters 
def func_declaration_to_class (argList):
	snippet =  argList[0] + argList[1].getstr()\
	 + argList[2].getstr() + argList[3][1] + argList[4].getstr() + argList[5][1]
	return [FuncDeclaration(argList[1].getstr(), argList[3][0], argList[5][0], snippet),snippet]



@parser.production('vars : var COMMA vars')
##@return list of arguments to a function in function declaration 
def multiple_ar(argList):
	return [[argList[0][0]] + argList[2][0], argList[0][1] + argList[1].getstr() + argList[2][1]]

@parser.production('vars : var')
##@return list of a single argument in function declaration
def single_var(argList):
	return [[argList[0][0]],argList[0][1]]

@parser.production('var : keyword VARIABLE')
##@return single argument in function declaration 
def argument_variable(argList):
	return [(argList[1].getstr(), keyword_dictionary[argList[0]]), argList[0] + argList[1].getstr()]


#calls
@parser.production('function-call : VARIABLE OPEN_PARENS CLOSE_PARENS')
##@return function call to a function with no arugment 
def nonparameter_func_call(argList):
	snippet =  argList[0].getstr() + argList[1].getstr() + argList[2].getstr()
	return [FunctionCall(argList[0].getstr(), [], snippet), snippet]

@parser.production('function-call : VARIABLE OPEN_PARENS expressions CLOSE_PARENS')
##@return functino call to a function with arguments 
def parameter_func_call(argList):
	snippet = argList[0].getstr() + argList[1].getstr() + argList[2][1]\
	+ argList[3].getstr()
	return [FunctionCall(argList[0].getstr(), argList[2][0], snippet), snippet]
#########################################################################################################################

 												#FUNCTIONS ENDS

#########################################################################################################################



@parser.production('class-functions-object : class-functions')
##@return list of call to a member functions of our defined class 
def class_function_to_object(argList):
	snippet =  argList[0][1]
	if len(argList[0][0])==2:
		return [Member_function(argList[0][0], snippet), snippet]
	else:
		return [Multiple_member_function(argList[0][0], snippet), snippet]

@parser.production('class-functions : VARIABLE DOT VARIABLE OPEN_PARENS CLOSE_PARENS')
##@return call to  a single member function with no arguments
def function_call(argList):
	return [[argList[0].getstr(),argList[2].getstr()], argList[0].getstr() + argList[1].getstr() + argList[2].getstr()\
	+ argList[3].getstr() + argList[4].getstr()]

@parser.production('class-functions : VARIABLE DOT VARIABLE OPEN_PARENS expressions CLOSE_PARENS')
##@return  call to a single member function with arguments
def function_call_2(argList):
	return [[argList[0].getstr(),argList[2].getstr(),argList[4][0]], argList[0].getstr() + argList[1].getstr()\
	+ argList[2].getstr() + argList[3].getstr() + argList[4][1] + argList[5].getstr()]

@parser.production('expressions : expression COMMA expressions')
##@return list of arguements at the time of function calls 
def list_of_expression(argList):
	return [[argList[0][0]]+ argList[2][0], argList[0][1] + argList[1].getstr() + argList[2][1]]

@parser.production('expressions : expression')
##@return list of a single argument to a function call 
def list_of_expression(argList):
	return [[argList[0][0]], argList[0][1]]




#########################################################################################################################

 												#FOR-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('assignments : assignment COMMA assignments')
##@return the list of assignments in the first black of for loop
def multiple_assign(argList):
    return [[argList[0][0]] + argList[2][0], argList[0][1] + argList[1].getstr() + argList[2][1]]

@parser.production('assignments : assignment')
##@returns the list of a single assignment
def single_assign(argList):
    return [[argList[0][0]], argList[0][1]]
@parser.production('for-block : keyFOR OPEN_PARENS assignments SEMICOLON expression SEMICOLON assignment CLOSE_PARENS block')
@parser.production('for-block : keyFOR OPEN_PARENS declaration SEMICOLON expression SEMICOLON assignment CLOSE_PARENS block')
##@return for-block object containing declaration, assignment and condition 
def block_of_for(argList):
	snippet = argList[0].getstr() + argList[1].getstr()\
	+ argList[2][1] +  argList[3].getstr() + argList[4][1] + argList[5].getstr() + argList[6][1] + argList[7].getstr()\
	+ argList[8][1]
	return [ForLoop(argList[2][0], argList[4][0], argList[6][0], argList[8][0], snippet), snippet]

#########################################################################################################################

 												#FOR-BLOCK ENDS

#########################################################################################################################


#########################################################################################################################

 												#WHILE-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
@parser.production('while-block : keyWHILE OPEN_PARENS expression CLOSE_PARENS block')
##@return while-loop object containing condition
def block_of_for(argList):
	snippet = argList[0].getstr() + argList[1].getstr() + argList[2][1]\
	+ argList[3].getstr() + argList[4][1]
	return [WhileLoop(argList[2][0], argList[4][0], snippet), snippet]

#########################################################################################################################

 												#WHILE-BLOCK ENDS

#########################################################################################################################

#########################################################################################################################

 												#COUT-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
##@brief object containing expressions to be output(includes endl)
@parser.production('output-stream : keyCOUT coutopers')
def output_stream(argList):
	return [argList[1][0],argList[0].getstr() + argList[1][1]]
@parser.production('coutopers : COUTOPER ENDL coutopers')
def coutoper_endl_coutopers(argList):
	return [[String("\n")] + argList[2][0], argList[0].getstr() + argList[1].getstr() + argList[2][1]]
@parser.production('coutopers : COUTOPER expression coutopers')
def coutoper_expression_coutopers(argList):
	return [[argList[1][0]] + argList[2][0], argList[0].getstr() + argList[1][1] + argList[2][1]]
@parser.production('coutopers : COUTOPER ENDL')
def coutoper_endl(argList):
	return [[String('"\n"')], argList[0].getstr() + argList[1].getstr() ]
@parser.production('coutopers : COUTOPER expression')
def coutoper_expression(argList):
	return [[argList[1][0]], argList[0].getstr() + argList[1][1]]

#########################################################################################################################

 												#COUT-BLOCK ENDS

#########################################################################################################################

#########################################################################################################################

 												#CIN-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
##@brief list containing variables to be input
@parser.production('input-stream : keyCIN cinopers')
def input_stream(argList):
	return [argList[1][0], argList[0].getstr() + argList[1][1]]
@parser.production('cinopers : CINOPER variable cinopers')
def cinoper_expression_coutopers(argList):
	return [[argList[1][0]] + argList[2][0], argList[0].getstr() + argList[1][1] + argList[2][1]]
@parser.production('cinopers : CINOPER variable')
def cinoper_expression(argList):
	return [[argList[1][0]], argList[0].getstr() + argList[1][1]]

#########################################################################################################################

 												#CIN-BLOCK ENDS

#########################################################################################################################


#########################################################################################################################

 												#IF-BLOCK STARTS

#########################################################################################################################
# all parser rules for a if block which can either be a single statement or a block
##@brief the conditions of if-block, elif-block, else-block and their corresponding functions
@parser.production('if-block : keyIF OPEN_PARENS expression CLOSE_PARENS block')
def if_statement_runner(argList):
	return [[[argList[2][0], argList[4][0]]], argList[0].getstr() + argList[1].getstr() + argList[2][1] + argList[3].getstr()\
	+ argList[4][1]]

@parser.production('elif-blocks : elif-block elif-blocks')
def elif_blocks1(argList):
	return [argList[0][0] + argList[1][0], argList[0][1] + argList[1][1]]
@parser.production('elif-blocks : elif-block')
def elif_blocks2(argList):
	return [argList[0][0], argList[0][1]]
@parser.production('elif-block : keyELIF OPEN_PARENS expression CLOSE_PARENS block')
def elif_block(argList):
	return [[[argList[2][0], argList[4][0]]], argList[0].getstr() + argList[1].getstr() + argList[2][1] + argList[3].getstr()\
	+ argList[4][1]]
@parser.production('else-block : keyELSE block')
def else_block(argList):
	return [[[Bool(True), argList[1][0]]], argList[0].getstr() + argList[1][1]]

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
	snippet = argList[0]+" " + argList[1][1]
	for eachVar in argList[1][0]:
		if len(eachVar) == 3:
			executionList.append(ArrayDeclaration(eachVar[0], keyword_dictionary[argList[0]], eachVar[1], keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]]), snippet)) #list_variable_dict[mainIndex][eachVar[0]] = Array(keyword_dictionary[argList[0]](), eachVar[1])
		elif eachVar[1] == None:
			executionList.append(PrimitiveDeclaration(eachVar[0], keyword_dictionary[argList[0]], keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]]), snippet)) #list_variable_dict[mainIndex][eachVar[0]] = keyword_dictionary[argList[0]](keyword_default_value_dict[argList[0]])
		else:
			executionList.append(PrimitiveDeclaration(eachVar[0], keyword_dictionary[argList[0]], eachVar[1], snippet)) #list_variable_dict[mainIndex][eachVar[0]] = keyword_dictionary[argList[0]](eachVar[1])
	return [executionList, snippet]

@parser.production('declaration : LINKEDLIST LESS keyword GREATER new_variables')
@parser.production('declaration : STACK LESS keyword GREATER new_variables')
@parser.production('declaration : QUEUE LESS keyword GREATER new_variables')
@parser.production('declaration : BST LESS keyword GREATER new_variables')
def data_structure_init(argList):
	executionList=[]
	snippet = argList[0].getstr() + argList[1].getstr() + argList[2] + argList[3].getstr()+" " + argList[4][1]
	for eachVar in argList[4][0]:
		executionList.append(DataStructureDeclaration(data_struct_dictionary[argList[0].getstr()], eachVar,argList[2], snippet))
	return [executionList, snippet]

@parser.production('new_variables : VARIABLE COMMA new_variables')
def list_of_variables(argList):
	return [argList[2][0]+[argList[0].getstr()], argList[0].getstr() + argList[1].getstr() + argList[2][1]]

@parser.production('new_variables : VARIABLE')
def list_of_variables(argList):
	return [[argList[0].getstr()], argList[0].getstr()]



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
	return [argList[5][0] + [(argList[0].getstr(), argList[2][0], [])], argList[0].getstr() + argList[1].getstr() + argList[2][1]\
	+ argList[3].getstr() + argList[4].getstr() + argList[5][1]]
@parser.production('default_assigns : VARIABLE EQUAL expression COMMA default_assigns')
def default_assign_with_value(argList):
	"""appends the variable along with value in the list of default_assigns"""
	return [argList[4][0] + [(argList[0].getstr(), argList[2][0])], argList[0].getstr() + argList[1].getstr() + argList[2][1]\
	+ argList[3].getstr() + argList[4][1]]


@parser.production('default_assigns : VARIABLE COMMA default_assigns')
def default_assign_without_value(argList):
	"""appends the variable without value in the list of default_assigns"""
	return [argList[2][0] + [(argList[0].getstr(), None)],argList[0].getstr() + argList[1].getstr() + argList[2][1]]

@parser.production('default_assigns : VARIABLE OPEN_SQUARE expression CLOSE_SQUARE')
def default_assign_array(argList):
	return [[(argList[0].getstr(), argList[2][0], [])], argList[0].getstr() + argList[1].getstr() + argList[2][1]\
	 + argList[3].getstr()]

@parser.production('default_assigns : VARIABLE EQUAL expression')
def default_assign_without_value(argList):
	"""returns a list of variable with value tuple"""
	return [[(argList[0].getstr(), argList[2][0])], argList[0].getstr() + argList[1].getstr() + argList[2][1]]


@parser.production('default_assigns : VARIABLE')
def default_assign_without_value(argList):
	"""returns a list of variable without value tuple"""
	return [[(argList[0].getstr(), None)], argList[0].getstr()]




#########################################################################################################################

 												#DECLARATION ENDS

#########################################################################################################################




#########################################################################################################################

 												#ASSIGNMENT STARTS

#########################################################################################################################
#########################################################################################################################
# all parser rules for assignment
##@brief all assignment rules return a Assignement object
# +=, -= etc. symbols are incorporated
@parser.production('assignment : variable EQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [Assignment(argList[0][0],argList[2][0], snippet), snippet]

@parser.production('assignment : variable PLUSEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr()\
	 + argList[2][1]
	return [Assignment(argList[0][0],BinaryOp(myAdd, argList[0][0], argList[2][0], "should not be accessed"), snippet), snippet]

@parser.production('assignment : variable MINUSEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr()\
	 + argList[2][1]
	return [Assignment(argList[0][0],BinaryOp(mySub, argList[0][0], argList[2][0], "should not be accessed"), snippet), snippet]

@parser.production('assignment : variable MULTEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr()\
	 + argList[2][1]
	return [Assignment(argList[0][0],BinaryOp(myMult, argList[0][0], argList[2][0], "should not be accessed"), snippet), snippet]

@parser.production('assignment : variable DIVEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr()\
	 + argList[2][1]
	return [Assignment(argList[0][0],BinaryOp(myDiv, argList[0][0], argList[2][0], "should not be accessed"), snippet), snippet]

@parser.production('assignment : variable MODEQUAL expression')
def assign_variable(argList):
	#if argList[0]
	snippet = argList[0][1] + argList[1].getstr()\
	 + argList[2][1]
	return [Assignment(argList[0][0],BinaryOp(myMod, argList[0][0], argList[2][0], "should not be accessed"), snippet), snippet]

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
##@return BinaryOp object with the first argument as the corresponding operator 
def simplex_isequal_simplex(argList):
	snippet =  argList[0][1]\
	 + argList[1].getstr() + argList[2][1]
	return [BinaryOp(oper_to_funcname_dict[argList[1].getstr()], argList[0][0], argList[2][0], snippet), snippet]



@parser.production('expression : simplex')
##@return  just the object for a simple expression
def simplex_to_expression(argList):
	return [argList[0][0], argList[0][1]]


#########################################################################################################################
# all parser rules for Simple Expression
##@brief these are the rules for defining simple expressions considering both unary and binary operators
@parser.production('simplex :  PLUS simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]\
	 + argList[2].getstr() + argList[3][1]
	return [BinaryOp(myAdd, UnaryOp(myPlus, argList[1][0], "should not be printed"), argList[3][0], snippet), snippet]

@parser.production('simplex :  PLUS simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]\
	 + argList[2].getstr() + argList[3][1]
	return [BinaryOp(mySub, UnaryOp(myPlus, argList[1][0], "should not be printed"), argList[3][0], snippet), snippet]

@parser.production('simplex :  MINUS simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]\
	 + argList[2].getstr() + argList[3][1]
	return [BinaryOp(myAdd, UnaryOp(myMinus, argList[1][0], "should not be printed"), argList[3][0], snippet), snippet]

@parser.production('simplex :  MINUS simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]\
	 + argList[2].getstr() + argList[3][1]
	return [BinaryOp(mySub, UnaryOp(myMinus, argList[1][0], "should not be printed"), argList[3][0], snippet), snippet]
	
@parser.production('simplex : simplex PLUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [BinaryOp(myAdd, argList[0][0], argList[2][0],snippet), snippet]

@parser.production('simplex : simplex MINUS term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [BinaryOp(mySub, argList[0][0], argList[2][0],snippet), snippet]

@parser.production('simplex :  simplex OR term')
def plus_term_plus_term_to_simplex(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [BinaryOp(myOr, argList[0][0], argList[2][0],snippet),snippet ]

@parser.production('simplex :  PLUS term')
def plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]
	return [UnaryOp(myPlus, argList[1][0],snippet), snippet]

@parser.production('simplex :  MINUS term')
def plus_term_to_simplex(argList):
	snippet = argList[0].getstr() + argList[1][1]
	return [UnaryOp(myMinus, argList[1][0],snippet), snippet]


@parser.production('simplex : term')
def plus_term_to_simplex(argList):
	return [argList[0][0], argList[0][1]]
#########################################################################################################################
# all parser rules for term
##@brief these are the rules for 'term' which is used in defining simple expressions 
@parser.production('term : term MUL factor')
@parser.production('term : term DIV factor')
def factor_mul_to_term(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	if argList[1].getstr() == '*':
		return [BinaryOp(myMult, argList[0][0], argList[2][0],snippet), snippet]
	else:
		return [BinaryOp(myDiv, argList[0][0], argList[2][0],snippet), snippet]

@parser.production('term : term MOD factor')
def factor_mod_to_term(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [BinaryOp(myMod, argList[0][0], argList[2][0], snippet), snippet]

@parser.production('term : term AND factor')
def factor_and_to_term(argList):
	snippet = argList[0][1] + argList[1].getstr() + argList[2][1]
	return [BinaryOp(myAnd, argList[0][0], argList[2][0], snippet), snippet]

@parser.production('term : factor')
def factor_to_term(argList):
	return [argList[0][0],argList[0][1]]


#########################################################################################################################
# all parser rules for factor
##brief these are the rules for defining 'factor' which is used in definition of term	
@parser.production('factor : variable')
def variable_to_factor(argList):
	return [argList[0][0], argList[0][1]]

@parser.production('factor : class-functions-object')
@parser.production('factor : function-call')
def classFuncobject_to_expression(argList):
	return [argList[0][0], argList[0][1]] #need to check whether working properly

@parser.production('factor : INT')
def int_to_factor(argList):
	return [Int(int(argList[0].getstr())), argList[0].getstr()]

@parser.production('factor : FLOAT')
def float_to_factor(argList):
	return [Float(float(argList[0].getstr())),argList[0].getstr()]

@parser.production('factor : STRING')
def string_to_factor(argList):
	return [String(argList[0].getstr()), argList[0].getstr()]

@parser.production('factor : BOOL')
def bool_to_factor(argList):
	if argList[0].getstr() == 'true':
		return [Bool(True), argList[0].getstr()]
	return [Bool(False), argList[0].getstr()]

@parser.production('factor : NOT factor')
def notfactor_to_factor(argList):
	snippet = argList[0].getstr() + argList[1][1]
	return [UnaryOp(myNot,argList[1][0], snippet), snippet]

@parser.production('factor : OPEN_PARENS expression CLOSE_PARENS')

def paren_expression_to_factor(argList):
	return [argList[1][0], argList[0].getstr() + argList[1][1] + argList[2].getstr()]


#########################################################################################################################

 												#EXPRESSION ENDS

#########################################################################################################################



#########################################################################################################################

 												#VARIABLE STARTS

#########################################################################################################################


#all parser rules for variables:: still not used mostly

#@parser.production('variable : variable OPEN_SQUARE expression CLOSE_SQUARE')
#def search_array_varialbe(argList):
##@brief rule for variable which is an element of an array
@parser.production('variable : VARIABLE OPEN_SQUARE expression CLOSE_SQUARE')
def search_array_variable(argList):
	""" searches for the array element at the given index"""
	result = argList[2][0]	
	y = argList[0].getstr() + argList[1].getstr() + argList[2][1] + argList[3].getstr()
	return [ArrayVariable(argList[0].getstr(), result, y), y]

@parser.production('variable : VARIABLE')
##@brief rules for defining a normal varialble
def search_variable(argList):
	"""searches for the variable in the variable dictionary and if found
		return the corresponding object"""
	var_name = argList[0].getstr()
	return [Variable(var_name), var_name]
	#return [var_name, list_variable_dict[mainIndex][var_name]] #one


#########################################################################################################################

 												#VARIABLE ENDS

#########################################################################################################################




#########################################################################################################################

 												#ERROR HANDLER

@parser.error
##@the error handler
#this gets calles whenever any error occurs in parsing
# @param token the token at which error has occurred
# @return raises an ValueError
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

#########################################################################################################################

#########################################################################################################################

## the file to be interpreted has to be given as the first command line argument
fileName = sys.argv[1]
file = open(fileName,'r')
initial = ""
for chunk in file:
	initial += chunk
file.close()
##@brief the build method of ParserGenerator class is called to parse the given code and produce output
mainparser = parser.build()
##@brief the parsed statement returns a list of executables which are then executed
for item in mainparser.parse(lexer.lex(initial)):
	item.exec()
