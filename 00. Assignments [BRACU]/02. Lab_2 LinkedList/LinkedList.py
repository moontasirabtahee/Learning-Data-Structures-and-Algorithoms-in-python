# Created by Moontasir Abtahee at 2/9/2022
# Feature: #BRAC UNIVERSITY
# Scenario: # CSE220 Lab Assignment

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class MyList:
    Head = None
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



    def showList(self):

        if self.Head == None:
            print("Empty LinkedList")
        else:
            tail = self.Head
            while tail is not None:
                print(tail.data,end="===>")
                tail = tail.next
            print()
    def isEmpty(self):
        if self.Head:
            return False
        return True


    def  clear(self):
        self.Head = None
        print("LinkedList Cleared")

    def insert(self,elem,index = None):
        if self.existanceChecker(elem):
            print("The Key already Exist")
        else:

            if index is None:
                tail = self.Head
                while tail.next is not None:
                    tail = tail.next

                node = Node(elem)
                tail.next = node
                tail=node

            else:
                if index==0:
                    node = Node(elem,self.Head)
                    self.Head = node
                else:
                    tail = self.Head
                    counter = 0
                    while tail is not None:
                        if counter == index-1:
                            break
                        else:
                            counter += 1
                            tail = tail.next


                    node = Node(elem)
                    node.next = tail.next
                    tail.next = node

    def existanceChecker(self,elem):
        tail = self.Head
        while tail:
            if tail.data == elem:
                return True
            tail = tail.next
        return False
    def length(self):
        counter = 0
        if self.Head is None:
            return 0
        else:
            tail = self.Head
            while tail:
                counter += 1
                tail = tail.next

        return counter


    def remove(self,key):
        tail = self.Head
        prev, temp = None,None
        if tail is None:
            print("Empty List")
        else:
            if self.Head.data == key:
                self.Head = self.Head.next
                return
            else:
                while tail:
                    if tail.data == key:
                        temp = tail.data
                        break
                    prev = tail
                    tail = tail.next

            prev.next = tail.next

            return temp



    #"------------------------------------------------------------------------------------------------" \
    def even_number(self):
        newHead = None
        newTail = None
        tail = self.Head
        while tail:

            if tail.data%2 == 0:

                node = Node(tail.data)
                if newHead is None:
                    newHead = node
                    newTail = newHead

                else:
                    newTail.next = node
                    newTail = node
            tail = tail.next


        return newHead

    def printByHead(self,Head):
        if Head == None:
            print("Empty LinkedList")
        else:
            tail = Head
            while tail is not None:
                print(tail.data, end="===>")
                tail = tail.next
            print()
    def search(self,data):
        tail = self.Head
        while tail:

            if tail.data == data:
                return True

            tail = tail.next

        return False

    def reverse(self):
        newHead = None
        tail = self.Head
        while tail:
            next = tail.next
            tail.next = newHead
            newHead = tail
            tail = next
        self.Head = newHead


    def sort(self):
        tail = self.Head
        i = None
        if tail is None:
            print("Empty LinkedList")
        else:
            while tail is not None:
                i = tail.next
                while i is not None:
                    if tail.data>i.data:
                        tail.data,i.data = i.data,tail.data
                    i = i.next
                tail = tail.next



    def sum(self):
        total = 0
        tail = self.Head
        while tail:
            total += tail.data
            tail = tail.next

        return total





ll = MyList([1,2,3,4,5,6,7,8,9,10])
ll.showList()
ll2 = MyList()
print(ll.isEmpty())
ll.remove(7)
ll.showList()
print(ll.length())
print(ll.existanceChecker(7))
ll.insert(999)
ll.insert(96,0)
ll.showList()
ll.insert(898,6)
ll.insert(7423,12)
ll.showList()
print(ll.length())

ll.printByHead(ll.even_number())

print(ll.search(999))
ll.reverse()
ll.showList()
ll.sort()
ll.showList()
print(ll.sum())

