# Created by Moontasir Abtahee at 2/21/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
def hocBuilder(height):
    if height == 0:
        return 0
    if height == 1:
        return 8
    else:
        return 5+ hocBuilder(height-1)


print(hocBuilder(2))
