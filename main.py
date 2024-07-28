import re
from datetime import datetime, timedelta

class User:
    def __init__(self, name, contact, email, address):
        self.name = name
        self.contact = contact
        self.email = email
        self.address = address
        self.borrowed_books = []

class Book:
    def __init__(self, name, status="available"):
        self.name = name
        self.status = status

class LibrarySystem:
    def __init__(self):
        self.users = []
        self.books = []
        self.borrow_history = []

    def create_account(self):
        name = input("Enter your name: ")
        contact = input("Enter your contact number (10 digits): ")
        while not re.match(r'^\d{10}$', contact):
            print("Invalid contact number format. Please enter 10 digits.")
            contact = input("Enter your contact number (10 digits): ")

        email = input("Enter your email: ")
        while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            print("Invalid email format. Please enter a valid email.")
            email = input("Enter your email: ")

        street_number = input("Street Number: ")
        street_name = input("Street Name: ")
        city = input("City: ")
        state = input("State: ")
        postal_code = input("Postal Code: ")

        address = (street_number, street_name, city, state, postal_code)
        user = User(name, contact, email, address)
        self.users.append(user)
        print("Account created successfully.")
    
    def search_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        return None

    def borrow_book(self, user, book_name):
        book = self.search_book(book_name)
        if book and book.status == "available":
            book.status = "not available"
            user.borrowed_books.append(book)
            borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.borrow_history.append({'title': book.name, 'borrow_date': borrow_date, 'return_date': None})
            print(f"{user.name} has successfully borrowed {book.name}.")
        elif book and book.status == "not available":
            print(f"Sorry, {book.name} is not available.")
        else:
            print(f"Book with name {book_name} not found.")

    def return_book(self, user, book_name):
        book = self.search_book(book_name)
        if book and book in user.borrowed_books:
            book.status = "available"
            user.borrowed_books.remove(book)
            return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.borrow_history.append({'title': book.name, 'return_date': return_date, 'borrow_date': None})
            print(f"{user.name} has successfully returned {book.name}.")
        elif not book:
            print(f"Book with name {book_name} not found.")
        else:
            print(f"You did not borrow {book.name}.")
    
    def display_menu(self):
        while True:
            print("\nLibrary System Menu:")
            print("1. Create an Account")
            print("2. Add a Book")
            print("3. Remove a Book")
            print("4. Borrow a Book")
            print("5. Return a Book")
            print("0. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_account()
            elif choice == "2":
                book_name = input("Enter the name of the book to add: ")
                self.books.append(Book(book_name))
                print(f"{book_name} added to the library.")
            elif choice == "3":
                book_name = input("Enter the name of the book to remove: ")
                book = self.search_book(book_name)
                if book:
                    self.books.remove(book)
                    print(f"{book_name} removed from the library.")
                else:
                    print(f"Book with name {book_name} not found.")
            elif choice == "4":
                contact_number = input("Enter your contact number: ")
                user = next((u for u in self.users if u.contact == contact_number), None)
                if user:
                    book_name = input("Enter the name of the book you want to borrow: ")
                    self.borrow_book(user, book_name)
                else:
                    print(f"User with contact number {contact_number} not found.")
            elif choice == "5":
                contact_number = input("Enter your contact number: ")
                user = next((u for u in self.users if u.contact == contact_number), None)
                if user:
                    book_name = input("Enter the name of the book you want to return: ")
                    self.return_book(user, book_name)
                else:
                    print(f"User with name {contact_number} not found.")
            elif choice == "0":
                print("Exiting the Library System. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.display_menu()