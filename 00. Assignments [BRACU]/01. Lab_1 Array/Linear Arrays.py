# Created by Moontasir Abtahee at 2/8/2022
# Feature: #BRAC UNIVERSITY
# Scenario: # CSE220 Lab Assignment

#1. Shift Left k Cells

def leftShiftbyOne(array):
    for i in range(0,len(array)-1):
        array[i] = array[i+1]

    array[-1] = 0
    return array

def leftShift(array,k):
    for i in range(k):
        array = leftShiftbyOne(array)

    return array

print(leftShift([10,20,30,40,50,60],4))

#2. Rotate Left k cells
def rotateLeftbyOne(array):
    temp = array[0]
    for i in range(0, len(array) - 1):
        array[i] = array[i + 1]

    array[-1] = temp
    return array


def rotateLeft(array,k):
    for i in range(k):
        rotateLeftbyOne(array)
    return array

print(rotateLeft([10,20,30,40,50,60],4))


#3. Remove an element from an array
def remove(source,size,idx):
    for i in range(len(source)):
        if i == idx:
            for j in range(i,len(source)-1):
                source[j] = source[j+1]
            source[size-1] = 0
    return source

print(remove([10,20,30,40,50,0,0,0,0],5,2))


#4. Remove all occurrences of a particular element from an array


def removeAll(source,size,elem):
    counter = 0
    for i in range(size):
        if source[i] != elem:
            source[counter] = source[i]
            counter += 1
        else:
            size = size - 1

        for i in range(size,len(source)):
            source[i] = 0
    return source

source=[10,2,30,2,50,2,2,10,0,0]
print(removeAll(source,8,2))


#5. Splitting an Array
def total(array):
    total = 0
    for i in array:
        total+=i

    return total

def balance(array):
    for i in range(len(array)):
        #print(array[:i+1],total(array[:i+1]),array[i+1:],total(array[i+1:]))
        if total(array[:i+1]) == total(array[i+1:]):
            return True

    return False

print(balance( [10, 3, 1, 2, 10]))

#6. Array series

def arraySeries(n):
    array = [0 for i in range(n*n)]
    index=len(array)-1
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if(j<=i):
                array[index]=j
            index-=1

    return array

print(arraySeries(3))


#7. Max Bunch Count
def maxBrunch(array):
    maxCounter = 0
    counter = 1
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            counter+=1
            if counter>maxCounter:
                maxCounter = counter
        else:
            counter = 1
    return maxCounter


print(maxBrunch([1,1,2, 2, 1, 1,1,1]))

#8. Repetition

def repeat(array,k):
    counter = 0
    for i in array:
        if i == k:
            counter+=1

    return counter


def Repetition(array):
    freq = {}

    for i in array:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print(freq)
    for i,j in freq.items():
        for x,y in freq.items():
            if i != x and j == y != 1:
                return True

    return False
print(Repetition([4,5,6,6,4,3,4,4]))