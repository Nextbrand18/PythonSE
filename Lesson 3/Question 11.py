
"""
11. Create a Flask application which listens to port 30000 and has 2 routes:

• /content - which returns the content of any txt file and status code 200 (e.g: localhost:4000/content).
• /register - which writes the word “hello” into any txt file and return “success” and status code 201 as a response (e.g: localhost:4000/register).



from flask import Flask 

app = Flask(__name__) 

@app.route('/content') 
def read(): 
    return open("words.txt").read(), 200 
    
@app.route('/register') 
def register(): 
    open("words.txt", 'w').write("hello") 
    return "success", 201 

    if __name__ == '__main__': 
        app.run('0.0.0.0', debug=True, port=30000)

"""

# Import the Flask class from the flask module
from flask import Flask 

# Create a Flask web application instance
# __name__ is a special Python variable that holds the name of the current module
# Using __name__ helps Flask determine the root path for the application
app = Flask(__name__) 

# Define a route for the URL '/content'
# This decorator tells Flask which URL should trigger this function
@app.route('/content') 
def read(): 
    # Open the file "words.txt", read its contents, and return them
    # The second value 200 is the HTTP status code (200 = OK)
    return open("words.txt").read(), 200 
    
# Define a route for the URL '/register'
@app.route('/register') 
def register(): 
    # Open "words.txt" in write mode and write "hello" to it
    # 'w' mode overwrites any existing content in the file
    open("words.txt", 'w').write("hello") 
    # Return a success message with status code 201 (Created)
    return "success", 201 

# This block ensures the app only runs if this script is executed directly
# (not when imported as a module in another script)
if __name__ == '__main__': 
    # Start the Flask development server
    # '0.0.0.0' makes the server publicly available on your local network
    # debug=True enables debug mode for development (auto-reload, detailed error messages)
    # port=30000 specifies which port the server listens on
    app.run('0.0.0.0', debug=True, port=30000)