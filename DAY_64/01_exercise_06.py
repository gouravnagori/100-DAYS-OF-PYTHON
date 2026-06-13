# Write a Library class with no_of_books and books as two instance variables. Write a program to create
# a library from this Library class and show how you can print all books, add a book and get the number
# of books using different methods. Show that your program doesnt persist the books after the program
# is stopped!

# Goal is to make library management system
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