'''

try:
    # Some code that might raise an exception
    x = 1
except Exception as e:
    # Code that runs if an exception occurs
    print(f"An error occurred: {e}")
finally:
    # Code that runs regardless of whether an exception occurred
    print("finally")
'''

try:
    # Some code that might raise an exception
    a = 1/0
finally:
    # Code that will run regardless of whether an exception occurred
    print("finally")

    """
    What exception types can be caught by the following handler?
Except:
    

Python has numerous built-in exceptions that are organized in a hierarchy. Here's a list of the most common built-in exceptions in Python:
Base Exceptions:

BaseException: The root exception class
Exception: Base class for all non-exit exceptions
ArithmeticError: Base class for arithmetic errors

Common Exceptions:

AssertionError: Raised when an assert statement fails
AttributeError: Raised when attribute reference or assignment fails
EOFError: Raised when input() hits end-of-file condition
FileNotFoundError: Raised when a file or directory is requested but doesn't exist
ImportError: Raised when an import statement fails
IndentationError: Raised for incorrect indentation
IndexError: Raised when a sequence index is out of range
KeyError: Raised when a mapping (dictionary) key is not found
KeyboardInterrupt: Raised when the user hits the interrupt key (Ctrl+C)
MemoryError: Raised when an operation runs out of memory
NameError: Raised when a local or global name is not found
NotImplementedError: Raised by abstract methods
OSError: Raised for operating system-related errors
OverflowError: Raised when a calculation exceeds maximum limit for a numeric type
RecursionError: Raised when the interpreter detects maximum recursion depth exceeded
RuntimeError: Raised when an error doesn't fall under any other category
StopIteration: Raised by next() when there are no further items
SyntaxError: Raised by the parser when syntax error is encountered
SystemError: Raised when the interpreter finds an internal error
SystemExit: Raised by the sys.exit() function
TypeError: Raised when an operation or function is applied to an object of inappropriate type
UnboundLocalError: Raised when a reference is made to a local variable before assignment
UnicodeError: Raised when a Unicode-related encoding or decoding error occurs
ValueError: Raised when a function receives an argument of correct type but inappropriate value
ZeroDivisionError: Raised when division or modulo operation has second argument of zero

All of these can be caught with a bare except: clause, though as mentioned, it's better practice to catch specific exceptions as needed.
    
    """

    """
    5. What is wrong with using the above type of exception handler?

    The exception handler except: without any specified exception type will catch all exceptions.
This is known as a bare except clause, and it's generally not recommended in Python because it can catch unexpected exceptions, including:

Built-in exceptions like ValueError, TypeError, IndexError, etc.
User-defined exceptions
System exceptions like KeyboardInterrupt and SystemExit
BaseException and all its subclasses

Using a bare except like this is often discouraged because:

It can hide programming errors that should be fixed
It might catch exceptions that should terminate the program (like KeyboardInterrupt)
It makes debugging more difficult as it doesn't distinguish between different types of errors
    """


    """
    6. What exceptions can be caught by the following handlers?
...
except IOError ...
except ZeroDivisionError

Here's what these exception handlers will catch:

except IOError:

This will catch IOError exceptions, which relate to input/output operations
Note that in Python 3, IOError is actually an alias for OSError, so it catches the same exceptions as OSError would
This includes file operations that fail (file not found, permission errors, etc.)
Examples: failed file opening, reading, writing, or other I/O operations


except ZeroDivisionError:

This catches only ZeroDivisionError exceptions
These occur when you attempt to divide by zero
For example: x = 5/0 or x = 5 % 0



Each handler will only catch the specific exception type mentioned and any subclasses of that exception. They won't catch other types of exceptions or their parent classes (like Exception or BaseException).

    
    """