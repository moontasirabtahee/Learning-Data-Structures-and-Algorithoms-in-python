# Created by Moontasir Abtahee at 2/9/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class Node:
    def __init__(self, data, next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyList:
    def __init__(self,a):
        self.head = Node(None)
        tail = None
        if self.uniqueTester(a):
            for i in a:
                node = Node(i)
                if self.head.next is None:
                    self.head.next = node
                    self.head.prev = node
                    node.next =self.head
                    node.prev = self.head
                    tail = node

                else:
                    node.prev = tail
                    node.next = tail.next
                    self.head.prev = node
                    tail.next = node
                    tail = node

    def showList(self):
        if self.head.next is None:
            print("Empty LinkedList")
        else:
            tail = self.head.next
            while tail is not self.head:
                print(tail.data,end= "==>")
                tail = tail.next
            print()
            tail = self.head
            while tail.prev is not self.head:
                print(tail.prev.data,end="<==")
                tail = tail.prev
            print()
    def uniqueTester(self,a):
        for i in a:
            if a.count(i)>1:
                return False
        return True

    def existanceChecker(self,elem):
        tail = self.head.next
        while tail is not self.head:
            if tail.data == elem:
                return True
            tail = tail.next
        return False

    def insert(self,elem,index = None):
        if index is None:
            if self.existanceChecker(elem):
                print("Key already exist")
            else:
                tail = self.head.next
                while tail.next is not self.head:
                    tail = tail.next

                node = Node(elem)
                node.next = self.head
                node.prev = tail
                tail.next = node
                self.head.prev = node


        else:
            idx = 0
            tail = self.head.next
            while tail.next is not self.head:

                if idx == index-1:
                    break
                idx += 1
                tail = tail.next

            node = Node(elem)
            node.next = tail.next
            node.prev = tail
            tail.next = node
            tail.next.prev = node

    def remove(self,index):
        idx = 0
        tail = self.head.next
        while tail.next is not self.head:

            if idx == index - 1:
                break
            idx += 1
            tail = tail.next

        tail.next = tail.next.next
        tail.next.prev = tail

    def removeKey(self,key):
        prev = None
        tail = self.head.next
        while tail is not self.head:
            if tail.data == key:
                break
            prev = tail
            tail = tail.next

        prev.next = tail.next
        tail.next.prev = prev

ll = DoublyList([1,2,3,4,5,6,7,8,9,10])
ll.showList()
print("---------------------------------------------------")
ll.insert(999)
ll.showList()
ll.insert(876,5)
ll.showList()
ll.remove(5)
ll.showList()
ll.removeKey(999)
ll.showList()
