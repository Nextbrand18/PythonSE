"""
9. Read your file content and print it

my_file = open("c:/temp/daniel.txt",'r') 
str = my_file.read() 
print(str) 
my_file.close()

"""

# Open the file in read mode
with open("words.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()
    
    # Print the content
    print("File content:")
    print(content)