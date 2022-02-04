# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def view(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            counter = self.head
            while counter.next is not self.head:
                print(counter.data,end="-->")
                counter =counter.next
            print(counter.data)


    def add_begin(self, data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.head.next = self.head

        else:

            node.next=self.head
            counter = self.head
            while counter.next is not self.head:
                counter =counter.next
            counter.next = node
            self.head = node


    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.head.next = self.head

        else:
            counter = self.head
            while counter.next is not self.head:
                counter = counter.next
            counter.next = node
            node.next = self.head


    def insert(self,data,index):
        if index == 0:
            self.add_begin(data)

        else:
            indexCounter = 0
            counter = self.head
            while counter.next is not self.head:
                if indexCounter == index-1:
                    break
                else:
                    print("x")
                    counter = counter.next
                    indexCounter+=1
            if indexCounter == 0:
                node = Node(data)
                node.next = self.head.next
                self.head.next = node
            elif counter is not self.head:
                node = Node(data)
                node.next = counter.next
                counter.next = node
            else:
                print(indexCounter)
                print("index not Found! Added at the end")
                self.add_end(data)

    def remove_begin(self):
        if self.head is None:
            print("ERROR!! Empty Singly 02. Linked List")
        else:
            counter = self.head
            while counter.next is not self.head:
                counter = counter.next
            counter.next = self.head.next
            self.head = self.head.next

    def remove_end(self):
        counter=self.head
        if counter.next is not self.head:
            while counter.next is not self.head:
                if counter.next.next is self.head:
                    break
                else:
                    counter=counter.next
            if counter is not self.head:
                counter.next=self.head

        else:
            print("Empty LinkedList")

    def remove_index(self,index):
        indexCounter=0
        counter=self.head
        while counter.next is not self.head:
            if indexCounter == index-1:
                break
            else:
                counter=counter.next
                indexCounter+=1

        if indexCounter == 0:
            self.head.next = self.head.next.next
        elif counter is self.head:
            print("Index Does Not Exist")
        else:
            counter.next = counter.next.next


    def clear(self):
        self.head = None
        return self.head



tester = CircularLinkedList()

tester.add_begin(100)
tester.insert(111,1)

tester.add_end(122)
tester.add_end(1000)
tester.add_begin(1000)
tester.insert(500,5)
tester.view()
tester.remove_begin()
tester.view()
tester.remove_index(1)
tester.remove_end()
tester.view()
tester.clear()
tester.view()
