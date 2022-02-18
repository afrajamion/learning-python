'''
Create a book class, and initialise each book object with author, title, 
ISBN, year of publication and number of pages. Define a str method which 
displays information about the book, and a search method which searches
by book or by author, through a dictionary attribute of the class which 
tracks the book objects created. Define two subclasses for different genres 
of books which override the default str method. As a stretch goal, also
implement a method which checks whether an ISBN is valid
'''
def titlecase(string):
    return ' '.join([word.capitalize() for word in string.split()])

class Book():
    books = {}
    def __init__(self, title, year, pages, isbn, author = "Unknown"):
        self.title = titlecase(title)
        self.author = author.title()
        self.published = year
        self.pages = pages
        self.isbn = isbn
        if self.author in Book.books:
            Book.books[self.author].append(self)
        else:
            Book.books[self.author] = [self]
    
    #search method
    @staticmethod
    def search_books(search_term, search_by = 'author'):
        if search_by == 'author':
            results = Book.books.get(search_term.title(), [])
            return f"Books by {search_term.title()}: {','.join([book.title for book in results]) if results else 'None'}"
        else:
            title = titlecase(search_term)
            for author, books in Book.books.items():
                if title in [book.title for book in books]:
                    return f"Book \'{title}\' was written by {author}"
            return f"Book \'{title}\' not found"

    def valid_isbn(self):
        digits = ''.join(self.isbn.split('-'))
        if len(digits) != 13:
            return False
        diglist = [int(digit) for digit in digits]
        return diglist[-1] == (10 - (sum([diglist[i] if i % 2 == 0 else 3 * diglist[i] for i in range(12)]) % 10) % 10) # second % 10 accounts for case sum(...) % 10 = 0

    def __str__(self):
        return f"First published in {self.published}, {self.title} was written by {self.author}.\nPages: {self.pages}\nISBN: {self.isbn}"

#subclasses of books
class FantasyNovel(Book):
    def __str__(self):
        return f"First published in {self.published}, {self.title} is an epic fantasy novel written by {self.author}.\nPages: {self.pages}\nISBN: {self.isbn}"

class ScifiNovel(Book):
    def __str__(self):
        return f"First published in {self.published}, {self.title} is a gripping Sci-Fi novel written by {self.author}.\nPages: {self.pages}\nISBN: {self.isbn}"

#Examples of using the init, str and valid_isbn methods for each of our classes
example_book = Book("other minds", 2017, 255, "978-0-00-822629-9", "peter godfrey-smith")
print(example_book)
print(f"Valid ISBN: {example_book.valid_isbn()}")

hobbit = FantasyNovel("the hobbit", 1937, 310, "978-0-00-745842-4", "j.r.r. tolkien")
print(hobbit)
print(f"Valid ISBN: {hobbit.valid_isbn()}")

timemachine = ScifiNovel("the time machine", 1895, 128, "978-0-14-119934-4", "h.g. wells")
print(timemachine)
print(f"Valid ISBN: {timemachine.valid_isbn()}")

print(Book.search_books('j.r.r. tolkien'))
print(Book.search_books('the time machine', 'book'))
print(Book.search_books('jSFVQJFV'))
print(Book.search_books('fbEF', 'book'))