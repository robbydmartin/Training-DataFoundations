# IN python we can have NAMED tuples
# They allow you to access thier elements by name index
# Named tuples are part ot the collections module and provide a way to create
#   self-documenting, immutable data structures
# GOOD FOR: reading an object or jows from SQL queries, CSVs, or API responses

from collections import namedtuple, OrderedDict, Counter

# To create a named tuple, we use the namedtuple() factory function
Point = namedtuple('Point', ['x', 'y'])

# We can create an instance of point
p = Point(x=1, y=5)

# Access using field name
print(p.x, p.y)

# Access items using index
print(p[0])

# Access using getattr() function
# pass in the namedtuple object and the attribute to get
print(getattr(p, 'y')) 

# MORE PRECISE EXAMPLE:
User = namedtuple('User', ['id', 'username', 'password', 'email'])

myUser = User(12, 'JonDoe', 'password', 'jondoe@email.com') # create an instance of the User factory func
mySecondUser = User(88, 'JaneDoe', 'something', 'janesemail@email.com')
print(myUser.username, myUser.password)
print(mySecondUser.username, mySecondUser.password)

########################################################

# Ordered Dictionaries
#   are good for when you are using items in a specific order
#   great for configuration settings or environment variables
#   also from the collections module

config = OrderedDict()

# Set defaults:
config["timeout"] = 5
config["retries"] = 3
config["two-factor"] = True

# We CAN override values that are already set
config["timeout"] = 10

# Set certain items to always be considered last
config.move_to_end("timeout")

# We can actully inspect the order of the dict
for key, value in config.items():
    print(key, value)

###############################################################

# Counters
# counters allow us to count things without writing loops
# comes from the collections module

words = ["fruit", "meat", "veggies", "dairy", "grains", "legumes", "fruit", "fruit", "dairy"]
count = Counter(words)
print(count)

# We can also specify what we want to count
print(count["fruit"])

K =2
word_lst = ['banana', 'apple', 'banana', 'orange', 'apple', 'apple']

word_dict = OrderedDict()

for word in word_lst:
    word_dict[word] = word_lst.count(word)

for key, value in word_dict.items():
    print(key)
    K -= 1
    if K == 0:
        break
