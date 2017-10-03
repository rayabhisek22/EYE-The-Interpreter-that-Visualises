from lexer import lexer

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
stream = lexer.lex(initial)
while(True):
	try:
		print(stream.next())
	except:
		print("done")
		break