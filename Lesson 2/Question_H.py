"""
H.
Write a program with the following:
1. Function that receive a name as an argument and prints it.
2. Function that receive a number, divide it by 2, and prints the result.

"""

def printName (pName):
    '''
    Function to print name
    '''
    pName = pName
    print (pName)


yourName = str(input("Type your name: "))
printName(yourName)

def calc (x):
    '''
    Function that receive a number, divide it by 2, and prints the result
    '''
    y = x/2
    print(y)

z = float(input("Input a number: "))
calc(z)