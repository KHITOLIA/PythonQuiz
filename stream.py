import streamlit as st
import time
import os
import csv
import streamlit as st
import os
import csv
import time
import atexit

# Folder and File path
FOLDER = "user_scores"
CSV_FILE = os.path.join(FOLDER, "progress.csv")


# -------------------------
# Quiz Questions
# -------------------------
questions = [
    # {
    #     "question": "What is the result of chr(65)?",
    #     "options": ["A", "a", "65", "Error"],
    #     "answer": "A"
    # },
    # {
    #     "question": "What is the output of len('hello')?",
    #     "options": ["4", "5", "6", "Error"],
    #     "answer": "5"
    # },
    # {
    #     "question": "What does int('10') return?",
    #     "options": ["10", "'10'", "Error", "1"],
    #     "answer": "10"
    # },
    # {
    #     "question": "Which keyword is used to handle exceptions?",
    #     "options": ["try", "error", "catch", "except"],
    #     "answer": "try"
    # },
    # {
    #     "question": "What does 'pass' do in Python?",
    #     "options": ["Skips to next iteration", "Stops execution", "Throws error", "Does nothing, a placeholder"],
    #     "answer": "Does nothing, a placeholder"
    # },
    # {
    #     "question": "Which function returns the ASCII value of a character?",
    #     "options": ["ord()", "ascii()", "chr()", "ordVal()"],
    #     "answer": "ord()"
    # },
    # {
    #     "question": "What is the result of chr(65)?",
    #     "options": ["A", "a", "65", "Error"],
    #     "answer": "A"
    # },
    # {
    #     "question": "Which file mode is used to append to a file?",
    #     "options": ["r", "w", "a", "x"],
    #     "answer": "a"
    # },
    # {
    #     "question": "What does open('file.txt', 'r') do?",
    #     "options": ["Reads file", "Writes to file", "Deletes file", "Creates file"],
    #     "answer": "Reads file"
    # },
    # {
    #     "question": "Which keyword is used to create a class?",
    #     "options": ["object", "def", "function", "class"],
    #     "answer": "class"
    # },
    # {
    #     "question": "What is the first index in a Python list?",
    #     "options": ["0", "1", "-1", "None"],
    #     "answer": "0"
    # },
    # {
    #     "question": "What is the output of bool(0)?",
    #     "options": ["True", "False", "None", "0"],
    #     "answer": "False"
    # },
    # {
    #     "question": "Which function converts a string to an integer?",
    #     "options": ["int()", "str()", "float()", "string()"],
    #     "answer": "int()"
    # },
    # {
    #     "question": "What is used to define a dictionary?",
    #     "options": ["()", "[]", "{}", "<>"],
    #     "answer": "{}"
    # },
    # {
    #     "question": "What does dict.get() do?",
    #     "options": ["Deletes key", "Returns value for key, or None if not found", "Adds key", "None"],
    #     "answer": "Returns value for key, or None if not found"
    # },
    # {
    #     "question": "Which keyword is used to define a lambda function?",
    #     "options": ["function", "def", "lambda", "fun"],
    #     "answer": "lambda"
    # },
    # {
    #     "question": "Which method is used to count occurrences in a list?",
    #     "options": ["index()", "find()", "count()", "search()"],
    #     "answer": "count()"
    # },
    # {
    #     "question": "What is the correct way to define a tuple?",
    #     "options": ["[1, 2]", "(1, 2)", "{1, 2}", "<1, 2>"],
    #     "answer": "(1, 2)"
    # },
    # {
    #     "question": "What will be the output of len((1,2,3))?",
    #     "options": ["2", "3", "4", "Error"],
    #     "answer": "3"
    # },
    # {
    #     "question": "What will print('Python' * 2) output?",
    #     "options": ["PythonPython", "Python 2", "Error", "Python"],
    #     "answer": "PythonPython"
    # },
    # {
    #     "question": "Which of the following is used for logical AND?",
    #     "options": ["&&", "and", "||", "&"],
    #     "answer": "and"
    # },
    # {
    #     "question": "What is the output of 'Hello'[1]?",
    #     "options": ["H", "e", "l", "Error"],
    #     "answer": "e"
    # },
    # {
    #     "question": "How do you remove an item from a set?",
    #     "options": ["delete()", "remove()", "pop()", "erase()"],
    #     "answer": "remove()"
    # },
    # {
    #     "question": "What is the data type of True?",
    #     "options": ["int", "str", "bool", "float"],
    #     "answer": "bool"
    # },
    # {
    #     "question": "Which module provides mathematical functions?",
    #     "options": ["maths", "calculate", "math", "numeric"],
    #     "answer": "math"
    # },
    # {
    #     "question": "What is the purpose of 'elif'?",
    #     "options": ["End of if", "Else if", "Error in if", "None of the above"],
    #     "answer": "Else if"
    # },
    # {
    #     "question": "What will print(5 > 3 and 2 < 4) output?",
    #     "options": ["False", "True", "Error", "None"],
    #     "answer": "True"
    # },
    # {
    #     "question": "How do you import a module named 'os'?",
    #     "options": ["include os", "import os", "use os", "require os"],
    #     "answer": "import os"
    # },
    # {
    #     "question": "What is the purpose of the 'finally' block in try-except?",
    #     "options": ["Executes if an error occurs", "Executes always", "Executes if no error", "Skips block"],
    #     "answer": "Executes always"
    # },
    # {
    #     "question": "Which of the following creates an empty set?",
    #     "options": ["set = {}", "set = []", "set = set()", "set = ()"],
    #     "answer": "set = set()"
    # },
    # {
    #     "question": "What is the output of [1,2,3] * 2?",
    #     "options": ["[1,2,3,1,2,3]", "[2,4,6]", "Error", "[1,2,3,2]"],
    #     "answer": "[1,2,3,1,2,3]"
    # },
    # {
    #     "question": "What method is used to sort a list in place?",
    #     "options": ["sort()", "sorted()", "order()", "arrange()"],
    #     "answer": "sort()"
    # },
    # {
    #     "question": "What is the output of 'Python'.replace('o', 'O')?",
    #     "options": ["PythOn", "Pythn", "PythoN", "Error"],
    #     "answer": "PythOn"
    # },
    # {
    #     "question": "Which operator is used to concatenate strings?",
    #     "options": ["*", "+", "-", "/"],
    #     "answer": "+"
    # },
    # {
    #     "question": "What is a docstring in Python?",
    #     "options": ["A single-line comment", "A multi-line comment", "A documentation string for modules/functions/classes", "An error message"],
    #     "answer": "A documentation string for modules/functions/classes"
    # },
    # {
    #     "question": "What is the output of 7 / 2?",
    #     "options": ["3", "3.5", "4", "Error"],
    #     "answer": "3.5"
    # },
    # {
    #     "question": "How do you create an empty dictionary?",
    #     "options": ["dict = ()", "dict = []", "dict = {}", "dict = dict()"],
    #     "answer": "dict = {}"
    # },
    {
        "question": "What does 'continue' do in a loop?",
        "options": ["Ends the loop", "Skips the rest of the current iteration and continues with the next", "Restarts the loop", "Causes an error"],
        "answer": "Skips the rest of the current iteration and continues with the next"
    },
    {
        "question": "Which function converts a number to a string?",
        "options": ["int()", "str()", "float()", "string()"],
        "answer": "str()"
    },
    {
        "question": "What is the output of min(10, 20, 5)?",
        "options": ["10", "20", "5", "Error"],
        "answer": "5"
    },
    {
        "question": "What is the output of max([1, 5, 2])?",
        "options": ["1", "5", "2", "Error"],
        "answer": "5"
    },
    {
        "question": "How do you check if an item exists in a list?",
        "options": ["item in list", "list.contains(item)", "list.has(item)", "check(list, item)"],
        "answer": "item in list"
    },
    {
        "question": "What is the output of '10' + '20'?",
        "options": ["30", "1020", "Error", "10 20"],
        "answer": "1020"
    },
    {
        "question": "Which method is used to remove the last element from a list?",
        "options": ["delete_last()", "remove_last()", "pop()", "cut()"],
        "answer": "pop()"
    },
    {
        "question": "What is the purpose of the 'self' parameter in a class method?",
        "options": ["Refers to the class itself", "Refers to the instance of the class", "Is a keyword for static methods", "None of the above"],
        "answer": "Refers to the instance of the class"
    },
    {
        "question": "Which of the following is NOT a valid Python comparison operator?",
        "options": ["<=", ">=", "=>", "=="],
        "answer": "=>"
    },
    {
        "question": "What is the output of 5 ** 2?",
        "options": ["10", "25", "7", "Error"],
        "answer": "25"
    },
    {
        "question": "What is the output of 'Python'.upper()?",
        "options": ["Python", "python", "PYTHON", "Error"],
        "answer": "PYTHON"
    },
    {
        "question": "How do you create a multiline string?",
        "options": ["Using single quotes ''", "Using double quotes \"\"", "Using triple quotes ''' ''' or \"\"\" \"\"\"", "Using backticks ``"],
        "answer": "Using triple quotes ''' ''' or \"\"\" \"\"\""
    },
    {
        "question": "What is the purpose of the 'else' block with a 'for' loop?",
        "options": ["Executes if the loop is empty", "Executes if the loop completes without a 'break'", "Executes after every iteration", "Executes if an error occurs"],
        "answer": "Executes if the loop completes without a 'break'"
    },
    {
        "question": "Which of the following is a dynamically typed language?",
        "options": ["C++", "Java", "Python", "C#"],
        "answer": "Python"
    },
    {
        "question": "What does 'pip' stand for?",
        "options": ["Python Install Packages", "Preferred Installer Program", "Package Installer for Python", "Python In Progress"],
        "answer": "Preferred Installer Program"
    },
    {
        "question": "What is the output of round(3.7)?",
        "options": ["3", "4", "3.0", "Error"],
        "answer": "4"
    },
    {
        "question": "How do you check the type of a variable 'x'?",
        "options": ["get_type(x)", "typeof(x)", "type(x)", "x.type()"],
        "answer": "type(x)"
    },
    {
        "question": "What is the purpose of 'sys' module?",
        "options": ["System administration", "System-specific parameters and functions", "String manipulation", "File operations"],
        "answer": "System-specific parameters and functions"
    },
    {
        "question": "What is the output of [1, 2, 3][0]?",
        "options": ["1", "2", "3", "Error"],
        "answer": "1"
    },
    {
        "question": "Which of the following is NOT a Python built-in function?",
        "options": ["print()", "len()", "custom_function()", "input()"],
        "answer": "custom_function()"
    },
    {
        "question": "How do you convert a list to a tuple?",
        "options": ["list.to_tuple()", "tuple(list)", "as_tuple(list)", "convert_to_tuple(list)"],
        "answer": "tuple(list)"
    },
    {
        "question": "What is the output of 'hello'.capitalize()?",
        "options": ["Hello", "hello", "HELLO", "Error"],
        "answer": "Hello"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Dictionary"
    },
    {
        "question": "What is list slicing?",
        "options": ["Removing elements from a list", "Adding elements to a list", "Extracting a portion of a list", "Sorting a list"],
        "answer": "Extracting a portion of a list"
    },
    {
        "question": "What is the output of abs(-5)?",
        "options": ["-5", "5", "0", "Error"],
        "answer": "5"
    },
    {
        "question": "Which method is used to remove all elements from a list?",
        "options": ["clear()", "delete_all()", "empty()", "remove_all()"],
        "answer": "clear()"
    },
    {
        "question": "What is a virtual environment in Python?",
        "options": ["A cloud server for Python", "An isolated Python environment for projects", "A debugging tool", "A graphics library"],
        "answer": "An isolated Python environment for projects"
    },
    {
        "question": "What is the output of 10 > 5 or 3 < 1?",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["string", "tuple", "list", "int"],
        "answer": "list"
    },
    {
        "question": "What does the 'with' statement ensure in file handling?",
        "options": ["File is always written to", "File is always read", "File is automatically closed", "File is encrypted"],
        "answer": "File is automatically closed"
    },
    {
        "question": "What is the output of print('Python'[2:5])?",
        "options": ["tho", "yth", "thon", "Error"],
        "answer": "tho"
    },
    {
        "question": "Which method is used to add multiple elements to a set?",
        "options": ["add_all()", "update()", "extend()", "insert_many()"],
        "answer": "update()"
    },
    {
        "question": "What is the purpose of 'import as'?",
        "options": ["To import all modules", "To give an alias to an imported module", "To import a module as a different data type", "To import specific functions"],
        "answer": "To give an alias to an imported module"
    },
    {
        "question": "What is the output of '1' == 1?",
        "options": ["True", "False", "Error", "None"],
        "answer": "False"
    },
    {
        "question": "What is the purpose of the 'zip()' function?",
        "options": ["To compress files", "To combine multiple iterables into an iterator of tuples", "To extract files", "To create a ZIP archive"],
        "answer": "To combine multiple iterables into an iterator of tuples"
    },
    {
        "question": "What is the output of len({'a':1, 'b':2})?",
        "options": ["1", "2", "3", "Error"],
        "answer": "2"
    },
    {
        "question": "Which of the following is a correct way to define a multiline comment?",
        "options": ["# This is a comment", "/* This is a comment */", "''' This is a comment '''", "// This is a comment"],
        "answer": "''' This is a comment '''"
    },
    {
        "question": "What does the 'isinstance()' function do?",
        "options": ["Checks if an object is an instance of a class", "Checks if two objects are identical", "Checks if an object is iterable", "Checks if an object is immutable"],
        "answer": "Checks if an object is an instance of a class"
    },
    {
        "question": "What is the output of print(type('Hello'))?",
        "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
        "answer": "<class 'str'>"
    },
    {
        "question": "What does a negative index in a list do?",
        "options": ["Accesses elements from the beginning", "Accesses elements from the end", "Causes an error", "Converts to a positive index"],
        "answer": "Accesses elements from the end"
    },
    {
        "question": "Which method is used to add an item to a specific position in a list?",
        "options": ["append()", "add()", "insert()", "put()"],
        "answer": "insert()"
    },
    {
        "question": "What is the output of 2 ** 3 ** 2?",
        "options": ["64", "512", "128", "Error"],
        "answer": "512" # Evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512
    },
    {
        "question": "What is the purpose of a 'try-except' block?",
        "options": ["To define a new function", "To handle errors and exceptions", "To create a loop", "To declare variables"],
        "answer": "To handle errors and exceptions"
    },
    {
        "question": "Which function is used to read a whole file's content?",
        "options": ["read_line()", "read_all()", "read()", "get_content()"],
        "answer": "read()"
    },
    {
        "question": "What is the output of 'Python'.find('th')?",
        "options": ["2", "3", "Error", "1"],
        "answer": "2"
    },
    {
        "question": "What is the purpose of 'yield' keyword?",
        "options": ["To return a value and terminate a function", "To create a generator", "To raise an exception", "To define a class"],
        "answer": "To create a generator"
    },
    {
        "question": "How do you get all keys from a dictionary 'my_dict'?",
        "options": ["my_dict.get_keys()", "my_dict.keys()", "keys(my_dict)", "my_dict.all_keys()"],
        "answer": "my_dict.keys()"
    },
    {
        "question": "What is the output of [1, 2, 3] + [4, 5, 6]?",
        "options": ["[1, 2, 3, 4, 5, 6]", "[5, 7, 9]", "Error", "[[1,2,3],[4,5,6]]"],
        "answer": "[1, 2, 3, 4, 5, 6]"
    },
    {
        "question": "Which of the following is NOT a Python collection type?",
        "options": ["list", "tuple", "array", "set"],
        "answer": "array" # 'array' isn't a built-in core type like list, tuple, set, dict. array.array exists but is from a module.
    },
    {
        "question": "What does 'None' represent in Python?",
        "options": ["Zero", "An empty string", "The absence of a value", "False"],
        "answer": "The absence of a value"
    },
    {
        "question": "What is the purpose of a constructor in a class?",
        "options": ["To destroy an object", "To initialize an object's state", "To define class methods", "To inherit from another class"],
        "answer": "To initialize an object's state"
    },
    {
        "question": "What is the output of print(bool(''))?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False"
    },
    {
        "question": "How do you make a copy of a list without affecting the original?",
        "options": ["list2 = list1", "list2 = list1.copy()", "list2 = list(list1)", "Both B and C"],
        "answer": "Both B and C"
    },
    {
        "question": "What is a decorator in Python?",
        "options": ["A design pattern that allows behavior to be added to an object without modifying the object's code", "A type of variable", "A way to comment code", "A built-in function for formatting"],
        "answer": "A design pattern that allows behavior to be added to an object without modifying the object's code"
    },
    {
        "question": "What is the output of '  hello  '.strip()?",
        "options": ["hello", "'  hello  '", " 'hello' ", "Error"],
        "answer": "hello"
    },
    {
        "question": "Which function is used to open a file for writing, creating it if it doesn't exist?",
        "options": ["open(filename, 'r')", "open(filename, 'w')", "open(filename, 'a')", "create(filename)"],
        "answer": "open(filename, 'w')"
    },
    {
        "question": "What is the correct syntax for a for loop that iterates from 0 to 4 (inclusive)?",
        "options": ["for i in range(5):", "for i in range(4):", "for i from 0 to 4:", "loop i in (0, 4):"],
        "answer": "for i in range(5):"
    },
    {
        "question": "What is an f-string in Python?",
        "options": ["A file string", "A fast string", "A formatted string literal", "A function string"],
        "answer": "A formatted string literal"
    },
    {
        "question": "What is the output of 1 + 2 * 3?",
        "options": ["9", "7", "6", "Error"],
        "answer": "7"
    },
    {
        "question": "What is the purpose of '__init__' method in a class?",
        "options": ["To destroy an object", "To initialize an object's attributes", "To print object details", "To define a static method"],
        "answer": "To initialize an object's attributes"
    },
    {
        "question": "Which method is used to join elements of a list into a string?",
        "options": ["concat()", "join()", "merge()", "combine()"],
        "answer": "join()"
    },
    {
        "question": "What is an iterable in Python?",
        "options": ["An object that can be looped over", "A type of error", "A mathematical function", "A variable name"],
        "answer": "An object that can be looped over"
    },
    {
        "question": "What is the output of print({}.get('key', 'default'))?",
        "options": ["None", "key", "default", "Error"],
        "answer": "default"
    },
    {
        "question": "How do you reverse a list in place?",
        "options": ["list.reverse()", "list.reversed()", "reverse(list)", "list[::-1]"],
        "answer": "list.reverse()"
    },
    {
        "question": "What does 'assert' keyword do?",
        "options": ["Declares a variable", "Checks if a condition is true, raises an AssertionError if not", "Prints a message", "Skips a block of code"],
        "answer": "Checks if a condition is true, raises an AssertionError if not"
    },
    {
        "question": "What is the output of print(float(5))?",
        "options": ["5", "5.0", "Error", "0.5"],
        "answer": "5.0"
    },
    {
        "question": "Which of the following is used to store unique items?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Set"
    },
    {
        "question": "What is a generator in Python?",
        "options": ["A function that generates random numbers", "A function that returns an iterator", "A class that generates objects", "A built-in data type"],
        "answer": "A function that returns an iterator"
    },
    {
        "question": "What is the purpose of 'super()' in class inheritance?",
        "options": ["Calls the current class's method", "Calls the parent class's method", "Calls a global function", "Returns the superclass object"],
        "answer": "Calls the parent class's method"
    },
    {
        "question": "What is the output of print(list('abc'))?",
        "options": ["['abc']", "['a', 'b', 'c']", "abc", "Error"],
        "answer": "['a', 'b', 'c']"
    },
    {
        "question": "Which module is commonly used for working with regular expressions?",
        "options": ["regex", "re", "pattern", "match"],
        "answer": "re"
    },
    {
        "question": "What is a lambda function?",
        "options": ["A named function", "An anonymous function", "A recursive function", "A built-in function"],
        "answer": "An anonymous function"
    },
    {
        "question": "What is the output of [1, 2, 3][1:3]?",
        "options": ["[1, 2]", "[2, 3]", "[1, 2, 3]", "Error"],
        "answer": "[2, 3]"
    },
    {
        "question": "Which of the following correctly opens a file for writing in binary mode?",
        "options": ["open('file.txt', 'wb')", "open('file.txt', 'b')", "open('file.txt', 'w+')", "open('file.txt', 'binary')"],
        "answer": "open('file.txt', 'wb')"
    },
    {
        "question": "What is the purpose of 'dir()' function?",
        "options": ["To get current directory", "To list attributes and methods of an object", "To delete a directory", "To create a directory"],
        "answer": "To list attributes and methods of an object"
    },
    {
        "question": "What is the output of 'apple'.count('p')?",
        "options": ["1", "2", "3", "0"],
        "answer": "2"
    },
    {
        "question": "What is the difference between 'is' and '=='?",
        "options": ["'is' checks value, '==' checks identity", "'is' checks identity, '==' checks value", "They are interchangeable", "None of the above"],
        "answer": "'is' checks identity, '==' checks value"
    },
    {
        "question": "What is a module in Python?",
        "options": ["A single function", "A file containing Python definitions and statements", "A variable type", "A program execution unit"],
        "answer": "A file containing Python definitions and statements"
    },
    {
        "question": "What is the output of type(1.0)?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'Decimal'>"],
        "answer": "<class 'float'>"
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "options": ["send", "yield", "return", "pass"],
        "answer": "return"
    },
    {
        "question": "What is list comprehension?",
        "options": ["A way to define a list of functions", "A concise way to create lists", "A method for list manipulation", "A type of list sorting"],
        "answer": "A concise way to create lists"
    },
    {
        "question": "What is the output of {'a':1, 'b':2}['b']?",
        "options": ["1", "2", "b", "Error"],
        "answer": "2"
    },
    {
        "question": "Which statement is used to skip the current iteration of a loop?",
        "options": ["break", "pass", "continue", "skip"],
        "answer": "continue"
    },
    {
        "question": "What is the output of print(tuple([1,2,3]))?",
        "options": ["(1,2,3)", "[1,2,3]", "{1,2,3}", "Error"],
        "answer": "(1,2,3)"
    },
    {
        "question": "Which function is used to get the current working directory?",
        "options": ["os.cwd()", "os.get_cwd()", "os.getcwd()", "os.current_dir()"],
        "answer": "os.getcwd()"
    },
    {
        "question": "What is the output of 'Python'.replace('P', 'J', 1)?",
        "options": ["Jython", "python", "Python", "Error"],
        "answer": "Jython"
    },
    {
        "question": "What is the purpose of 'sys.exit()'?",
        "options": ["To exit a loop", "To exit the Python interpreter", "To exit a function", "To exit a class"],
        "answer": "To exit the Python interpreter"
    },
    {
        "question": "How do you create a frozen set?",
        "options": ["frozenset([1,2,3])", "frozen_set(1,2,3)", "set.freeze([1,2,3])", "immutable_set([1,2,3])"],
        "answer": "frozenset([1,2,3])"
    },
    {
        "question": "What is the output of print(bool(1))?",
        "options": ["True", "False", "0", "1"],
        "answer": "True"
    },
    {
        "question": "Which method is used to remove an item from a dictionary by its key?",
        "options": ["delete()", "remove()", "pop()", "clear()"],
        "answer": "pop()"
    },
    {
        "question": "What is an argument in a function?",
        "options": ["The return value of the function", "A variable defined inside the function", "A value passed to the function when it's called", "The name of the function"],
        "answer": "A value passed to the function when it's called"
    },
    {
        "question": "What is the purpose of the 'global' keyword?",
        "options": ["To define a function globally", "To access and modify a global variable from inside a function", "To make a variable accessible only within a function", "To declare a new global variable"],
        "answer": "To access and modify a global variable from inside a function"
    },
    {
        "question": "What is the output of print('Python'.startswith('P'))?",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "Which of the following is used to remove whitespace from both ends of a string?",
        "options": ["trim()", "strip()", "remove_whitespace()", "clean()"],
        "answer": "strip()"
    },
    {
        "question": "What is the default return value of a Python function if no return statement is used?",
        "options": ["0", "An empty string", "None", "True"],
        "answer": "None"
    },
    {
        "question": "What is the output of print(divmod(10, 3))?",
        "options": ["(3, 1)", "3.33", "1", "Error"],
        "answer": "(3, 1)"
    },
    {
        "question": "What is the purpose of the 'pass' statement?",
        "options": ["To raise an error", "To act as a placeholder where a statement is syntactically required but no action is desired", "To terminate a loop", "To skip a line of code"],
        "answer": "To act as a placeholder where a statement is syntactically required but no action is desired"
    },
    {
        "question": "Which method is used to convert all characters in a string to uppercase?",
        "options": ["upper()", "to_upper()", "uppercase()", "capitalize()"],
        "answer": "upper()"
    },
    {
        "question": "What is the output of 5 // 2?",
        "options": ["2", "2.5", "3", "Error"],
        "answer": "2"
    },
    {
        "question": "What is the purpose of the 'help()' function?",
        "options": ["To get help from the Python community", "To display documentation for modules, functions, classes, keywords, etc.", "To find errors in code", "To suggest improvements to code"],
        "answer": "To display documentation for modules, functions, classes, keywords, etc."
    }
]

# -------------------------
# Session Initialization
# -------------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selections" not in st.session_state:
    st.session_state.selections = [None] * len(questions)
if "submitted" not in st.session_state:
    st.session_state.submitted = [False] * len(questions)
if "username" not in st.session_state:
    st.session_state.username = ""

# -------------------------
# Save User Progress
# -------------------------
def save_user_progress(username, score, total):
    folder = "user_scores"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, "progress.csv")

    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Username", "Score", "Total Questions"])
        writer.writerow([username, score, total])

# -------------------------
# Main App Logic
# -------------------------
def main():
    st.set_page_config(page_title="Python Quiz App", layout="centered", page_icon="🧠")
    st.title("🧠 Python Quiz App")

    if st.session_state.username == "":
        st.session_state.username = st.text_input("Enter your Username to begin:", key="username_input")
        if st.session_state.username:
            st.rerun()
        return

    st.markdown(f"👤 **User:** `{st.session_state.username}`")

    q_idx = st.session_state.current_q
    total = len(questions)

    if q_idx >= total:
        st.success("🎉 You’ve completed the quiz!")
        st.subheader(f"✅ Final Score: {st.session_state.score} / {total}")

        # Save user progress
        save_user_progress(st.session_state.username, st.session_state.score, total)

        st.markdown("---")
        st.subheader("📝 Your Answers Review")
        for i, q in enumerate(questions):
            selected = st.session_state.selections[i]
            correct = q["answer"]
            is_correct = selected == correct
            result = "✅ Correct" if is_correct else f"❌ Wrong (Correct: {correct})"
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.write(f"- Your Answer: `{selected}`")
            st.write(f"- {result}")
            st.markdown("---")
        return

    # -------------------------
    # Progress
    # -------------------------
    progress = (q_idx + 1) / total
    st.progress(progress, text=f"Question {q_idx + 1} of {total}")

    # -------------------------
    # Current Question
    # -------------------------
    q = questions[q_idx]
    st.subheader(f"Question {q_idx + 1}")
    st.markdown(f"**{q['question']}**")

    previous_selection = st.session_state.selections[q_idx]
    selected = st.radio(
        "Select your answer:",
        options=q["options"],
        index=q["options"].index(previous_selection) if previous_selection in q["options"] else None,
        key=f"radio_{q_idx}"
    )

    if selected:
        st.session_state.selections[q_idx] = selected

    if not st.session_state.submitted[q_idx]:
        if st.button("✅ Submit Answer"):
            if selected:
                st.session_state.submitted[q_idx] = True
                correct = q["answer"]
                if selected == correct:
                    st.success(f"✅ Correct! You chose: {selected}")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! You chose: {selected}")
                    st.info(f"✔️ Correct answer: {correct}")

                time.sleep(1.5)
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.warning("⚠️ Please select an option first.")
    else:
        correct = q["answer"]
        if selected == correct:
            st.success(f"✅ Correct! You chose: {selected}")
        else:
            st.error(f"❌ Wrong! You chose: {selected}")
            st.info(f"✔️ Correct answer: {correct}")
        time.sleep(1.5)
        st.session_state.current_q += 1
        st.rerun()

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    main()



