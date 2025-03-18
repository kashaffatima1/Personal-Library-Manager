import json #to save data in json format
import os #file handling

DATA_FILE = "library.txt"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file)

library = []      

#Dispay menu library
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
   
#add book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower()
    library.append(
        {"title": title, 
         "author": author, 
         "year": year, 
         "genre": genre, 
         "read": read})
    print("Book added successfully!")
    save_data(library)

def remove_book(library):
    delete_book = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == delete_book.lower():
            library.remove(book)
            print(f"Book {delete_book} removed successfully!")
            save_data(library)
            break
    else:
            print(f"{delete_book} book not found in the library!")

def search_book(library):
    search_query = input("Search by title or author? ").strip().lower()
    found_books = [
        book for book in library
        if search_query in book["title"].lower() or search_query in book["author"].lower()
    ]
    if found_books:
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {book['read']}")
    else:
         print(f"No matching book found in the library!")

def display_all_book(library):
    if library:
      for book in library:
          status = "Read" if book["read"].lower() == "yes" else "Unread"
          print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print("No books in the library!")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"].lower() == "yes")
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage Read: {percentage_read:.1f}%")

library = load_data()
while True:
    display_menu()
    choice = input("Enter your choice(1-6): ").strip()
    if choice == "1":
        add_book(library)
    elif choice == "2":
        remove_book(library)
    elif choice == "3":
        search_book(library)
    elif choice == "4":
        display_all_book(library)
    elif choice == "5":
        display_statistics(library)
    elif choice == "6":
        print("Good Bye!")
        save_data(library)
        break
    else:
        print("Invalid choice. Please choose a valid option.")









