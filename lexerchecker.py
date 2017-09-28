from lexer import lexer

initial = input("give me the input\n")
stream = lexer.lex(initial)
while(True):
	try:
		print(stream.next())
	except:
		print("done")
		break