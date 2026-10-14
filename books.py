class Book:
    def __init__ (self, book_id:int, title:str, author:str, category:str, available_copies:int, copies:int):
        self.book_id = book_id
        self.title = title 
        self.author = author
        self.category = category
        self.available_copies = available_copies
        self._copies = copies

    def __str__ (self):
        return f"Book ID : {self.book_id}, its title: {self.title}, books author: {self.author}, book category: {self.category}, available copies: {self.available.copies}"

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value:int):
        if value < 0:
            raise ValueError("Number of copies canot be negative")
        self._copies = value