# Created by Moontasir Abtahee at 2/21/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
def pattern(n,i=1,j=1):
    if n == 0:
        return
    if i >j:
        print(j ,end=" ")
        pattern(n,i,j+1)
    if i == j:
        print(j)
        pattern(n-1,i+1,1)

pattern(10)



def space(s):  # Detect the space
    if s == 0:
        return
    print(" ", end=" ")
    space(s - 1)


def row_printer(n, i=1):  # Print the row
    if n == 0:          # "n" initialize the iteration
        return          # i print the row elem
    else:
        print(i, end=" ")
        row_printer(n - 1, i=i + 1)


def pattern_print(n):
    wrap(n, 1, 1, n)


def wrap(num, j, i, n):
    if num == 0:
        return
    space(n - i)
    row_printer(j)
    print()  # space new row start
    wrap(num=num - 1, i=i + 1, j=j + 1, n=n)


pattern_print(10)
