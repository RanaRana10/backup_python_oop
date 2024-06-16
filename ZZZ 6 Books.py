class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        return [book.title for book in self.books]

    def register_member(self, member):
        pass

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def checkout(self):
        self.is_available = False

    def checkin(self):
        self.is_available = True

    def display_details(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass

class EBook(Book):
    def __init__(self, title, author, isbn, format):
        super().__init__(title, author, isbn)
        self.format = format

    def display_details(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Format: {self.format})"

# Create a library
my_library = Library("Central Library", "Main Street")

# Create books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
book2 = EBook("Python Crash Course", "Eric Matthes", "978-1-59327-603-4", "PDF")

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)

# List available books
print("Available Books:")
for book in my_library.books:
    if book.is_available:
        print(book.display_details())
