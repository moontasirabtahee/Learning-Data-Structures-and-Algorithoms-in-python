# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            # counter = self.head
            # while counter.next is not None:
            #     counter = counter.next
            #
            # counter.next = node
            # node.prev = counter
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def print(self):
        if self.head is None:
            print("02. Linked List is Empty")
            return
        else:
            counter = self.head
            while counter is not None:
                print(counter.data ,end=" ==> ")
                counter = counter.next

    def length(self):
        length = 0
        counter = self.head
        while counter is not None:
            length += 1
            counter = counter.next
        return length

    def backward_print(self):
        counter = self.tail
        while counter is not None:
            print(counter.data, end=" <== ")
            counter = counter.prev


    def insert(self,index, data):
        if index<0 and index>=self.length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_beginning(data)

        else:
            index_counter = 0
            counter = self.head
            while counter is not None:
                if index_counter == index-1:
                    node = Node(data,counter.next,counter)

                    counter.next.prev = node
                    counter.next = node
                counter = counter.next
                index_counter += 1

    def remove(self,index):
        if index<0 and index>=self.length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            index_counter = 0
            counter = self.head
            while counter is not None:
                if index_counter == index-1:
                    counter.next = counter.next.next
                    counter.next.prev = counter

                counter = counter.next
                index_counter += 1

    def insert_values(self,list):
        self.head = None
        self.tail = None
        for i in list:
            node = Node(i)
            if self.head is None:
                self.head =node
                self.tail =node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node



    def insert_after_value(self, data_after, data_to_insert):
# Search for first occurance of data_after value in linked list
# Now insert data_to_insert after data_after node
        counter = self.head
        while counter:
            if data_after == counter.data:
                node = Node(data_to_insert,counter.next,counter)
                counter.next.prev = node
                counter.next = node

                break
            counter =counter.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next

            del temp
            return

        if self.tail.data == data:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
        else:
            counter = self.head
            while counter is not None:
                if counter.data == data:
                    next_v=counter.next
                    prev_v = counter.prev
                    next_v.prev = prev_v
                    prev_v.next = next_v
                    break
                counter = counter.next




# Remove first node that contains data\

ll = Linkedlist()
ll.insert_at_end("Second Value")
ll.insert_at_beginning("First Value")
ll.insert_at_end("Third Value")
ll.print()
print()
x = ll.length()
print(x)
ll.backward_print()
ll.insert(2,"Inserted Value")
ll.insert(3,"Three")
ll.insert(0,"FIRST lol")
print()
ll.print()
print()
ll.backward_print()
print()
ll.remove(0)
ll.remove(2)
ll.remove(2)
ll.print()
print()
ll.insert_values([1,2,3,4,5,6,7,8,9])
print()

ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
print()
ll.backward_print()
print()
ll.insert_values(["banana","mango","grapes","orange"])
print()
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
print()
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
print("------")
ll.print()
print()
ll.backward_print()
ll.remove_by_value("figs")
print()
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")

ll.remove_by_value("grapes")
print()
ll.print()