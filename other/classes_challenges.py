# Create a Rectangle class with attributes length and width. 
# Add methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 10)
print(rect.area())      
print(rect.perimeter()) 


# Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance


acct = BankAccount("1234")
print(acct.get_balance()) 
acct.deposit(100)
print(acct.get_balance()) 
acct.withdraw(50)
print(acct.get_balance()) 


# Create a Car class with attributes make, model, and year. 
# Add methods to get and set the values of the attributes.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

car = Car("Ford", "Focus", 2020)
print(car.get_make())  
car.set_make("Toyota")
car.set_model("Pickup")
car.set_year(1988)
print(car.get_make())  
print(car.get_model()) 
print(car.get_year())  
print(car)


# Create a Product class with attributes name, price, and quantity. 
# Add methods to calculate the total value of the product (price * quantity) 
# and add or remove items from the product inventory.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity
    
    def add_items(self, quantity):
        self.quantity += quantity
    
    def remove_items(self, quantity):
        if quantity > self.quantity:
            print("Insufficient quantity")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

prod = Product("MacBookPro", 1000, 5)
print(prod.total_value()) 
prod.add_items(2)
print(prod.quantity)      
prod.remove_items(3)
print(prod.quantity)     
prod.remove_items(5)
print(prod)      

# Books and Bookshelf challenge

class Book:
    def __init__(self, title, author, publisher, pub_year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pub_year = pub_year
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nPublication Year: {self.pub_year}"
        

class BookShelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = []
    
    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            print(f"{book.title} has been added to the shelf.")
        else:
            print("The shelf is full.")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the shelf.")
        else:
            print("That book is not on the shelf.")
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print("That book is not on the shelf.")
    
    def find_books_by_author(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        if not books:
            print("No books by that author are on the shelf.")
        else:
            return books
    
    def __str__(self):
        if not self.books:
            return "The shelf is empty."
        else:
            output = "Books on shelf:\n"
            for book in self.books:
                output += str(book) + "\n\n"
            return output

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "J. B. Lippincott & Co.", 1960)
book3 = Book("1984", "George Orwell", "Secker & Warburg", 1949)
book4 = Book("The Catcher in the Rye", "J. D. Salinger", "Little, Brown and Company", 1951)

shelf = BookShelf(3)
print(shelf)

shelf.add_book(book1)
shelf.add_book(book2)
shelf.add_book(book3)
shelf.add_book(book4)
print(shelf)

shelf.remove_book(book3)
print(shelf)

book = shelf.find_book_by_title("The Great Gatsby")
print(book)

books = shelf.find_books_by_author("J. D. Salinger")
if books is not None:
    for book in books:
        print(book)
else:
    print("No books found for that author.")