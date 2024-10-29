class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_book(self):
        print("Available books:\n")
        for book in self.available_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print(f"You have now borrowed '{requested_book}'. Enjoy your reading!")
            self.available_books.remove(requested_book)
        else:
            print(f"Sorry, '{requested_book}' is not available. Try a different book.")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print(f"You have now returned '{returned_book}'. Thank you!")


class Customer:
    def request_book(self):
        self.book = input("\nEnter the book you would like to borrow: ").strip().lower()
        return self.book

    def return_book(self):
        self.book = input("\nEnter the book you would like to return: ").strip().lower()
        return self.book


library = Library(["Atomic Habits", "Rich Dad Poor Dad", "Think and Grow Rich"])
customer = Customer()

while True:
    print("\nEnter 1 to show available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit the program")

    user_choice = input("\nEnter your choice: ")
    if user_choice == "1":
        library.display_book()
    elif user_choice == "2":
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == "3":
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice == "4":
        print("Thank you for visiting the library. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
