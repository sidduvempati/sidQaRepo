# Function- a block of code that can either perform a task or return a value. 

def greet(name): # paramater which takes in arguments
    print(f"hi {name}")

greet("chris")

def greet1(first_name, second_name, age):
    print(f"{first_name} {second_name} is {age}")

greet1("chris", "reeves", 10)

# Better to use return as we can store in a variable, send to a file and print outside of the function.
# print inside - limits the resuablility of the function. 
# Avoid input() - or anything that relies on command line. 

def greeter(name):
    return(f"hello {name}")

x = greeter("chris")

print(x)

def greet2(name):
    return f"hello {name}"

name = input("enter name: ")
print(greet2(name))

# Default argument

def greet3(name, age=10): # default args must come as last arguments
    return f"{name} is {age}"

print(greet3("john"))
print(greet3("john", 20))

# Exercise: make a calc that just does addition of 2 numbers - using a function

def add_calc(num1, num2):
    x = num1 + num2
    return x

print(add_calc(5,5))

# *args
# if you do not know how many arguments that will be passed into your function, add a * before the param name
# It will recieve a tuple of arguments

def fruit_list(*fruits):
    print("The fruits are:")
    for fruit in fruits:
        print(fruit)

fruit_list("apple", "orange", "pear")

def numbers_list(*numbers):
    for i in numbers:
        print(i)

numbers_list(1,2,3,4,5,6)

# Keyword arguments - kwargs
# sends arguments as key = value therefore order does not matter
# we define the value when we pass the argument. 

def fruit_list1(fruit1, fruit2, fruit3):
    print(f"fav = {fruit1}")
    print(f"2nd fav = {fruit2}")
    print(f"3rd fav = {fruit3}")

fruit_list1(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")

# We also have **kwargs
# We use if we dont know how many keyword args there will be

def fav_food(**food):
    print("fav food is", food["fruit"], "not", food["dairy"])

fav_food(dessert = "ice-cream", dairy = "cheese", fruit = "blueberries") 

# passing a list as an arguemnt

def my_function(food):
    for x in food:
        print(x)

list1 = ["apple", "banana", "cherry"]

my_function(list1)

# format example - use {} as a plaeholder

name = "john"
age = 20
height = 1.7

print("my name is {}, i am {} years old, my height is {} meters".format(name, age, height))















