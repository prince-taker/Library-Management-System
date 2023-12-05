# Prince Lesapo

import re


class Library:
    def __init__(self):
        self.books = list()

    def add_book(self, book):
        """
        Takes a Book object as input and adds it to the library's collection.
        :param book: A book object.
        :return: None.
        """
        self.books.append(book)

    def remove_book(self, isbn):
        """
        Takes an ISBN as input and removes the corresponding book from the library's collection.
        :param isbn: ISBN for the book to remove.
        :return: None.
        """
        if not re.search(r"^[0-9]{3}-[0-9]+", isbn):
            raise ValueError("Provided ISBN is incorrect, please enter valid ISBN")

        found = False
        title = None
        for book in self.books:
            if isbn == book.book_isbn:
                found = True
                title = book.book_title
                self.books.remove(book)
                break

        if found:
            print(f"{title} with ISBN:{isbn} has been removed")
        else:
            print(f"Book with ISBN:{isbn}, not found on the library.")

    def check_out_book(self, isbn):
        """
        Takes an ISBN as input and checks out the corresponding book if it is available.
        :param isbn: ISBN of the book to check out.
        :return: None.
        """
        if not re.search(r"^[0-9]{3}-[0-9]+", isbn):
            raise ValueError("Provided ISBN is incorrect, please enter valid ISBN")

        found = False
        checked_out = False
        title = None
        for book in self.books:
            if book.book_isbn == isbn:
                found = True
                title = book.book_title
                if book.status.lower() == "available":
                    checked_out = True
                    book.status = "Checked Out"

        if found:
            if checked_out:
                print(f"{title} with ISBN:{isbn} has been successfully checked out.")
            else:
                print(f"{title} with ISBN:{isbn} has already been checked out.")
        else:
            print(f"Book with ISBN:{isbn}, not found on the library, consider adding it.")

    def return_book(self, isbn):
        """
        Takes an ISBN as input and returns the corresponding book.
        :param isbn: ISBN of the book returned.
        :return: None.
        """
        if not re.search(r"^[0-9]{3}-[0-9]+", isbn):
            raise ValueError("Provided ISBN is incorrect, please enter valid ISBN")

        found = False
        title = None
        for book in self.books:
            if book.book_isbn == isbn:
                found = True
                title = book.book_title
                book.status = "Available"

        if found:
            print(f"{title} with ISBN:{isbn} is now available to borrow.")
        else:
            print(f"Book with ISBN: {isbn}, is not on the library. Add the book to the library.")

    def generate_available_books_report(self):
        """
        Generates a report of all available books in the library.
        :return: None.
        """
        with open("available_books_report.txt", "w") as f1:
            for book in self.books:
                if book.status.lower() == "available":
                    f1.write(f"{book.book_title}, {book.book_author}, {book.book_isbn}, {book.genre} \n")

    def generate_checked_out_books_report(self):
        """
        Generates a report of all checked-out books in the library.
        :return: None.
        """
        with open("checked_out_books_report", "w") as f2:
            for book in self.books:
                if book.status.lower() == "checked out":
                    f2.write(f"{book.book_title}, {book.book_author}, {book.book_isbn}, {book.genre} \n")
