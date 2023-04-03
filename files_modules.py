# Modules
# Module are python files that we can use to extend our functionality of our scripts.
# We can import existing modules or create our own
# Many are built-in and do not require any set up.
# some are included in modules and some need to be installed with pip 

#import math # importing the whole math module

#number = float(input("enter a number: "))

#answer = math.sqrt(number) # syntax for referencing an object from a module (mod-name.object-name)

#print(answer)

# import multiple modules

#import math 
#import random


#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi) # pi * a random number rounded up. 

#for i in range(5):
#    print(random_pi())

# Just with requried objects (save memory + performance)

#from math import pi, ceil, floor
#from random import randint

#def random_pi():
#    return floor(randint(1,10) * pi) # objects can be called without module now. 

#for i in range(5):
#    print(random_pi())

# pip 
# install modules that require installation
# can search https://pypi.org - modules published by community 
# pip needs to be installed - sudo apt install python3-pip

#import requests

#print(requests.get("https://google.com"))

# if installing lots of modules for different applications its best to use a virtual enviroemnt.
# this prevent any modules affecting python system wide. - ie its isolated. 
# (we will do this tomorrow)

# exercise:
# create 2 files, in 1 (call it dice.py) write a function what will generate a random \
# number between 1 and 6. In a second file use the dice module to simulate throwing 2 dice and \
# print the value. 

# Files
# read, write, and edit files
# Python can work with most file types although may need to import/install modules
# we will focus on .txt files

# eg:

#file = open("filename.txt", "mode") # mode can be r (read-only), w (write), \
# r+ (read and write), a (append)

#file.close() # must close the file when finished. - this will close the most recently \
# opened file. 

# to read:
# open file and we use readline() - reads a line and moves on to the next line.
# read() - read all lines
# seek() - useful to make sure you are readin from start of file- file.seek(0)

#eg:

#file = open("example.txt", "r")

#print(file.readline()) # prints first line
#file.readline()
#print(file.readine()) # print third line
#file.seek(0) # returns to 1st line
#print(file.readline()) # prints first line

#file.close() # prints 1st, 3rd, 1st lines 

#file = open("lines.txt", "r")

#lines = file.readlines() # reads all lines at once and stores in a list. 
#print(lines)
#file.close()

# Writing files

#file = open("lines1.txt", "w")

#for n in range(1,11):
#    newline = "this is line" + " " + str(n) + "\n"
#    file.write(newline)

#file.close()

# Best way to edit:

#file = open("lines1.txt", "r")

#outfile = ""

#for line in range(1,10):
#    if line % 2 == 0: # takes even numbers
#        outfile += file.readline()
#    else:
#       file.readline() # skip over odd numbers

#file = open("lines1.txt", "w")
#file.write(outfile) # writes even numbers
#file.close()

# exercise:

# Open a new text file called teams.txt and add the names of 5 sports teams.
# Read and display the names of the 1st and 4th team in the file.
# Edit your teams.txt file so that the top line is replaced with "this is a new line"
# print out the edited file line by line.  

#1

file = open("teams.txt", "w")
sports_teams = ["man utd", "man city", "real madrid", "barcelona", "charlton"]

for i in sports_teams:
    newline = i + "\n"
    file.write(newline)

file.close()

#2 

file = open("teams.txt", "r")

lines = file.readlines()

print(lines[0].strip()) # removes whitespace
print(lines[3].strip())

file.close()








