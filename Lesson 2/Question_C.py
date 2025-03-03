"""
C.

1. Create a variable and initialize it with a number 1-4.
2. Create 4 conditions (if-elif) which will check the variable value.
3. Print a different season name for each number:
For example:
- 1 = summer
- 2 = winter
- 3 = fall
- 4 = spring

"""

codeInput = int(input("Enter a code between  1 - 4 to determine the season: "))
print("You entered:", codeInput)

if codeInput == 1:
    print ("summer")
elif codeInput == 2:
    print ("winter")
elif codeInput == 3:
    print ("fall")
elif codeInput == 4:
    print ("spring")
else:
    print ("Sorry, you have entered a code that is out of range. Please choose between 1 - 4")