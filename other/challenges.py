# Password checker

def password_checker(password):
	x = ["password", "admin", "qwerty", "123456789"]
	if password in x:
		print(f"Use a safer password! {password} is compromised")
	else: 
		print(f"{password} is ok to use!")
password = input("Enter a password to check: ")
password_checker(password)

# Simple calc

def calc(x, y):
	sum = x + y
	sub = x - y
	mul = x * y
	print(f"sum is {sum}, sub is {sub}, multiply is {mul}")

x = int(input("Enter a number: "))
y = int(input("Enter second number: "))

calc(x, y)

# Highest number

def highest_number(a, b, c):
	if a > b and a > c:
	    print(f"{a} is highest")
	elif b > a and b > c:
		print(f"{b} is highest")
	else:
		print(f"{c} is highest")
highest_number(20, 25, 100)

# Even/odd

def even_odd(x):
	if x % 2 == 0:
		print(f"{x} is even")
	else:
		print(f"{x} is odd")

x = int(input("Enter a number: "))
even_odd(x)

# Text to upper

def convert(text):
	x = text.upper()
	print (x)
text = input("Enter a string: ")
convert(text)

# Radius-area

def circle_area(radius):
	area = 3.14*radius*radius
	return area
radius = float(input("Enter radius: "))
print(circle_area(radius))

# C to F degrees converter

degrees = float(input("Enter temp in degrees C: "))

def celcius_to_fahrenheit(degress):
    converted = (degrees * 1.8) + 32
    return(f"this is converted to {converted} in F")
print(celcius_to_fahrenheit(degrees))
