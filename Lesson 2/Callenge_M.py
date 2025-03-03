"""
M.
Create a nested for loop (loop inside another loop) to create a pyramid shape:

"""

d = "X"

for i in range(5):
    for j in range(1):
        print(i * d)



# Set the height of the pyramid
height = 5

# Outer loop for rows
for i in range(height):
    # Inner loop for spaces before stars
    for j in range(height - i - 1):
        print(" ", end="")
    
    # Inner loop for stars
    for k in range(2 * i + 1):
        print("x", end="")
        
    # Move to the next line after each row
    print()