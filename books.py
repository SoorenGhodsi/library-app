from datetime import date, datetime


class Book(object):
    def __init__(self, title, author, genre):
        today = date.today()
        self.title = title
        self.author = author
        self.genre = genre
        self.addDate = today.strftime("%B %d, %Y")
        
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

    def __str__(self):
        return 'Title: {}| Author: {}| Genre: {}|Date added: {}'.format(self.title, self.author, self.genre, self.addDate)

'''    
book1 = Book("James and the Giant Peach", "Roald Dahl", "Childrens")
print(book1.title)
print(book1.addDate)
print(book1)
'''       
