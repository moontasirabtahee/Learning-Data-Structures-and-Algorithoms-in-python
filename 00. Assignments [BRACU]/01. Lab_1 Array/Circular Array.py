# Created by Moontasir Abtahee at 2/8/2022
# Feature: #BRAC UNIVERSITY
# Scenario: # CSE220 Lab Assignment
#1. Palindrome

def palindrome(array,start,size):
    end = (start+size-1)%len(array)
    count = 0
    while(start != end):
        if array[start] != array[end]:
            return False


        start = (start+1)%len(array)
        end = (end-1)%len(array)

    return True


print(palindrome([20,10,0,0,0,10,20,30] ,5,5))

#2. Intersection
def intersection(array1,start1,size1,array2,start2,size2):

    array = []
    array1 = LinearArray(array1, start1, size1)
    array2 = LinearArray(array2,start2,size2)
    for i in array1:
        for j in array2:
            if i == j:
                array.append(i)

    return array
def LinearArray(arr,start,size):
    array = []
    for i in range(size):
        array.append(arr[start])
        start = (start+1)%len(arr)

    return array
print( intersection([40,50,0,0,0,10,20,30],5,5, [10,20,5,0,0,0,0,0,5,40,15,25],8,7))
# Suppose you have been hired to develop a musical chair game. In this game there
# will be 7 participants and all of them will be moving clockwise around a set of 7 chairs
# organized in a circular manner while music will be played in the background. You will
# control the music using random numbers between 0-3.If the generated random number
# is 1, you will stop the music and if the number of participants who are still in the game is
# n, the participants at position (n/2) will be eliminated. Each time a participant is
# eliminated, a chair will be removed and you have to print the player names who are still
# in the game.The game will end when there will be only one participant left. At the end of
# the game,display the name of the winner.
# [Hint: You will need to invoke a method to generate a random number between 0
# (inclusive) to 3 (inclusive)]


import random
player = [1,2,3,4,5,6,7]
while len(player)>1:
    x = random.randint(1,3)
    if x==1:
        #player = player[:(len(player)//2)] + player[(len(player)//2)+1:]
        x = player[(len(player)//2)]
        player.remove(x)
        print(player)

print(player)