"""
1. Write the following code: a = 1/0;
2. Build a corresponding try-except block to avoid exception.
"""

a = 1/0


try:
    print (a)

except:
    pass

print ("ended")

#------------------------------------------------------

try:
    print (a)

except:
    print("division by zero error occured")

print ("ended")

#------------------------------------------------------




