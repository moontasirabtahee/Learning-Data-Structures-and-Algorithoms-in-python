# Created by Moontasir Abtahee at 2/4/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Design a food ordering system where your python program will run two threads,
#
# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python
#
# Pass following list as an argument to place order thread,
import time
from collections import deque
class Queue:
    def __init__(self):
        self.array = deque()
    def enqueue(self,data):
        self.array.appendleft(data)
    def isEmpty(self):
        return len(self.array) == 0
    def size(self):
        return len(self.array)
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queus is Empty")
        else:
            return self.array.pop()


rest = Queue()
def place_order(orders):
    for i in orders:

        rest.enqueue(i)
        print(f"Placing order for {i}")
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while not rest.isEmpty():
        order = rest.dequeue()
        print(f"Now Serving {order}")
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']
place_order(orders)
serve_order()