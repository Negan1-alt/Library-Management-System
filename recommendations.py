class Recommendation:
    def __init__ (self, user_id:int, book_id:int, reason:str, score):
        self.user_id = user_id
        self.book_id = book_id
        self.reason = reason
        self.score = score
    def __str__(self) :
        return (f"Recommendation: (User: {self.user_id}, Book: {self.book_id}, Reason:{self.reason}, Score: {self.score})")

recommend = Recommendation(12,12,"nothing", 12.15)
print(recommend)


