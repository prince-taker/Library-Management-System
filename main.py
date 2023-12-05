# Prince Lesapo
from book import Book
from library import Library


def main():
    try:
        book1 = Book("Project Hail Marry", "Andy weir", "978-0593135228", "Science Fiction", "Available")
        book2 = Book("The House in the Cerulean Sea", "T.J. Klune", "978-0575415267", "Fantasy", "Checked Out")
        book3 = Book("The Midnight Library", "Matt haig", "978-1524797774", "Philosophical Fiction", "Available")
        book4 = Book("The Hate U Give", "Angie Thomas", "978-0062423520", "Young Adult Fiction", "Checked Out")
        book5 = Book("The Broken Earth", "N.K. Jemison", "978-0316333795", "Fantasy", "Available")

        books = Library()
        books.add_book(book1)
        books.add_book(book2)
        books.add_book(book3)
        books.add_book(book4)
        books.add_book(book5)

        books.return_book("978-0062423520")
        books.remove_book("978-0316333795")
        books.generate_available_books_report()
        books.generate_checked_out_books_report()
    except ValueError as v:
        print(v)


if __name__ == '__main__':
    main()
