"""
K.
Create a program which will get a list of numbers and prints the sum of all items.

"""

nList = [13,6,10,87,7,4,9,9,5,40, 8,35,99]
x = 0

for i in nList:
    print(i)
    x=x+i
print(f"Sum of the numbers in the list is {x}")

'''
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    print(sum_numbers)

'''