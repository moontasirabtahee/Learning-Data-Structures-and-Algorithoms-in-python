# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Stack:
    size = 0
    def __init__(self):
        self.stackList = []
        print("This is a 03. Stack data Structure implemented with List")
        print("This class have 4 method\n1.push\n2.pop\n3.peek\n4.isempty")

    def push(self,data):
        self.stackList.append(data)
        Stack.size += 1

    def pop(self):
        removed = self.stackList[-1]
        self.stackList = self.stackList[:-1]
        Stack.size -= 1
        return removed

    def peek(self):
        print(self.stackList[-1])

    def isempty(self):
        if len(self.stackList) == 0:
            return True
        return False

    def __size(self):
        return Stack.size

tester = Stack()
tester.push(10)
tester.push(20)
tester.push(30)
tester.push(40)
tester.push(50)
tester.push(60)
tester.peek()
print(tester.pop())
print(tester.pop())
print(tester.pop())
print(tester.pop())
print(tester.pop())
print(tester.pop())
print(tester.isempty())
