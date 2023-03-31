# if ,elif, else
# Conditional statements are used to accomadate different paths our code might take
# we use if statements to run code if a given condition is met

#my_bool = False

#if my_bool:
#    print("my bool is true")
#else:
#    print("my bool is flase")

# We can nest if statements:

#if some-condition:
#    if some-other-condition
#        ....
#    else:
#        ....
#else:
#    .... 

# Conditionals
# equals to: == 
# not equal to: !=
# less than: <
# more than: >
# less than or equal to: <=/>=

# Examples

#money = 1

#if money > 10:
#    print("i have some money")
#else:
#    print("i dont have much")

# Elif - else if 
# We dont always need to check if every statement evaluates to true
# mostly only one statement will be true
# elif makes our code more efficiant
# Will only run if no other statement has been evaluated as true

#temp = 5

#if temp >= 30:
#    print("its a very hot day")
#elif temp > 25:
#    print("its hot")
#elif temp > 20:
#    print("its ok")
#elif temp > 15:
#    print("could be beter")
#elif temp == 0:
#    print("its exactly freezing")
#else:
#    print("its cold")

# Exercise
# Ask for an input form a user for a grade/mark
# if the mark is greater than 85 print "distinction"
# if the mark is between 65 and 85 print "pass"
# anything else print "fail"
# DO this with just if statements first, then with elif statememts 

#x = int(input("enter a grade: "))

#if x >= 85:
#    print("distiction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# multiple comparators + with multiple conditions using and/or:

#deposit = 10
#password = "password1234"

#if 0 < deposit <= 100 and password == "password":
#    print(f"thank you for £{deposit} deposit!")
#else:
#    print("failed to deposit")

# not 

deposit = 0
password = "password"

if not (0 < deposit <= 100) or password != "password":
    print("failed to deposit")
else:
    print(f"thank you for £{deposit} deposit!")

# in and not in:

#name = "root"

#if name in ("root", "admin"):
#    print("this is not a valid username")
#else:
#    print(f"welcome {name}")

name = "root"

if name not in ("root", "admin"):
    print(f"welcome {name}")
else:
    print("invalid username")

# challenge
# Weight-converter app, convert a user inputted weight (float) and user to select \
# either kgs or lbs from a prompt. write an if statement that checks if the unit entered\
# is kgs or lbs. if kgs convert into lbs, and print converted weight. 
# Else statement to handle the other conversion.
# error handling - user should be able to enter lowercase or uppercase. 

weight = float(input("weight: "))
unit = input("K (kgs) or L for (lbs)")
if unit.upper() == "K": 
    converted = weight / 0.45
    print("weight in Lbs: ", converted)
else:
    converted = weight * 0.45
    print("weight in Kgs: ", converted) 












