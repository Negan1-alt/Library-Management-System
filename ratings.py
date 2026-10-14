class Rating:
    def __init__ (self, user_id:int, book_id:int, score:int, review: str = ""):
        self.user_id = user_id
        self.book_id = book_id
        self._score = score
        self.review = review

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value:int):
        if not (1 <= value <=10):
            raise ValueError("rating must be between 1 and 10")
        self._score = value