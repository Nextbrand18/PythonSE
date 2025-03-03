"""
L.
Write a Python program to iterate over dictionaries and prints all keys using for loop.
"""

nDict = {"Name" : "Brian", "Gender" : "Male", "Status":"Active"}


q =[]
for keys in nDict:
    q.append(keys)
print(q)

#Version 133.0.6943.142
'''
d = {'x': 10, 'y': 20, 'z': 30}
for item in d.keys():
    print(item)
'''