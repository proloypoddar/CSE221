class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True
        self.borrower = None
    def set_title(self, title):
        self.title = title
    def get_title(self):
        return self.title
    def set_author(self, author):
        self.author = author
    def get_author(self):
        return self.author
    def set_genre(self, genre):
        self.genre = genre
    def get_genre(self):
        return self.genre
    def set_availability(self, available):
        self.available = available
    def get_availability(self):
        return self.available
    def set_borrower(self, borrower):
        self.borrower = borrower
    def get_borrower(self):
        return self.borrower
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailable: {self.available}")
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.ame = name
        self.borrowed_books = []
    def get_member_id(self):
        return Book.member_id
    def get_name(self):
        return self.name
    def borrow_book(self, book):
        if book.get_availability():
            self.borrowed_books.append(book)
            book.set_availability(False)
            book.set_borrower(self)
        else:
           None
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_availability(True)
            book.set_borrower(None)
        else:
            None
    def display_borrowed_books(self):
        titles = []
        for book in self.borrowed_books:
            titles.append(book.get_title())
        return titles
class Library:
    def __init__(self):
        self.books_available = []
        self.library_members = []
    def add_library_member(self, member):
        self.library_members.append(member)
    def add_book(self, book):
        self.books_available.append(book)
    def display_book_list(self):
        print("All the books in library are:")
        for book in self.books_available:
            book.display_info()
            print("---------------")
    def display_library_members(self):
        print("Library Members:")
        for member in self.library_members:
            print(member.get_name())

# Driver code
book1 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fiction")
book2 = Book("Nothing Lasts Forever", "Sidney Sheldon", "Fiction")
book3 = Book("Calculus", "Gilbert Strang", "Education")

member1 = LibraryMember("LM01", "Tom Cruise")
member2 = LibraryMember("LM02", "Brad Pitt")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_library_member(member1)
library.add_library_member(member2)

member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book3)

library.display_book_list()
print("1======================================")
member1.display_borrowed_books()
print("2======================================")
member2.display_borrowed_books()
print("3======================================")
member1.return_book(book2)
print("4======================================")
member1.display_borrowed_books()
library.display_book_list()