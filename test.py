from lexer import lexer

a = lexer.lex("true")
while(True):
	print(a.next())