# Iteration is another word for loops, repeating a block of code over and over
# without having to write the code multiple times
# saves time

# 2 types of loops:
# While loop
# For loop 

# While loop
# A while loop will continue to execute code while a condition is true
# if the condition is never true the while loop will never start

print("1")
print("2")
print("3")

x = 0

while x <100:
    print(x)
    x += 1 # same as x = x + 1 

# break

i = 1

while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

# continue

j = 0

while j < 6:
    j += 1
    if j == 3:
        continue
    print(j)

k = 1
while k < 6:
    print(k)
    k += 1
else:
    print("k is no longer less than 6")

# For loops
# A for lop will iterate over any iterable collection - lists/strings/dictionaries
# Useful for when we want to use data in a collection
# Do something to individual elements in a collection

# iterating through lists

numbers = [1, 3, 5, 9]
for item in numbers:
    print(item)

# using a while loop:

l = 0
while l < len(numbers):
    print(numbers[l])
    l += 1 

# Change items

my_fruits = ["apple", "orange", "banana"]

for fruit in my_fruits:
    print(fruit.upper())

# Range function

for a in range(5):
    print(a) # 0-4 (stops at 5) 

for a in range(1,5):
    print(a) # 1-4

for a in range(1,10,2):
    print(a) # 1 to 9 in steps of 2 

# strings

for x in "hello":
    print(x)

for word in "hello world".split():
    print(word)

# List comprehenshion

result = [x**2 for x in range(5)]
print(result)

#same as:

results = []
for x in range(5):
    results.append(x**2)
print(results)

# Dictionary iteration

for i in {"drink": "wine"}:
    print(i)

for value in {"food": "jam"}.values():
    print(value)

for key, value in {"shape": "square"}.items():
    print(key, value)

# break and continue

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break

# nested loops

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i*j)

# write a while loop which asks for the names of 5 people,
# for each person print their name followed the text "is great!"        

counter = 0

while counter < 5:
    name = input("please enter a name: ")
    print(name + " is great!")
    counter += 1 




