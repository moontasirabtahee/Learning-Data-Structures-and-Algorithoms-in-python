# Created by Moontasir Abtahee at 2/9/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
#Implement a recursive algorithm to find factorial of n.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n-1)


print(factorial(5))

def Fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(10))

def printArray(array):
    if len(array) == 0:
        return
    print(array[0], end=" -->")
    printArray(array[1:])




printArray([1,2,3,4,5,6,7,8])
print()
def powerN(base,N):
    if N == 0:
        return 1
    return base*powerN(base,N-1)

print(powerN(3,3))

