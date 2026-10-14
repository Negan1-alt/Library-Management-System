from enum import Enum
class ReadingHistory:
    def __init__(self, user_id:int, book_id: int, date: str, status: str):
        self.user_id = user_id
        self.book_id = book_id
        self.date = date
        self.status = status

class ReadingStatus(Enum):
    BORROWED = "Borrowed"
    COMPLETED = "Completed"
    WANT_TO_READ = 'Want to Read'
    