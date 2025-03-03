"""
10. Write Hebrew content into your text file and print its content programmatically.


my_file2 = open("c:/temp/hebrew.txt",'w',encoding='utf-8') 
my_file2.write("שלום ") 
my_file2.close() 

my_file2 = open("c:/temp/hebrew.txt",'r',encoding='utf-8') 
str = my_file2.read() 
print(str)
"""

# Write Hebrew content to file
with open("words.txt", "w", encoding="utf-8") as file:
    # Some Hebrew text (a greeting and a sentence)
    hebrew_text = "שלום! זה טקסט בעברית. ברוכים הבאים לעולם התכנות."
    file.write(hebrew_text)
    
print("Hebrew text has been written to the file.")

# Read and print the Hebrew content
with open("words.txt", "r", encoding="utf-8") as file:
    content = file.read()
    
    print("\nFile content:")
    print(content)