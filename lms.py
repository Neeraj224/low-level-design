class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        # private attributes in Python are defined using a double underscore "__"
        self.__is_available = True
    
    def display_info(self):
        print(f"'{self.title}' by {self.author}, published in {self.year}")
        
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is currently unavailable.")
    
    def return_book(self):
        self.__is_available = True
        print(f"'{self.title} has been returned.'")

# by passing the name of a class to another class, we make
# sure that the current one we're defining inherits the one passed:
class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def display_info(self):
        print(f"'{self.title}' [Digital Edition] by {self.author} ({self.year}), {self.file_size} MB")

class Library:
    def __init__(self):
        self.books = {}
        self.authors = {}
        self.years = {}
    
    def add_book(self, book):
        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1
            print(f"{book.title} added to the library!")
            
            # now we check if we have any other by this book's author:
            if book.author not in self.authors:
                self.authors[book.author] = []
                self.authors[book.author].append(book.title)
            else:
                if book.title not in self.authors[book.author]:
                    self.authors[book.author].append(book.title)
            
            # we also check if any other book from the same year is available or not:
            if book.year not in self.years:
                self.years[book.year] = []
                self.years[book.year].append(book.title)
            else:
                if book.title not in self.years[book.year]:
                    self.years[book.year].append(book.title)
    
    def list_books(self):
        if not self.books:
            print("No book available in the library!")
        else:
            for book in self.books.keys():
                book.display_info()
    
    def list_books_by_author(self):
        if not self.authors:
            print("No authors available!")
        else:
            for author in self.authors.keys():
                print(f"{author}: {self.authors[author]}")
    
    def list_books_by_year(self):
        if not self.years:
            print("No books available for any year(s)")
        else:
            for year in self.years.keys():
                print(f"{year}: {self.years[year]}")

    def search_library(self, searchTitle = None, searchAuthor = None, searchYear = None):
        # search by title:
        if searchTitle:
            for book in self.books:
                if book.title == searchTitle:
                    if self.books[book] > 0:
                        print(f"'{book.title}' is available. We have {self.books[book]} copy(s).")
                        # TODO: Add a renting function
                        return
            else:
                print(f"'{searchTitle}' is not available in the library")
        
        # search by author returns the books available by that
        # particular author:
        if searchAuthor:
            for author in self.authors.keys():
                if author == searchAuthor:
                    print(f"{author}'s books: {self.authors[author]}.")
                    return
            
            print(f"We have no books by {searchAuthor}.")
            return
        
        # search by year returns the books taht were published in that
        # particular  year:
        if searchYear:
            for year in self.years.keys():
                if year == searchYear:
                    print(f"Books published in {year}: {self.years[year]}.")
                    return
            
            print(f"We have no books published in the year {searchYear}.")
            return


def main():
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill A Mockingbird", "Harper Lee", 1960)
    book3 = Book("A Midsummer Day's Nightmare", "Miriam Shakespeare", 1949)
    book4 = Book("Match 22", "Broseph Teller", 1949)
    # book1.display_info()
    # book2.display_info()
    
    dBook1 = DigitalBook(book1.title, book1.author, book1.year, 20)
    # dBook2 = DigitalBook("The Pragmatic Programmer", "Andy Hunt", 1999, 1.2)
    # dBook1.display_info()
    # dBook2.display_info()
    
    atkins = Library()
    atkins.add_book(book1)
    atkins.add_book(book2)
    atkins.add_book(book3)
    atkins.add_book(book4)
    atkins.add_book(Book("Go Set A Watchman", "Harper Lee", 2015))
    atkins.add_book(Book("Go Set A Watchman", "Harper Lee", 2015))
    
    # atkins.list_books()
    atkins.list_books_by_author()
    atkins.list_books_by_year()
    
    # search books
    atkins.search_library(searchTitle = "1984")
    atkins.search_library(searchAuthor = "Harper Lee")
    atkins.search_library(searchYear = 1949)
    atkins.search_library(searchTitle = "Yellow Submarine")
    atkins.search_library(searchAuthor = "Anais Nin")
    atkins.search_library(searchYear = 1992)
    atkins.search_library(searchTitle = "Go Set A Watchman")

if __name__ == "__main__":
    main()
