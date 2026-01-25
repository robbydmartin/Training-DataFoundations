# Python is an object oriented programming language.
# it makes use of classes and objects to create our systems and applications
# Classes are the blueprints, objects are generated based on those blueprints.

class Animal:

    # In python, we have to override the __init__() function to create our constructor
    # Notice this is DOUBLE underscore, both before and after
    # Double leading and trailing underscores are used for special methods that
    # Python calls automatically in certain situations (__init___, __str__(), __len__(), etc.)


    # Passing in self references our freshly created object in our constructor
    def __init__(self, name, age):
        self.name = name
        self.__age = age # double underscores means private property
    
    # Getter for private properties only
    def get_age(self): return self.__age
    # Setter for private properties only
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than zero")

    def speak(self):
        print(f"{self.name} made a noise")

    def introduction(self):
        return f"My name is {self.name}, I am {self.get_age()} year(s) old"

Bob = Animal("Bob", 3)
print(Bob.name)
print(Bob.get_age())
print(Bob.speak())

# PILLARS OF OOP: Abstraction, Inheritance, Polymorphism, and Encapsulation
# Abstraction - the idea of showing only what the user needs to know and hiding the implementation details
# Inheritance - child classes can reuse and extend the behaviour of our parent classes
# Polymorphism - (many forms) meaning one interface but multiple implementations
# Encapsulations - the practice of bundling data/attributes and methods into a single unit and
#   restricting access to some of the object's components

# INHERITANCE DEMO: inheriting from Animal class
class Dog(Animal):

    def __init__(self, name, age, breed, color="Brown"): # using the equals will apply a defaut value for the parameter
        super().__init__(name, age)
        #self.name = name
        #self.age = age
        self.breed = breed
        self.color = color

    # Polymorphism example - we are overriding the definition of the speak function
    def speak(self):
        return f"{self.name} barked at the mailman!"
    
    # __str__ acts as our toString() method
    def __str__(self):
        return f"My name is {self.name}, I am a {self.color} {self.breed}"
    
Major = Dog("Major", 7, "German Shepherd", "Black")
print(Major) # with the __str__ method, this will now return our formatted string
print(Major.speak())

class Other():
    def __init__(self, place, time):
        self.place = place
        self.time = time


class Cat(Dog, Other):
    def __init__(self, name, age, breed, color, place, time, hairLength):
        # using the super method we can call the parent class constructor
        super().__init__(name, age, breed, color)
        super().__init__(place, time)
        self.hairLength = hairLength

    def scratch(self):
        return f"{self.name} has scratched the door frame"
    
    def speak(self):
        return f"{self.name} meowed at the door!"
    
Ash = Cat("Ash", 2, "Maine Coone", "Gray", "Medium Hair", "here", "Now")
print(Ash.scratch())
print(Ash.speak())
#print(Ash.__age) throws an error because the property is private
print(Ash.get_age())
Ash.set_age(3) # change the age
print(Ash.get_age())
print(Ash.time)
