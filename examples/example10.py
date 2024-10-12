def book_list(books, func):
    for book in books:
        print(func(book))
        
books = ['Мастер и маргарита','Преступление и наказание','Идиот']

def book_print(book):
    return book.upper() + ' - прочитано'

book_list(books, book_print)