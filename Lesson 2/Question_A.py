"""
A.
1 Create two numeric variables named X and Y.
2. Print the word “BIG” if the value of X is bigger than Y.
3. Print the word “small” if the value of X is smaller than Y.
"""

X = input("Enter a Value for X: ")
Y = input("Enter a Value for Y: ")

if X > Y:
    print("BIG")
elif Y > X:
    print("small")
else:
    print("Neither is BIG or small")