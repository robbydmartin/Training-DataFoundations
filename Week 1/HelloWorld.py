print("Hello, World!") # Can use both single and double quotes to print strings.
print('Hello, World!')

## Datatypes in Python
# variables can be declared implicitly without specifying datatype
a = "string of words and characters and yada yada"
explicit_string: str = "word!"

# Number types
# Integer - int - whole numbers
b = 7
explicit_int: int = 7

# Float - float - decimal numbers
c= 3.14159
explicit_float: float = 2.5739

# Boolean values
# Falsey values: 0, 0.0, empty string "", empty list [], empty tuple (), empty dict {}
# Truthy values: anything else!
d = True
explicit_bool: bool = False

if b:
    print("b is True")
else:
    print("b is False")

# Nonetype - None - represents a null value or the absence of a value
e = None
explicit_none: None = None

# Print multiple variables
print(a, b)
print(explicit_string)
# Print sum of b and c
print(b + c)
# Mix variables
print("I have", b, "cats in my house.")

# Datatype can change without explicitly changing it.
f = 74
print(f)
f = "Green"
print(f)

# Casting lets up specify the datatype we want to convert to
a = str(9)
b = int(9)
c = float(9) # will print as 9.0
d = bool(9) # will print as True
print(a, b, c, d)

# Check datatype using the type() function
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Variables are CASE SENSITIVE!
A = "uppercase A"
print(A)
a = "lowercase a"
print(a)

# We can assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"
print(dog, DOG, Dog, dOg)

