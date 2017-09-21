from lexer import lexer
from parserClasses import *
from rply import ParserGenerator
initial = input("Enter the code\n")
parser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['INT', 'PLUS'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[]
)

oper_to_funcname_dict = {'==': myIsEqual, '-' : myIsNotEqual,\
                         '>=': myGreaterThanEqualTo, '<':myLessThan,\
                         '>':myGreaterThan, '<=': myLessThanEqualTo}

@parser.production('expression : simplex ISEQUAL simplex')
@parser.production('expression : simplex NOTEQUAL simplex')
@parser.production('expression : simplex GREATER simplex')
@parser.production('expression : simplex GREATEREQUAL simplex')
@parser.production('expression : simplex LESS simplex')
@parser.production('expression : simplex LESSEQUAL simplex')

def expression_symb_expression(p):
	#p is the list of all tokens matched
	"""to handle the case of expression followed by an expression"""
	BinOp = BinaryOp(oper_to_funcname_dict[p[1].getstr()])
	print(p[0])
	print(p[2])


@parser.production('simplex : INT')

mainparser = parser.build()
print(mainparser.parse(lexer.lex(initial)))