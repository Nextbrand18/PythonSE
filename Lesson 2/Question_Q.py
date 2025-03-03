'''
Q.
Write a Python program to get the smallest number from a list.
'''

nList = [13,6,10,87,7,4,9,9,5,40, 8,35,99]
#print(nList[i-1])

# First element
sm = nList[0]


for i in range (len(nList)):
    if (nList[i] < sm):
        sm = nList[i]
print(sm)


