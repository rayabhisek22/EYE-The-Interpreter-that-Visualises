from Queue import Queue
from SinglyLinkedList import SinglyLinkedList
from Stack import Stack
from headersForDataStructures import wait
from BinarySearchTree import BinarySearchTree


a = BinarySearchTree(300, 300, 10, "MyBinaryTree")
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(5)
a.insert(14)
#a.search(14)
#a.search(31)
#a.erase(110)
a.erase(5)


for i in range(100):
	wait()




"""
a = Queue(1000, 300, 10, "myQueue")
a.pushFront(10)
print(a.head.data, a.tail.data)
a.pushFront(100)
print(a.head.data, a.tail.data)
a.pushFront(20)
print(a.head.data, a.tail.data)
print(a.popFront())
print(a.head.data, a.tail.data)
print(a.popBack())
print(a.head.data, a.tail.data)
print(a.popFront())
print(a.head.data, a.tail.data)
"""

"""
a = Stack(500, 500, 10, "myStack")
a.push(40)
a.push(100)
a.top()
a.pop()
a.pop()
"""
for i in range(2):
	wait()
"""
a = SinglyLinkedList(1000, 100, 10)
a.insert(0,9)
a.insert(0,10)
a.insert(0,13)
a.insert(0, 20)
print (a.get(10))
#print(a.indexOf(20))
a.erase(9)
a.insert(2, 1)
b = input()"""