from lexer import lexer
import sys

lines = []
for line in sys.stdin:
    lines.append(line)
initial = ''.join(lines)
del lines

stream = lexer.lex(initial)
while(True):
	try:
		print(stream.next())
	except:
		print("done")
		break