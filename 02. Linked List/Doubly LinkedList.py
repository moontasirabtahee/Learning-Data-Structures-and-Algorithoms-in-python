# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Node:
    def __init__(self,data,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self,head = None):
        self.head = head

    def add_begin(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def add_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            counter = self.head
            while counter.next is not None:
                counter = counter.next

            counter.next = node
            node.prev = counter


    def insert(self,data,index):
        if index == 0:
            self.add_begin(data)

        else:
            node=Node(data)
            indexCounter = 0
            counter = self.head
            while counter is not None:
                if indexCounter == index-1:
                    break
                else:
                    counter = counter.next
                    indexCounter+=1
            if counter is not None:
                node.prev = counter
                node.next = counter.next
                counter.next.prev = node
                counter.next = node
            else:
                print("index not Found, added at end")
                self.add_end(data)

    def remove_begin(self):
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None

        else:
            print("Empty LinkedList")

    def remove_end(self):
        counter=self.head
        if counter is not None:
            while counter.next is not None:
                if counter.next.next is None:
                    break
                else:
                    counter=counter.next
            if counter is not None:
                counter.next=None
        else:
            print("Empty LinkedList")

    def remove_index(self,index):
        indexCounter=0
        counter=self.head
        while counter is not None:
            if indexCounter == index-1:
                break
            else:
                counter=counter.next
                indexCounter+=1

        if counter is None:
            print("Index Does Not Exist")
        else:
            counter.next.prev = counter
            counter.next=counter.next.next


    def view(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            counter = self.head
            print("Frontend", end="===>")
            while counter is not None:
                print(counter.data,end='-->')
                counter = counter.next
            counter = self.head
            print()
            while counter.next is not None:
                counter = counter.next
            print("Backend", end="===>")
            while counter is not None:

                print(counter.data, end='-->')
                counter=counter.prev
            print()
    def clear(self):
        self.head = None
        return self.head


tester = DoublyLinkedList()
tester.add_begin(111)
tester.view()
tester.add_begin(1000)
tester.view()
tester.add_end(222)
tester.add_end(1000)
tester.view()
tester.insert(555,2)
tester.view()
tester.remove_begin()
tester.view()
tester.insert("Error",652659)
tester.view()
tester.remove_end()
tester.remove_end()
tester.view()
tester.remove_index(2)
tester.view()
tester.clear()
tester.view()