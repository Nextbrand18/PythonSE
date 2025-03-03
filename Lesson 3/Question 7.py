"""
7. Create a text file named “words.txt” programmatically

Ans

my_file = open("c:/temp/daniel.txt",'w') 
my_file.close()
"""

with open("words.txt", "w") as file:
    file.write("")  # Creates an empty file


"""
with open("words.txt", "w") as file:
    file.write("This is my new text file.\nIt contains some sample text.")

    
"""