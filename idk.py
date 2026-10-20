books = ["Matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library stock:",library)

class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies

    def show_details(self):
        print(self.title, "Available copies: ", self.copies)



class Library:
    def __init__(self, stock):
        self.stock = stock

    def show_available_book(self):
        available_books = [
            book for book in self.stock if self.stock[book] > 0
        ]
        print(" Books Available: ", available_books)

    def borrow_book(self, chosen_book):
        if chosen_book not in self.stock:
            print(chosen_book, "is not in the Library!")
            return False

        if self.stock[chosen_book] == 0:
            print(chosen_book, "is not available!")
            return False

        self.stock [chosen_book]-= 1
        print(chosen_book, "borrowed successfully!")
        print("Remaining copies:", self.stock[chosen_book])
        return True


my_library = Library(library)
my_library.show_available_book()

chosen_book = input("Which book do you want to borrow? ").lower().strip()

late_fees = [5, 6, 4, 8, 7 ]
extra_fee = int(input("Enter the extra fee to add to every book: "))

updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees: ", updated_fees)

if chosen_book in books:
    book_index = books.index(chosen_book)
    chosen_fee = updated_fees[book_index]
    print("Late fee for", chosen_book, ":", chosen_fee)

    borrowed = my_library.borrow_book( chosen_book)

    print("")
    print("LIBRARY SUMMARY")

    if borrowed:
        print("Book Borrowed:", chosen_book)
        print("Late Fee:", chosen_fee)
    else:
        print("No book was borrowed")

    print("Updated Library Stock:", my_library.stock)
    print("-------------------------------------------")

else:
    print("Sorry, this book is not in our book list.")


