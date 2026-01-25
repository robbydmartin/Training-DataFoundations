class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says, \"Woof!\""
    
no_name = Animal("No name")
# no_name.speak() # Will raise the error

Bobo = Dog("Bobo")
print(Bobo.speak())

class Bird():
    def fly(self):
        return "Flying high!"
class Parrot(Animal, Bird):
    def speak(self):
        return f"{self.name} says, \"Squak!\""

Jiago = Parrot("Jiago")
print(Jiago.fly())
print(Jiago.speak())

class Cat(Animal):
    def speak(self):
        return f"{self.name} says, \"Meow!\""

Olivia = Cat("Olivia")
print(Olivia.speak())

pet_store = [Bobo, Jiago, Olivia, Cat("Toledo")]

for pet in pet_store:
    print(pet.speak())

iter_pets = iter(pet_store)
print(next(iter_pets).name)
print(next(iter_pets).name)
print(next(iter_pets).name)


### CUSTOM ITERATOR CLASS
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

numbers = [1, 2, 3, 4, 5]
my_iter = MyIterator(numbers)
for num in my_iter:
    print(num)

### GENERATORS
def square_numbers(nums):
    for num in nums:
        yield num * num # uses the keyword 'yield'

numbers = [1, 2, 3, 4, 5]
squares = square_numbers(numbers)
# This will return the square of each element in 'numbers'
for square in squares:
    print(square)

### ENUMERATE() FUNCTION
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
