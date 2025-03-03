"""
8. Write your name into the file

ANS
my_file = open("c:/temp/daniel.txt",'w') 
my_file.write("daniel") 
my_file.close()
"""

# Open the file in write mode
with open("words.txt", "w") as file:
    # Write your name to the file
    file.write("BJ")  # Replace "Your Name" with your actual name

print("Successfully wrote name to words.txt")