# Created by Moontasir Abtahee at 2/9/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        return None
    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp



def checkParentheses(exp):
    st = Stack()
    flag = False
    idx = 0
    closed = ""
    for i in exp:
        idx += 1
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

    if flag == True and (len(st.stack)) == 0:
            print("This expression is correct")
            return
    elif flag == False and st.peek() != None:
        print(f"""This expression is NOT correct.
Error at character # {st.peek()}- not closed.""")
    else:
        print(f"""This expression is NOT correct.
Error at character #.{closed}- not opened.""")


checkParentheses("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")