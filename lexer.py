from rply import LexerGenerator
lg = LexerGenerator()
lg.ignore(r'\s+')
lg.ignore(r'\n+')
lg.add('COMMA', r",")
lg.add('SEMICOLON',r";")
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OR', r'\|\|')
lg.add('AND', r'&&')
lg.add('ISEQUAL', r"==")
lg.add('NOTEQUAL',r'!=')
lg.add('MOD', r'%')
lg.add('NOT', r'!')
lg.add('LESSEQUAL', r'<=')
lg.add('GREATEREQUAL', r'>=')
lg.add('LESS', r'<')
lg.add('GREATER', r'>')
lg.add('EQUAL',r'=')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('OPEN_BRACES', r'\{')
lg.add('CLOSE_BRACES', r'\}')
lg.add('OPEN_SQUARE', r'\[')
lg.add('CLOSE_SQUARE', r'\]')
lg.add('keyINT', r'int')
lg.add('keyINT', r'long')
lg.add('keyINT', r'long\ int')
lg.add('keyINT', r'long\ long')
lg.add('keyINT', r'long\ long\ int')
lg.add('keyINT', r'unsigned\ int')
lg.add('keyFLOAT', r'float')
lg.add('keyFLOAT', r'double')
lg.add('keySTRING', r'string')
lg.add('keyBOOL', r"bool")
lg.add('keySTRING', r'string')
lg.add('keyIF', r"if")
lg.add('keyFOR', r"for")
lg.add('keyWHILE', r"while")
lg.add('FLOAT', r'[0-9]*\.[0-9][0-9]*')
lg.add('INT', r'[0-9][0-9]*')
lg.add('STRING', r'"[^"]*"')
lg.add('CHAR', r"'.'")
lg.add('BOOL', r"true")
lg.add('BOOL', r"false")
lg.add('VARIABLE' , r'[a-zA-Z][0-9a-zA-Z_]*')
lexer = lg.build()

