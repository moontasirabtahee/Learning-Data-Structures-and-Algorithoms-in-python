# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: #  nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#
#   (a) What was the average temperature in first week of Jan
#
#   (b) What was the maximum temperature in first 10 days of Jan
#
#   Figure out data structure that is best for this problem

array = []
with open("nyc_weather.csv","r") as f:
    for line in f:
        temp = line.split(",")

        try:
            temperature = int(temp[1])
            array.append(temperature)

        except:
            print("Unvalid value! row ignored")

    average = sum(array[:7])/7
    print(average)

    maximum = max(array[:10])
    print(maximum)

#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

class Hashtable:
    def __init__(self):
        self.MAX = 5
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        temp = 0
        for i in key:
            temp+=ord(i)

        return temp%self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for id ,elem in enumerate(self.arr[h]):

            if len(elem)==2 and elem[0] == key:
                self.arr[h][id] = (key,value)
                found = False
                break
        if not found:
                self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]


ht = Hashtable()
ht["Aba"] = 7
print(ht["Aba"])
with open("nyc_weather.csv","r") as f:
    for line in f:
        temp = line.split(",")

        try:
            day = str(temp[0])
            temp = int(temp[1])
            ht[day] = temp
        except:
            print("Row Ignored !! Invalid temperature")


    print(ht.arr)
    print(ht["Jan 9"])


#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

word = {}
with open("poem.txt",'r') as f:
    for line in f:
        line = line.rstrip("\n")
        wordList = line.split(" ")
        for i in wordList:
            if i not in word.keys():
                word[i] = 1
            else:
                word[i] += 1

    print(word )
