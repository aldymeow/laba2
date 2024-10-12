def book_list(books, func):
    for book in books:
        print(func(book))
        
books = ['Мастер и маргарита','Преступление и наказание','Идиот']

book_list(books, lambda book: book.upper() + ' - прочитано')