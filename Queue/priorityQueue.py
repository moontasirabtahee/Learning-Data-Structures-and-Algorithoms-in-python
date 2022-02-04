# Created by Moontasir Abtahee at 2/4/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
class priorityQueue:
    maxSize = 0
    size = 0
    def __init__(self,maxSize = 5):
        print("This is Priority Queue Class")
        print("This class have 4 method\n1.enqueue\n2.dequeue\n3.isfull\n4.isempty")
        priorityQueue.maxSize = maxSize
        self.queueList = list()

    def enqueue(self,data,priority):
        if priorityQueue.size == priorityQueue.maxSize:
            print(priorityQueue.size)
            print("###Queue is full",data,'can not be in this Queue###')
        else:
            x=(priority, data)
            self.queueList.append(x)
            priorityQueue.size += 1



    def dequeue(self):
        if self.isempty():
            return("NO ELEMENT in the Queue")
        else:
            max = 0
            for i in range(len(self.queueList)):
                if self.queueList[i][0] > self.queueList[max][0]:
                    max = i

            removed = self.queueList[max]
            self.queueList = self.queueList[:max]+self.queueList[max+1:]
            return removed[1]

    def isempty(self):
        return not self.queueList

    def isfull(self):
        if priorityQueue.size == priorityQueue.maxSize:
            print("This Queue is full")
        else:
            x = priorityQueue.maxSize - priorityQueue.size
            print("This Queue is not Full")
            print(f"You have {x} space(s)")


tester = priorityQueue()
tester.enqueue(10,3)
tester.enqueue(20,0)
tester.enqueue(30,5)
tester.enqueue(40,10)
print(tester.isempty())
tester.enqueue(50,3)
tester.enqueue(60,1)
tester.isfull()
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.dequeue())
print(tester.isempty())

