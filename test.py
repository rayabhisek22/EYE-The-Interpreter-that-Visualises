from lexer import lexer

a = lexer.lex("bool a = true")
while(True):
	print(a.next())