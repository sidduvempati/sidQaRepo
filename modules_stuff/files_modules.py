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

from math import pi, ceil, floor
from random import randint

def random_pi():
    return floor(randint(1,10) * pi) # objects can be called without module now. 

for i in range(5):
    print(random_pi())

# pip 
# install modules that require installation
# can search https://pypi.org - modules published by community 
# pip needs to be installed - sudo apt install python3-pip

import requests

print(requests.get("https://google.com"))

# if installin glosts of modules for different application its best to use a virtual enviroemnt.
# this prevent any modules affecting python system wide. - ie its isolated. 
# (we will do this tomorrow)

# exercise:
# create 2 files, in 1 (call it dice.py) write a function what will generate a random \
# between 1 and 6. In a second file use the dice module to simulate throwing 2 dice and \
# print the value. 


