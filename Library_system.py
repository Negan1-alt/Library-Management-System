from users import User
from books import Book
from ratings import Rating
from reading_history import ReadingHistory
class LibarySystem:
    def __init__(self):
        self.users = []
        self.books = []
        self.ratings = []
        self.reading_history = []
        self.recommendations = []

    def add_user(self, user:User):

        if any(u.email == user.email for u in self.users):
            print("this user is already used")
            return

        if '@' not in user.email:
            print("Email should have '@' on it")
            return

        if '.' not in user.email:
            print("Email should have '.' on it")

        self.users.append(user)
        print(f"User {user.name} added successffully")

    def display_users(self):
        if not self.users:
            print("no users found")
            return
        for user in self.users:
            print(user)

    def add_book(self, book:Book):
        if any(b.book_id == book.book_id for b in self.books):
            print(f"book with id {book.book_id} already exists")
            return

        if book.available_copies < 0:
            print("number of copies cannot be negative") 
            return

        self.books.append(book)
        print(f"book {book.title} added successfully")

    def display_books(self):
        if not self.books:
            print("no books found")
            return
        for book in self.books:
            print(book)

    def search_by_title(self, title_search:str):
        found = [book for book in self.books if title_search in book.title]
        return found

    def search_by_author(self, author_search: str):
        return [book for book in self.books if author_search in book.author]

    def search_by_category(self, category_search: str):
        return [book for book in self.books if category_search in book.category]

    def add_rating(self, rating:Rating):
        if 1 <= rating.score <= 10:
            self.ratings.append(rating)
            print(f" Rating added successfully")
        else:
            print(f"Score must be between 1 and 10")

    def user_reading_history(self, user_id:int):
        user_history = [history for history in self.reading_history if history.user_id == user_id]
        if not user_history:
            print(f"no reading history found for user id: {user_id}")
            return

        for record in user_history:
            book_title = next((book.title for book in self.books if book.book_id == record.book_id), "Unkown book")
            print(f"Book: {book_title}, Statu: {record.status}, Date: {record.date}")

    def recommend_books(self, user_id:int):
        user_rated_books_id = [r.book_id for r in self.ratings if r.user_id == user_id and r.score >= 7]

        favorite_catogories = [book.category for book in self.books if book.book_id == user_rated_books_id]

        user_history_books_id = [h.book_id for h in self.reading_history if h.user_id == user_id]

        recommended_books = [book for book in self.books if book.category in favorite_catogories and book.book_id not in user_history_books_id]

        return recommended_books

    def book_average_rating(self, book_id:int ):
        book_score = [rating.score for rating in self.ratings if rating.book_id == book_id]

        average_score = sum(book_score) / len(book_score)
        return round(average_score, 2)