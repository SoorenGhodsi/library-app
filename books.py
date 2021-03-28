from datetime import date, datetime

class Book(object):
    def __init__(self, title, author, genre):
        today = date.today()
        self.title = title
        self.author = author
        self.genre = genre
        self.addDate = today.strftime("%B %d, %Y")
        self.lentTo = "*"
        
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
       self.__title = title
       
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
       self.__author = author
       
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
       self.__genre = genre
       
    def addDate(self):
        return self.__addDate
       
    @property
    def lentTo(self):
        return self.__lentTo

    @lentTo.setter
    def lentTo(self, name):
       self.__lentTo = name

    def __str__(self):
        return 'Title: {}| Author: {}| Genre: {}|Date added: {}|Is Lent? {}'.format(self.title, self.author, self.genre, self.addDate, self.isLent())

    def isLent(self):
        if(self.lentTo == "*"):
            return False
        return True

    def unLend(self):
        self.__lentTo = "*"
    
#checks if the string that is searched is in the title
    def matches(self, searchString):
        search = searchString.lower().trim()
        return search in self.title.lower().trim()

'''
book1 = Book("James and the Giant Peach", "Roald Dahl", "Childrens")
print(book1.title)
print(book1.addDate)
print(book1)
book1.genre = "YA"
book1.lentTo = "Jeremy"
print(book1)
print(book1.matches("James and "))
'''



#Sorts
def titleSort(books):
    newList = sorted(books, key=lambda book: (book.title, book.author, book.genre))
    return newList

def authorSort(books):
    newList = sorted(books, key=lambda book: (book.author, book.title, book.genre))
    return newList

def genreSort(books):
    newList = sorted(books, key=lambda book: (book.genre, book.title, book.author))
    return newList

'''
book1 = Book("James and the Giant Peach", "Roald Dahl", "Childrens")
book2 = Book("Harry Potter 1", "J.K Rowling", "YA")
book3 = Book("Harry Potter 2", "J.K Rowling", "YA")
book4 = Book("Harry Potter 3", "J.K Rowling", "YA")
book5 = Book("Divergent", "Veronica Roth", "Adult")

books = [book1, book2, book3, book4, book5]

for book in books:
    print(book)
    
bookTitles = titleSort(books)

for book in bookTitles:
    print(book)
    
bookAuthors = authorSort(books)

for book in bookAuthors:
    print(book)

bookGenres = genreSort(books)

for book in bookGenres:
    print(book)
'''


    



 
