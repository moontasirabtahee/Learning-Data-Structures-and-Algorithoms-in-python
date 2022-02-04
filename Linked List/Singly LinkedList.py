# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node

        else:
            # counter = self.head
            # while counter.next is not None:
            #     counter = counter.next
            # counter.next = node
            node.next = self.head
            self.head = node

    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node

        else:
            counter = self.head
            while counter.next is not None:
                counter = counter.next
            counter.next = node


    def insert(self,data,index):
        if index == 0:
            self.add_begin(data)

        else:
            indexCounter = 0
            counter = self.head
            while counter is not None:
                if indexCounter == index-1:
                    break
                else:
                    counter = counter.next
                    indexCounter+=1

            if counter is not None:
                node = Node(data)
                node.next = counter.next
                counter.next = node
            else:
                print("index not Found! Added at the end")
                self.add_end(data)


    def remove_begin(self):
        if self.head is None:
            print("ERROR!! Empty Singly Linked List")
        else:
            self.head = self.head.next
    def remove_end(self):
        counter = self.head
        if counter is not  None:
            while counter.next is not None:
                if counter.next.next is None:
                    break
                else:
                    counter = counter.next
            if counter is not  None:
                counter.next = None

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
            counter.next = counter.next.next


    def clear(self):
        self.head = None
        return self.head
    def view(self):
        counter = self.head
        if counter is not None:
            while counter is not None:
                print(counter.data,end="-->")
                counter = counter.next
            print()
        else:
            print("Empty Linked List")





tester = SinglyLinkedList()
tester.add_end(122)
tester.add_begin(100)
tester.insert(111,1)
tester.add_end(1000)
tester.add_begin(1000)
tester.view()
tester.remove_begin()
tester.view()
tester.remove_index(1)
tester.remove_end()
tester.view()
tester.clear()
tester.view()