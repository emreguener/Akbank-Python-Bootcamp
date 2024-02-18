class Library:
    def __init__(self):
        # Open the 'books.txt' file in 'a+' mode for reading and appending
        self.file = open("books.txt", "a+", encoding="UTF-8")

    
    def __del__(self):
        # Close the file when the instance is deleted
        self.file.close()

    def add_book(self):
        # Prompt the user to input book details
        name = input("Book Title: ")
        author = input("Book Author: ")
        year = input("First Release Year: ")
        nOf_pages = input("Number of pages: ")

        # Format the book details and write to the file
        added_book = "{},{},{},{}\n".format(name, author, year, nOf_pages)
        self.file.write(added_book)
        print("Book {} has been successfully added to the library".format(name))
        
    def list_books(self): # Directly appending the latest book at the end
        # Move the file pointer to the beginning of the file
        self.file.seek(0)
        # Read all the lines from the file
        books_content = self.file.readlines()
        if not books_content:
            print("There is no book in the library.")
            return

        print("All the books in the library:")
        for book in books_content:
            book_info = book.strip().split(",")
            # Check if the book information contains at least two elements (title and author)
            if len(book_info) >= 2:
                # If so, print the book name and author
                print("Book Name: {}, Author: {}".format(book_info[0], book_info[1]))
            else:
                # If the book information is incomplete, print an error message
                print("Invalid book information:", book)

                
    def delete_book(self):
        # Prompt the user to input the name of the book to delete
        removed_book_name = input("Name of the book you want to delete: ")
        self.file.seek(0)
        # Read all the lines from the file
        books_content = self.file.readlines()
        total_books = []
        deleted = False
        
        for book in books_content:
            content = book.strip().split(",")
            # If the book name matches, don't include it in total_books list
            if removed_book_name != content[0]:
                total_books.append(book)
            else:
                deleted = True

        # If book is deleted, overwrite the file with updated book list
        if deleted:
            self.file.seek(0)
            # Truncate the file, removing all its contents
            self.file.truncate()
            # Write the updated book list back to the file
            self.file.writelines(total_books)
            print("{} has been deleted from the library".format(removed_book_name))
        else:
            print("{} is not found in the library".format(removed_book_name))
            
    
    def list_books_sorted(self): # Sorting alphabetically by book title
        self.file.seek(0)
        books_content = self.file.readlines()
        if not books_content:
            print("There is no book in the library.")
            return

        # Sort books by title
        books_content.sort(key=lambda x: x.split(',')[0].strip())  

        print("All the books in the library (sorted by title):")
        for book in books_content:
            book_info = book.strip().split(",")
            # Check if the book information contains at least two elements (title and author)
            if len(book_info) >= 2:
                # If so, print the book name and author
                print("Book Name: {}, Author: {}".format(book_info[0], book_info[1]))
            else:
                # If the book information is incomplete, print an error message
                print("Invalid book information:", book)
            
    def search_book_name(self):
        # Prompt the user to input the name of the book to search
        search_query = input("Enter the name of the book you want to search: ")
        self.file.seek(0)
        books_content = self.file.readlines()
        found_books = []

        for book in books_content:
            book_info = book.strip().split(",")
            # If search query matches book name, add it to found_books list
            if search_query.lower() in book_info[0].lower(): 
                found_books.append(book)

        # If any books are found, print them
        if found_books:
            print("Search results for '{}':".format(search_query))
            for book in found_books:
                print(book)
        else:
            print("No books found with the name '{}'".format(search_query))

            
    def search_book_author(self):
        # Prompt the user to input the name of the author to search
        search_query = input("Enter the name of the author you want to search: ")
        self.file.seek(0)
        books = self.file.readlines()
        found_books = []

        for book in books:
            book_info = book.strip().split(",")
            if search_query.lower() in book_info[1].lower():
                found_books.append(book)

        if found_books:
            print("Search results for author '{}':".format(search_query))
            for book in found_books:
                print(book)
        else:
            print("No books found with author '{}'".format(search_query))

import os
def clear_screen():
    # for Windows 
    if os.name == 'nt':
        _ = os.system('cls')
    # for Linux and MacOS 
    else:
        _ = os.system('clear')


def menu():
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Alphabetical Sorting by Book Title")
    print("5) Search by Book Title")
    print("6) Search by Book Author")
    print("7) Exit")


def main():
    # Create an instance of the Library class
    lib = Library()
    while True:
        # Display the menu options
        menu()
        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")
        # Based on the user's choice, call the appropriate method
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.delete_book()
        elif choice == "4":
            lib.list_books_sorted()
        elif choice == "5":
            lib.search_book_name()
        elif choice == "6":
            lib.search_book_author()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        
        # Wait for user input before clearing the screen
        input("Press enter to continue")
        clear_screen()     
        
if __name__ == "__main__":
    main()