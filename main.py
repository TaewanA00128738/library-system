class LibrarySystem:
    
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
                pass
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