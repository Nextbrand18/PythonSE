"""
I.
Write a program with the following:
1. Function that receive two numbers, add them, and return the sum.
2. Function that receive two Strings, add space between them, and return one spaced string.

"""

def sumIT(x,y):
    #z = x + y
    print (x + y)

x = float(input("Enter 1st number: "))
y = float(input("Enter 2nd number: "))

sumIT(x,y)

def rString(i,j):
    #z = x + y
    print (f"{i} {j}")

i = str(input("Enter 1st string: "))
j = str(input("Enter 2nd string: "))

rString(i,j)