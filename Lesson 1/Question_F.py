"""
F.
1. Create a variable and initialize it with a number 1-4.
2. Create 4 conditions (if-elif) which will check the variable.
3. Print the season name accordingly:
- 1 = summer
- 2 = winter
- 3 = fall
- 4 = spring
"""

ab = int(input("Enter a code between  1 - 4 to determine the season: "))
print("You entered:", ab)

if ab == 1:
    print ("summer")
elif ab == 2:
    print ("winter")
elif ab == 3:
    print ("fall")
elif ab == 4:
    print ("spring")
else:
    print ("Sorry, this code is out of range")