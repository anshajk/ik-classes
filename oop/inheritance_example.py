"""
Inheritance is a mechanism in which one class inherits the attributes and methods of another class. 
The class that inherits is called the subclass, and the class being inherited from is called the superclass.
"""

from simple_class import Book


class EBook(Book):
    """
    A class to represent an EBook, inheriting from the Book class.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    year (int): The year the book was published.
    file_size (float): The size of the ebook file in MB.
    """

    def __init__(self, title, author, year, file_size):
        """
        The constructor for the EBook class.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
        file_size (float): The size of the ebook file in MB.
        """
        super().__init__(title, author, year)
        self.file_size = file_size

    def display_details(self):
        """Method to display the details of the ebook."""
        print(
            f"'{self.title}' by {self.author}, published in {self.year}, file size: {self.file_size}MB"
        )


# Creating an object of the EBook class
my_ebook = EBook("1984", "George Orwell", 1949, 1.5)
my_ebook.display_details()
