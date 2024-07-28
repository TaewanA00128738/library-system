import re
from datetime import datetime, timedelta

class User:
    def __init__(self, name, contact, email, address):
        self.name = name
        self.contact = contact
        self.email = email
        self.address = address

class LibrarySystem:

    def __init__(self):
        self.users = []

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
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "0":
                print("Exiting the Library System. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.display_menu()