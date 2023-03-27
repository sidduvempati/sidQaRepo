# Different ways of storing data
# Lists - ordered, mutable, collection of values
# Dictionaries - unordered, mutable, collection of key-value pairs
# Tuple - ordered, immunatble, collection of values. 
# sets - unordered, mutable, collection of unique values.

# mutable can be changed, immutable cant be changed. 

# lists - multiple values contained in a single variable, defined by square \
#           brackets with commas [,]. 

colours = ["blue", "red", "green", "yellow"]

print(colours)

# Referencing - elements in a list are referenced by their position (or index) \
#                this starts from position 0. Backwards would be -1.

print(colours[0])
print(colours[-4])

# sub-list of items by slicing, up to but not including the second number. 

print(colours[0:2])
print(colours[1:])

# Altering lists using index and new value, delete with del keyword

food = ["bread", "cheese", "pasta", "apple"]
food[0] = "rice"
del food[1]
print(food)

# Checking if an item is in a list
print("pasta" in food)
print("orange" in food)

# Nested lists

numbers = [1, 2, 3, 4]
letters = ["a", "b", "c", "d"]
combined = [numbers, letters]
print(combined[0][1], combined [1][1])

# Lists can contain multiple data types

my_list = ["red", 5, ["green", "apple"], 10]
print(my_list)
print(my_list[2][0])
print(my_list[0])

# list methods

# append
my_fruits = ["apple","orange", "kiwi"]
my_fruits.append("pear")
print(my_fruits)

# Remove

my_fruits.remove("apple")
print(my_fruits)

# Insert
my_fruits.insert(0, "mango")
my_fruits.insert(1, "melon")
print(my_fruits)

# Extend with a list
my_fruits.extend(["grape", "cherry"])
print(my_fruits)

# Finds index
print(my_fruits.index("orange"))

# Reverse
my_fruits.reverse()
print(my_fruits)

# Sort

my_fruits.sort()
print(my_fruits)

my_fruits.sort(key=len)
print(my_fruits)

# join

x = ", ".join(my_fruits)
print(x)

# dictionaires - defined {}

# similar to list but no index.
# keys have to be unique, values dont

drinks = {"fizzy": "sprite", "still": "water", "juice":"orange", "alcoholic":"beer"}
print(drinks)
print(drinks["still"])
# Can only query keys not values

# add an item
drinks["non-alcoholic"] = "water"
print(drinks)

# Overwrite 

drinks["non-alcoholic"] = "squash"
print(drinks)

# Return all keys or values
print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())
print("still" in drinks)

# Get method - returns the value for key else defaults
print(drinks.get("still", "not-found"))
print(drinks.get("stille", "not-found"))
print(drinks.get("stille"))

# update

drinks.update({"sugary": "cola"})
print(drinks)
#or
drinks.update(very_sugary = "red-bull")
print(drinks)

# pop

print(drinks.pop("non-alcoholic"))
print(drinks)
print(drinks.pop("non-alcoholic", "not-found"))