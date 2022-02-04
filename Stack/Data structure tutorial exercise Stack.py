# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.

class Stack:
    size = 0
    def __init__(self):
        self.stackList = []
        print("This is a Stack data Structure implemented with List")
        print("This class have 4 method\n1.push\n2.pop\n3.peek\n4.isempty")

    def push(self,data):
        self.stackList.append(data)


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



def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    rstr = ''
    while not stack.isempty():
        rstr += stack.pop()

    return rstr

print(reverse_string("We will conquere COVI-19"))