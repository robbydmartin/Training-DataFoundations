import array as arr

# Functions are how we package useful functionality into reusable blocks to use when needed.
# creating a function - we use the def keyword, name the function, give it parameters
# then we write the code we want it to execute

# function with 2 parameters
def addition_function(x: int, y: int):
    return x + y

# no parameters function
def bark():
    print("Woof")

# Calling our functions
sum = addition_function(9, 10)
print(sum)
bark()

print(addition_function("my cat ", "Wonton")) # This will still work!

# SCOPES
# are areas of the code where an object/variable/function can be called upon and used

# Local: variables declared inside a block of code and are only available inside that block
def local_variable():
    message = "Hi people!"
    print(message)

    # Enclosed: function is enclosed within another function
    # this function can access variables from the outer function
    def enclosed():
        message = "enclosed hi people"
        print(message)
    
    enclosed()
    print(message)

local_variable()

# Global: accessed from anywhere within the file they are declared in
# as well as other files IF they are brought in via import
myCat = "Wonton"

# Default: Built-in default python methods where all keywords live and can be accessed from anywhere

# Modules in Python are simply files in which python code is written
# to use different modules, we have to import them into the module we want to use it from
# modules also support aliases using the 'as' keyword

# Arrays are not technically built into python, we have to import the array module
# contain elements of the same type, stored sequentially, and indexed from 0
# array(typecode, initializer)

# Typecode: this is a single character that specifies the type of data stored in the array
# 'i' : stored integer (4 bytes)
# 'f' : floating point (4 bytes)
# 'd' : double precision floating point (8 bytes)
# 'b' : signed integer (1 byte)
# 'u' : unicode character (2 bytes)
# 'l' : signed long integer (4 bytes) -> (can be platform dependent)

# Initializer: this is an optional parameter that intializes the array with elements
# it can be a list, tuple, or any iterable containing the initial values for the array

intArray = arr.array('i', [1, 2, 77, 3, 25, 99, 51])
print(intArray[2])
mySubset = intArray[1:4]
print(mySubset)

for item in intArray:
    print(item)

# Find the length
print(len(intArray))
# Sort the array in ascending order (default)
print(sorted(intArray))

# Lambda functions AKA anonymous functions
# small, single line functions that can have any number of arguments, but only one single expression
# lambda args: expression

add = lambda x, y: x + y
print(add(3, 4))

# List of tuples
pokedex = [
    ("Bulbasaur", 1),
    ("Lapras", 131),
    ("Eevee", 133),
    ("Cubone",  104),
    ("Gengar", 94)
]

dictionaryPokedex = {3: "Venasaur", 133:"Eevee", 2: "Ivysaur", 94:"Gengar"}

print(dictionaryPokedex)

pokedex.sort(key = lambda x: x[1], reverse=False) # sorts in ascending order, reverse=False is the default so not necessary
print(pokedex[1][1])