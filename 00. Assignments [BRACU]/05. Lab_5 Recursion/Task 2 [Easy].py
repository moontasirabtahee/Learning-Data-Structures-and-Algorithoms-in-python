# Created by Moontasir Abtahee at 2/21/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here


#a)Implement a recursive algorithm that takes a decimal number n and converts n to its corresponding (you may return as a string) binary number.
def dec_bin(num,str=""):
    if num == 0:
        if str == "":
            return 0
        else:
            return str

    if num%2 == 0:
        str = "0"+str
        return dec_bin(num//2,str)
    else:
        str = "1" + str
        return dec_bin(num // 2, str)


print(dec_bin(990))


class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class MyList:
    def __init__(self,a = None):
        self.Head = None
        if a:
            self.array2List(a)


    def array2List(self,a):
        tail = self.Head
        for i in a:
            node = Node(i)
            if self.Head is None:
                self.Head = node
                tail = self.Head
            else:
                tail.next = node
                tail = node

        return self.Head

def AddAll(Head,sum = 0):
    if Head is None:
        return sum
    return AddAll(Head.next,sum+Head.data)


def printall(Head):
    if Head is None:
        return
    else:
        printall(Head.next)
        print(Head.data,end="==>")
        return
ll = MyList([1,2,3,4,5,6,7,8,9,11])
print(AddAll(ll.Head))

print(printall(ll.Head))