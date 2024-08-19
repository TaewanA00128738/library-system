
import unittest
from main import LibrarySystem, User, Book

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.library_system = LibrarySystem()
        self.user = self.library_system.create_account("John Doe", "1234567890", "john.doe@example.com", ("123", "Main St", "Anytown", "AT", "12345"))
        self.library_system.add_book("Python Programming")
        self.library_system.add_book("Data Science with Python")

    def test_create_account(self):
        self.assertEqual(len(self.library_system.users), 1)
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.contact, "1234567890")
        self.assertEqual(self.user.email, "john.doe@example.com")

    def test_add_book(self):
        self.library_system.add_book("New Book")
        self.assertEqual(len(self.library_system.books), 3)

    def test_borrow_book(self):
        self.library_system.borrow_book(self.user, "Python Programming")
        book = self.library_system.search_book("Python Programming")
        self.assertEqual(book.status, "not available")
        self.assertIn(book, self.user.borrowed_books)

    def test_borrow_nonexistent_book(self):
        self.library_system.borrow_book(self.user, "Nonexistent Book")
        # No assertion here since the method just prints an error message

    def test_return_book(self):
        self.library_system.borrow_book(self.user, "Data Science with Python")
        self.library_system.return_book(self.user, "Data Science with Python")
        book = self.library_system.search_book("Data Science with Python")
        self.assertEqual(book.status, "available")
        self.assertNotIn(book, self.user.borrowed_books)

    def test_return_nonexistent_book(self):
        self.library_system.return_book(self.user, "Nonexistent Book")
        
if __name__ == "__main__":
    unittest.main()