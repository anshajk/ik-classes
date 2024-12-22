"""
This module demonstrates a simple class definition in Python.

A class is a blueprint for creating objects. Classes encapsulate data for the object and methods to manipulate that data.

An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
"""


class Book:
    """
    A simple class to represent a Book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    year (int): The year the book was published.
    """

    def __init__(self, title, author, year):
        """
        The constructor for the Book class.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        """Method to display the details of the book."""
        print(f"'{self.title}' by {self.author}, published in {self.year}")


# Creating an object of the Book class
# An object is an instance of a class. Here, 'my_book' is an instance of the Book class.
my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
my_book.display_details()
