"""
Polymorphism is the ability to present the same interface for different underlying forms (data types).
In Python, this is achieved by method overriding and method overloading.
"""


class Book:
    def display_details(self):
        """Method to display the details of the book."""
        print("This is a book.")


class EBook(Book):
    def display_details(self):
        """Method to display the details of the ebook."""
        print("This is an ebook.")


class AudioBook(Book):
    def display_details(self):
        """Method to display the details of the audiobook."""
        print("This is an audiobook.")


# Demonstrating polymorphism
books = [Book(), EBook(), AudioBook()]

for book in books:
    book.display_details()
