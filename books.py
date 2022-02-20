class Books:
    def __init__(self, author, book_name, genre, price):
        self.author = author
        self.book_name = book_name
        self.genre = genre
        self.price = price

    def __str__(self):
        return f'{self.author}, {self.book_name}, {self.genre}, {self.price} uah'


book1 = Books('Elizabeth Gilbert', 'City of girls', 'Novel', 349)
book2 = Books('Dan Ariely', 'Predictably Irrational', 'Non-fiction', 475)
