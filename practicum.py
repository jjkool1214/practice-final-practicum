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
        return self.__title + " written by " + self.__author + ' (' + self.__publication_year + ')'
    
    def __repr__(self):
        return self.__title + " written by " + self.__author + ", published in " + self.__publication_year
        
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publication_year(self):
        return self.__publication_year
     

class Library:
  pass

def organize_library(library:Library) -> None:
   pass

def main():
    """
    Use this function to manually test your code (if needed)
    """

if __name__ == "__main__":
    main()
