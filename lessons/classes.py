# Classes and methods is part of OOP - object orientated programming. 
# Key concepts:
# Class - a blueprint of attributes(variabes) and method(functions) which \ 
# we can use to make objects.
# Objects - is an instance of a class
# method - functions attached to the class
# Allows us to easily make multiple objects of the same type.
# if we wanted to model a class of students if we idnt use Classes we would neeed \
# unique variables for each student. 

class Dog: # Creates a class called dog.
    energy = "high" # Setting an attribute for the class.

    def speak(self): # creeates a method.
        print("bark!")

fido = Dog() # sets fido as an object of the class Dog. 

# redefine attribute
fido.energy = "low"

print(fido.energy)# call the attribute energy
fido.speak() # Calling the method

###

class Students: # note - no parenthesis
    pass

student_1 = Students()
student_2 = Students()

print(student_1) # returns it is an object of class Students and its memory location.

student_1.first = "john"
student_1.last = "smith"
student_1.age = 10

print(student_1.first, student_1.last)

student_2.first = "katie"
student_2.last = "smith"
student_2.age = 11

print(student_2.age)

# What if we had to do this for 30 students

# lets try:

class Student:
    def __init__(self, first, last, age): # __indicates a backgound taks__
        self.first = first                # init initialises the object with these attributes.
        self.last = last                  # self param refers to the object itself
        self.age = age                    # The object itself is passed as the first arg.
                                          # self maps the class data to the object data.
student_3 = Student("john", "smith", 10)
student_4 = Student("katie", "smith", 11)

print(student_3.age, student_4.age)

class Student1:
    def __init__(self, first, last, age): 
        self.first = first                
        self.last = last                  
        self.age = age
        self.full = first + " " + last           

student_5 = Student1("john", "smith", 10)
student_6 = Student1("katie", "smith", 11)

print(student_5.full+",",student_6.full)


# with a method

class Student2:
    def __init__(self, first, last, age): 
        self.first = first                
        self.last = last                  
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

student_7 = Student2("john", "smith", 10)
student_8 = Student2("katie", "smith", 11)

print(student_7.fullname())
print(Student2.fullname(student_8))

# change value of a attribute

class Student3:
    def __init__(self, first, last, age): 
        self.first = first                
        self.last = last                  
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + 1)

student_9 = Student3("john", "smith", 10)
student_10 = Student3("katie", "smith", 11)

print(student_9.age)
student_9.change_age()
print(student_9.age)

# Using a self-class variable

class Student4:

    age_increase_amount = 25 # self class variable

    def __init__(self, first, last, age): 
        self.first = first                
        self.last = last                  
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_11 = Student4("john", "smith", 10)
student_12 = Student4("katie", "smith", 11)

student_11.change_age()
print(student_11.age)

print(student_11.age_increase_amount)
print(Student4.age_increase_amount)

# __dict__

print(Student4.__dict__)
print(student_11.__dict__)

# change the variable

Student4.age_increase_amount = 20
student_12.age_increase_amount = 15

print(Student4.age_increase_amount)
print(student_11.age_increase_amount)
print(student_12.age_increase_amount)

print(student_11.__dict__)
print(student_12.__dict__)

# non self class variable

class Student5:

    age_increase_amount = 25 # self class variable
    num_of_students = 0

    def __init__(self, first, last, age): 
        self.first = first                
        self.last = last                  
        self.age = age

        Student5.num_of_students += 1     

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_13 = Student5("john", "smith", 10)
student_14 = Student5("katie", "smith", 11)

print(Student5.num_of_students)

# enscapsulation - the methods + attributes can only be called by objects of the class.
# They are  not available to anything else in the program. 
# Abstraction - child class can implement its own specific use of a method from its \
# parent class. 
# inheritance - a parent class provides a method tha applies to all child classes.
# Polymorphism - child class is a type of the parent class. it can be treated as an object
# of its parent class. 


# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

# Child class
class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species) 
        self.breed = breed

    def meow(self):
        print("Meow")

my_cat = Cat("Whiskers", "feline", "siamese")

my_cat.meow()
my_cat.eat()

print(my_cat)

# __str__ - This method return a string representation of the object.
# usuful for debugging and prining info on the object

class Animal1:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} ({self.species})"

# Child class
class Cat1(Animal1):
    def __init__(self, name, species, breed):
        super().__init__(name, species) 
        self.breed = breed

    def meow(self):
        print("Meow")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed})"    

my_cat1 = Cat1("Whiskers", "feline", "siamese") 

my_cat1.meow()
my_cat1.eat()

print(my_cat1)

# Leading and trailing underscores:
# _money = 100 - single leading underscore signifes the variable is private. 
# type_ or print_ or class_ - avoid conflicts with keywords in python. 
# double leading underscore - name mangling - avoids collisios if our class is extended.
# attribute not accesible without the class name. 
# we access them _ClassName__attributeName. 

class Feline:
    __family = "Felidae"

cat2 = Feline()

print(cat2._Feline__family)
