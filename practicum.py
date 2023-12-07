"""
Implement your solution to the practicum in this file.

@author Your Name
"""
class Book:
    __slots__ = ['__title', '__author', '__publication_year']
    def __init__(self, title, author, publication_year):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year

    def __str__(self):
        return self.__title + " by " + self.__author + ' (' + str(self.__publication_year) + ')'
    
    def __repr__(self):
        return self.__title + ", a book by " + self.__author + ", published in " + str(self.__publication_year) + '.'
        
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publication_year(self):
        return self.__publication_year
    
    def __gt__(self, other):
        if self.__author != other.__author:
          return ord(other.__author[0]) < ord(self.__author[0])
        return ord(other.__title[0]) < ord(self.__title[0])        
     

class Library:
  __slots__ = ['__name', '__books']
  def __init__(self, name) -> None:
      self.__name = name
      self.__books = {} # title:book

  def is_empty(self):
      return len(self.__books.keys()) == 0
  
  def get_name(self):
      return self.__name
  
  def get_books(self):
      return self.__books
  
  def reload(self, books):
      for book in books:
          self.__books[book.get_title()] = book

  def check_out(self, title, author):
      if self.is_empty():
          return None
      for titles in self.__books.keys():
          if title == titles and self.__books[titles].get_author() == author:
              del self.__books[title]
              return self.__books[title]
      return None
  
  def return_book(self, book):
      self.__books[book.get_title()] = book

  

def organize_library(library:Library) -> None:
   pass

def main():
    book_1 = Book('grah', 'you', 1999)
    book_2 = Book('brah', 'you', 1932)
    book_3 = Book('gvbue', 'abc', 1923)
    books = [book_1, book_2, book_3]
    print(sorted(books))

if __name__ == "__main__":
    main()
