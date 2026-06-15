class Library:
    def __init__(self):
        self.book = []
        self.nbook = 0
    def addbook(self,book):
        self.book.append(book)
        self.nbook = len(self.book)
    def show(self):
        print(f'the library has {self.nbook} books')

b1 = Library()

b1.addbook('Atomic Habit')        
b1.addbook('Power of money')        
b1.addbook('Theory of bigbang') 
b1.addbook('Atomic Habit')        
b1.addbook('Power of money')        
b1.addbook('Theory of bigbang') 
b1.addbook('Atomic Habit')        
b1.addbook('Power of money')        
b1.addbook('Theory of bigbang') 
b1.show()