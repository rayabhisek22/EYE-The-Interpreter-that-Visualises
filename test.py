from lexer import lexer

a = lexer.lex("""string x="aman"  + "fool"; """)
while(True):
	print(a.next())