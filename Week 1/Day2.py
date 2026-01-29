# Collections - variables that hold multiple values
# Collections is a module in python
# Lists, tuples, sets, and dictionaries

'''
List is a collection that is ordered and changable
'''

# Lists use square[] brackets and can contain different data types
# Python sees lists as objects with the datatype as 'list'
fruits = ["Orange", "Strawberry", "Apple"]
fruityFruits = favoriteFruits = ["Watermelon", "Blueberries", "Banana"]
Or, St, Ap = fruits # Can associate a list with individual variables.
print(Or)
print(St)
print(Ap)

mixedTypes = ["cheese", 17, False, 32.76] # All valid for a list

#len() - returns length of list
print(len(fruits))

#type() - returns the datatype of the list
print(type(fruits))

# Access an item in the list using the item's index
print(fruits[1])
# Can also use negative indexing which starts at the end
print(fruits[-1])
# Range of indexes, the second number is NOT inclusive
print(fruits[1:3])

# Add items to a list
fruits.append("Grapes")
print(fruits)
# Add items at specific index
fruits.insert(2, "Kiwi")
print(fruits)

#TUPLES
# Tuples can contain different datatypes and are defined by the data type 'Tuple'
animalTuple = ("Cat", "Dog", "Bird", "Fish")
print(animalTuple)

# len() works for tuples too
print(len(animalTuple))

# Since tuples are immutable, we cannot use the append() function
# Instead we can convert to a list
animalList = list(animalTuple)
animalList.append("Snake")
print(animalList)

#SETS
# Sets are created using curly braces{}
colorSet = {"blue", "green", "pink", "orange"}

# Sets can use the add() and remove() functions for adding and removing elements
colorSet.add("black")
colorSet.remove("blue")
print(colorSet)

# Sets support intersection, difference, and union
secondSet = {"Burger", "Fries", "Milkshake", "pink", "black"}
intersectionSet = colorSet & secondSet
print("Intersection set: ", intersectionSet)

differenceSet = colorSet - secondSet
print("Difference set: ", differenceSet)

unionSet = colorSet | secondSet
print("Union set: ", unionSet)

#DICTIONARIES
# Dictionaries are defined as key/value pairs with curly braces{} and separated by a colon :
# Pairs are separated by commas,
# The first value is treated as the key and the second element is the value
foodDictionary = {"Sushi":"Fish", "Spaghetti":"Beef", "Pizza":"Pepperoni"}

# values() will return a list of all the values in the dictionary
print(foodDictionary.values())

# The value of a specific item can be changed by referring to it's key
foodDictionary["Sushi"] = "Rice"
print(foodDictionary)

# We can also add items by using a new index key and giving it a value
foodDictionary["Pickle"] = "Cucumber"
print(foodDictionary)

# We can check if a key exists in the dictionary
if "Burger" in foodDictionary:
    print("Yes, there is a burger in the dictionary")
else:
    print("No, no burger in dictionary")

#OPERATORS
# symbols that define operation behaviors between data types

# Arithmetic operators:
# +, -, *, /, %(mod), **(exponent), //(floor division)

# Assignment operators:
# =, +=, -=, *=, /=, etc. there are others

# Comparison operators:
# ==, !=, >, <, >=, <=

# Logical operators:
# and, or, not

# Getting user input using the input() function
print("Please enter your name")
name = input()
# f stands for formatted string
# this allows us to parameterize our string
print(f"Hello {name}!")

favColor = input(f"What is your favorite color, {name}?")
print(f"I like {favColor} too!")

message_string = ''' This is a mulit-line string!
can you believe it?'''
print(message_string)