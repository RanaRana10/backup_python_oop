class Book:
    def __init__(self, title, author, total_copies, available_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1

            print(f"Book '{self.title}' by {self.author} borrowed successfully.")
        else:
            print(f"Sorry, '{self.title}' by {self.author} is not available right now.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"Book '{self.title}' by {self.author} returned.")
        else:
            print(f"All copies of '{self.title}' by {self.author} have been returned.")

# Create book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 5, 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3, 3)
book3 = Book("1984", "George Orwell", 7, 7)
book4 = Book("Pride and Prejudice", "Jane Austen", 4, 4)

# Borrow and return books
book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.borrow()
book4.borrow()
book3.return_book()
book2.return_book()