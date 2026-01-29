# Math module contains many important mathematic constants and functions
import math
import json
import re

#min() and max() functions find the smallest and largest values in an ITERABLE(collections) or 
# amongst multiple arguments
x = min(2, 7, 99, 18, 4)
y = max(6, 17, 81, 100, 42)
print("Minimum value:", x)
print("Maximum value:", y)

# abs() function returns the absolute value of a number
z = abs(-7.23)
print("Absolute value:", z)

# pow(x, y) functions return the value of a number(x) raised to the power of another number(y).
# the pow() will always return a float, the ** will return original datatype and is slightly faster
a = pow(3, 4) # 3 to the power of 4
print("Power of:", a)

# sqrt() function returns the square root of a number, returns a float
b = math.sqrt(64)
print("Square root of 64 is:", b)

# ceil() function that rounds a number UP to the nearest integer
c = math.ceil(4.2)

# floor() function that rounds a number down to the nearest integer
d = math.floor(7.8)
print("Ceil:", c, "Floor:", d)

# pi constant represents the mathematical constant pi
p = math.pi # notice its NOT a function!
print("The value of pi is:", p)

### JSON
# The JSON module can be used to work with JSON data
# JSON stands for JavaScript Object Notation

# We can parse JSON objects and convert them into Python dictionaries
json_data = '{"name":"Alice", "age":30, "city":"New York"}' # MUST BE IN QUOTES!!!
data = json.loads(json_data)
print("Name:", data["name"]) #get the value associated with the keys
print("Age:", data["age"])

# We can convert Python dictionaries into JSON objects
# dict, list, tuple, string, int, floats, boolean, None can all be 
#   converted to JSON using the dumps() function
python_dict = {"fruit":"Apple", "color":"red", "quantity":5}
json_object = json.dumps(python_dict)
print("JSON object", json_object, type(json_object))

# The dumps() function can take additional parameters to format the JSON output
formatted_json = json.dumps(python_dict, indent=4)
print("Formatted JSON:", formatted_json)

### REGULAR EXPRESSIONS (RegEx)
# which is a sequence of characters that form a search pattern
# useful for finding substring, data validation, text manipulation, and more!
# the 're' module provides support of regular expressions in Python

# search(pattern, string) function to seach for a pattern within a string
text = "The cat and the rat are on the roof with another cat eating cat food and wearing 3 shoes and 4 collars"
match = re.search("cat", text)
if match:
    print("Pattern found:", match.group())

# we can use the findall(pattern, text) function to find all occurences of a pattern in a string
matches = re.findall("cat", text)
print("All occurences of 'cat'", matches)

# regex metacharacters can help us perform more complex searches
#   AKA wildcards
# [] - a set of characters
print(re.findall(r"[crh]at", text)) # the 'r' signifies we are not looking for the exact match but metacharacters
# checks for all instances of 'cat' AND 'rat'

# \d - any digit 0-9
print(re.findall(r"\d", text))

# ^ - starts with
print(re.search(r"^The", text)) # checks if the string starts with 'The'

# $ - ends with
print(re.search(r"collars$", text)) # checks if the string ends with 'collars'

# split() function splits a string at each match of a pattern
# using the '\s' lets us split at the spaces
split_text = re.split(r"\s", "Split this text into words.")
print(split_text)

# sub(toReplace, withWhat, text) function replaces matches with a specified string
replaced_text = re.sub(r"cat", "dog", text)
print(replaced_text)

