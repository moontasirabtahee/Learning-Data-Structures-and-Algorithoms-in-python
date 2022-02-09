# Created by Moontasir Abtahee at 2/9/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.stack = []
    def push(self,data):
        if self.head is None:
            self.head = Node(data)

        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            return value

    def headCheck(self):
        return self.head

def checkParentheses(expre):
    st = Stack()
    flag = False
    index = 0
    closed = ""
    for i in expre:
        index += 1
        if i == "(" or i == "{" or i == "[":
            st.push(i)
        elif i == ")" or i == "}" or i == "]":
            closed = i
            peekValue = st.peek()
            if peekValue == None:
                flag = False
                break
            if i == ")":
                if peekValue == "(":
                    st.pop()
                    flag = True
                else:
                    flag = False
                    break

            elif i == "}":
                if peekValue == "{":
                    st.pop()
                    flag = True
                else:
                    flag = False
                    break

            elif i == "]":
                if peekValue == "[":
                    st.pop()
                    flag = True
                else:
                    flag = False
                    break

    if flag == True and st.headCheck() is None:
        print("This expression is correct.")
    elif flag == False and st.headCheck() is not None:
        print(f"""This expression is NOT correct.
Error at character # {st.head.data}- not closed.""")
    else:
        print(f"""This expression is NOT correct.
Error at character #.{closed}- not opened.""")


checkParentheses("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
