# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        temp = 0
        for i in key:
            temp += ord(i)

        return temp%self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for id , elem in enumerate(self.arr[h]):

            if len(elem) == 2 and elem[0] == key:
                self.arr[h][id] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
    def __getitem__(self, key):
        h = self.get_hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]
    def __delitem__(self, key):
        h = self.get_hash(key)
        for id ,elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][id]
ht = HashTable()
ht["march 6"] = 1714804999
print(ht["march 6"])
ht["march 17"] = 954657
print(ht["march 17"])
print(ht.arr)
del ht["march 17"]
print(ht.arr)