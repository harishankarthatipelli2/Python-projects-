      
                              
print("------------library management system-------------")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.library = []

    def add_book(self):
        book_id = input("Enter book id: ")
        title = input("Enter title: ")
        author = input("Enter author: ")

        book = Book(book_id, title, author)
        self.library.append(book)
        print("Book added successfully")

    def view_book(self):
        for book in self.library:
            status = "Available" if book.available else "Issued"
            print(book.book_id, book.title, book.author, status)

    def issue_book(self):
        book_id = input("Enter book id: ")
        for book in self.library:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued")
                else:
                    print("Already issued")
                return
        print("Book not found")

    def return_book(self):
        book_id = input("Enter book id: ")
        for book in self.library:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned")
                else:
                    print("Already returned")
                return
        print("Book not found")

    def delete_book(self):
        book_id = input("Enter book id: ")
        for book in self.library:
            if book.book_id == book_id:
                self.library.remove(book)
                print("Removed successfully")
                return
        print("Book not found")

    def search_book(self):
        book_id = input("Enter book id: ")
        for book in self.library:
            if book.book_id == book_id:
                print(book.book_id, book.title, book.author)
                return
        print("Book not found")

    def show_stats(self):
        total = len(self.library)
        available = sum(1 for b in self.library if b.available)
        issued = total - available

        print("Total books:", total)
        print("Available:", available)
        print("Issued:", issued)


library = Library()

while True:
    print("\n------Library Management System------")
    print("1. Add book")
    print("2. Search book")
    print("3. View books")
    print("4. Issue book")
    print("5. Return book")
    print("6. Delete book")
    print("7.show statistics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.search_book()
    elif choice == "3":
        library.view_book()
    elif choice == "4":
        library.issue_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        library.delete_book()
    elif choice == "7":
        library.show_stats()
    else :
        break
    
         
        
        
        
    
