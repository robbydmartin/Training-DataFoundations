import Functions

print(Functions.myCat)

# Control flow statements in Python

# For
loopPets = ["Herman", "Flags", "Leonard", "Olivia"]

# loops through a collection of items
# for x in collection, do something
for pet in loopPets:
    print(pet)

# While
# good for execution while a condition is true
count = 0
while (count < 5):
    print("from the while loop")
    count += 1

# We can nest loops and mix&match
# BUT, if you find yourself using 3 or more loops deep, there is likely a better way

# If-else
# we can check a condition(s) and execute a block of code based on the output(true/false)
# be careful! Python relies on indentation to know where the blocks of code end
cheese = 6
if cheese > 5:
    print("Cheese is the greatest!")
else:
    print("Cheese is NOT the greatest.")

# We can check multiple conditions using elif
# this will execute the FIRST true block and skip the rest
# good for checking multiple Mutually Exclusive conditions
score = 33

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else: # else catches anything that is not caught by the previous conditions
    print("Grade F")

# Shorthand if/else
a = 7
b = 9
c = 70

if a > b: print("a is greater than b")
print("a is my favorite") if a > b else print("b is my favorite")

# Multiple conditions using our logical operators
if a > b and c > a:
    print("Both conditions are true")
if a > b or c < a:
    print("At least one condition is true")
if not a < b:
    print("a is not less than b")

if a > 5:
    print("a is more than 5")
    if a > 10:
        print("and more than 10")
    else:
        print("but not more than 10")

# Match-case (known as switch statements in other languages)
choice = input("select a number betwee 1 and 3: ")
match choice:
    case "1":
        print("you chose case number 1")
    case "2":
        print("you chose case number 2")
    case "3":
        print("you chose case number 3")
    case _: # the default case if none above are true
        print("you did not follow directions!")

