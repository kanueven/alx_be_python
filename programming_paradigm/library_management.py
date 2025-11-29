class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # already returned

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []  # list to store books in the library
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self,title):
            for book in self._books:
                if book.title == title and not book._is_checked_out:
                    book.is_checked_out = True
                    return True
            return False
    def return_book(self,title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title ==title:
                if book.return_book():
                    return True
                else:
                    print("This book was not checked out.")
            else:
                print("Book not found in the library.")
            
        
    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(book)
        