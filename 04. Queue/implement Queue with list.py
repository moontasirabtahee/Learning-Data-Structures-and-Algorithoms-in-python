# Created by Moontasir Abtahee at 2/4/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
class Queue:
    maxsize = 0
    size = 0
    def __init__(self,maxsize = 5):
        print("This is a queue implemented with List.")
        print("This class have 4 method\n1.enqueue\n2.dequeue\n3.isfull\n4.isempty")
        Queue.maxsize = maxsize
        self.queueList = list()
    def enqueue(self,data):
        if Queue.size == Queue.maxsize:
            print("###04. Queue is full",data,'can not be in this 04. Queue###')
        else:
            self.queueList.append(data)
            Queue.size += 1
    def dequeue(self):
        if self.isempty():
            return("NO ELEMENT in the 04. Queue")
        else:
            removed = self.queueList[0]
            self.queueList = self.queueList[1:]
            self.size -=1
            return removed

    def isfull(self):
        if Queue.size == Queue.maxsize:
            print("This 04. Queue is full")
        else:
            x = Queue.maxsize - Queue.size
            print("This 04. Queue is not Full")
            print(f"You have {x} space(s)")

    def isempty(self):
        return not self.queueList



tester = Queue()
tester.enqueue(10)
tester.enqueue(20)
tester.enqueue(30)
tester.enqueue(40)
print(tester.isempty())
tester.enqueue(50)
tester.enqueue(60)
tester.isfull()
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.isempty())
