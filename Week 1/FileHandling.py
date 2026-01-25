import os

# File handling refers to the process of creating, opening, reading, writing,
# and deleting files using python.
# Python has built-in funcitons and methods that make this easy!

# Important to know for data persistance and processing
#   - automation for many real-world tasks
#   - handling large data sets

# open() - is the key function and takes two parameters: filename and mode
# 4 different modes available:
#   "r" - read; the default mode for reading and throws an error if the file does not exist
#   "a" - append the end of a file and it creates the file if it does not exist
#   "w" - write and if a file alread has data, it will be overwritten
#   "x" - create; returns an error if the file fails to create (e.g. file path incorrect, etc.)

# We can determine if the file should be handled as binary or text using "b" and " t" respectively

# create a new file
#myFile = open('./Week 1/Resources/MyNewFile.txt', "x") # mode is always passed in as a string
#mySecondFile = open('./Week 1/Resources/MySecondFile.txt', "+w")

myFile = open('./Week 1/Resources/MyNewFile.txt', "r") # open in read mode
#print(myFile.read())

# rad a single line, calling it again will read the next line
#print(myFile.readline())
#print(myFile.readline())
#print(myFile.readline())

# we can also specify to only read the first x characters
# read functions will also keep track of where we are
#print(myFile.read(3))
#print(myFile.read(4))

# it is best practice to clse a file once we are done with it.
#myFile.close()

# We can access files using exact paths
# We can use the 'with' statement to automatically close the file after its suite finishes
with open('C:/Users/rober/OneDrive/Documents/Revature/Training-DataFoundations/Training-DataFoundations/Week 1/Resources/MySecondFile.txt', "r") as myfile:
    print(myFile.read())
#print(myFile.read()) this will cause an error since it is not in the with block

pokemonTeam = []

# for p in range(6):
#     pokemon =  input("Enter a Pokemon for your team: ")
#     pokemonTeam.append(pokemon)

# with open('./Week 1/Resources/myPokemonTeam.txt', "+w") as teamFile:
#     for p in pokemonTeam:
#         teamFile.write(p + "\n") # write each pokemon to a new line
#     print("Your pokemon has been saved!")

with open('./Week 1/Resources/myPokemonTeam.txt', "r") as teamFile:
    print("Your Pokemon team consists of: ")
    print(teamFile.read())

# it is best practice to check if a file exists before trying to delete it
if os.path.exists('./Week 1/Resources/mySecondFile.txt'):
    os.remove('./Week 1/Resources/mySecondFile.txt')
    print("File deleted successfully")
else:
    print("Something went wrong, file was not deleted")

