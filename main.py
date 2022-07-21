import datetime
import os

class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n", ""),
            "lender_name" :"","issue_date":"", "status":"Avalible"}})
            id+=1

    def display_books(self):
        print("**************** List of Books ****************")
        print("Books Id", "\t ", "Title")
        print("***********************************************")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("status"), "]")


    def borrowing_books(self):
        books_id = input("Enter Book ID: ")
        current_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"] == "Avalible":
                print(f"This book is alredy borwoed to {self.books_dict[books_id]['lender_name']} \t on {self.books_dict[books_id]['issue_date']}")
                return self.borrowing_books()
            elif self.books_dict[books_id]["status"] == "Avalible":
                first_name = input("Enter Your Name: ")
                self.books_dict[books_id]["lender_name"] = first_name
                self.books_dict[books_id]["issue_date"] = current_date
                self.books_dict[books_id]["status"] = "Borrowed"
                print("Book Borrowed Successfully :) ")
        else:
            "Book ID Not Found ! Plz try Again."
            return self.borrowing_books()

    def add_books(self):
        new_book = input("Enter New Book: ")
        if new_book == "":
            return self.add_books()
        elif new_book > 20:
            print("The Name Of The Book Is Too Long. ")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_book,
                'lender_name': '', 'issue_date': '','status': 'Avalible'}})
                print(f"This book{new_book} has been Added Successfully. ")

    def return_books(self):
        book_id = input('Enter Book ID: ')
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["status"] == "Avalible":
                print("This book is available in the library. Plz Try Another ID.")
                return self.return_books()
            elif not self.books_dict[book_id]['status'] == 'Avalible':
                self.books_dict[book_id]['lender_name'] = ''
                self.books_dict[book_id]['issue_date'] = ''
                self.books_dict[book_id]['status'] = 'Avalible'
                print("Updated Successfully :) \n")
            else:
                "Book ID Not Found ! Plz try again."


try:
    myLibrary = Library("list_of_books.txt", "Python's")
    press_key_list = {"D": "Display Books", "I": "Books metaphor", "A": "Add Books", "R": "Return Books", "Q": "Quit"}

    key_press = False
    while not (key_press == "q"):
        print(f"\n************ Welcome To {myLibrary.library_name}'s Library Management System ************\n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press Key : ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Borrowed BOOK\n")
            myLibrary.borrowing_books()

        elif key_press == "a":
            print("\nCurrent Selection : ADD BOOK\n")
            myLibrary.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : DISPLAY BOOKS\n")
            myLibrary.display_books()

        elif key_press == "r":
            print("\nCurrent Selection : RETURN BOOK\n")
            myLibrary.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check. !!!")


l = Library("list_of_books.txt", "java")
print(l.display_books())





