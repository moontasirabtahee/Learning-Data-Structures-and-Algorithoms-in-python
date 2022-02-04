# Created by Moontasir Abtahee at 2/3/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses = [2200,2350,2600,2130,2190]

# In Feb, how many dollars you spent extra compare to January?
print(f"{monthly_expenses[1]-monthly_expenses[0]}")

# Find out your total expense in first quarter (first three months) of the year.
print(f"{monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]}")

# Find out if you spent exactly 2000 dollars in any month
print(2000 in monthly_expenses)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

monthly_expenses.append(1980)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

monthly_expenses[3] = monthly_expenses[3]-200
print(monthly_expenses)


heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("Black panther")
heros = heros[:-1]
heros.insert(3,"Black Panther")
heros.remove("thor")
heros.remove("hulk")

heros.insert(1,"Doctor strage")

heros.sort()
print(heros)

#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

odd_numbers = []
max_number = int(input())
for i in  range(1,max_number):
    if i%2 != 0:
        odd_numbers.append(i)
        print(f"{i} is added to the list")
