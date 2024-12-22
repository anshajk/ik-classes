"""
Encapsulation is a mechanism of restricting access to some of the object's components and protecting the object's internal state.
This is achieved by using private attributes and methods.

In Python, encapsulation is implemented using public, protected, and private variables:
- Public variables: Accessible from anywhere. By default, all variables are public.
- Protected variables: Indicated by a single underscore (_). They should not be accessed directly outside the class, but it is still possible.
- Private variables: Indicated by a double underscore (__). They cannot be accessed directly outside the class and are name-mangled to prevent accidental access.
"""


class Book:
    """
    A simple class to represent a Book with encapsulation.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    year (int): The year the book was published.
    """

    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def get_details(self):
        """Method to get the details of the book."""
        return f"'{self.__title}' by {self.__author}, published in {self.__year}"

    def set_title(self, title):
        """Method to set the title of the book."""
        self.__title = title


# Creating an object of the Book class
my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(my_book.get_details())
my_book.set_title("Go Set a Watchman")
print(my_book.get_details())
