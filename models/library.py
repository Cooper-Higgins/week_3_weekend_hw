from models.book import *

book1 = Book(1, "The Man Who Knew", "Sebastian Mallaby", "Autobiography", True)
book2 = Book(2, "Liar's Poker", "Michael Lewis", "Financial Journalism", False)
book3 = Book(3, "Reimagining Capitalism in a World on Fire", "Rebecca Henderson", "Sustainability", True)
library = [book1, book2, book3]

def add_new_book(book):
    library.append(book)

def burn_book(book_title):
    book_to_burn = None
    for book in library:
        if book.title == book_title:
            book_to_burn = book
            break

    library.remove(book_to_burn)
