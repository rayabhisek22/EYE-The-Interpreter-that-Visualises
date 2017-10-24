from HashTable import *

l = HashTable(29, 100, 100, 10, "My hash")
for i in range(1, 16):
	l.push(i*490)
print(l.find(49))