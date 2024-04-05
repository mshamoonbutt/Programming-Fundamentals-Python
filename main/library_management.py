def check_out_book(library, book, patron):
    if book in library:
        print(f"Sorry, '{book}' is already checked out to '{library[book]}'.")
    else:
        library[book] = patron
        print(f"Book '{book}' is checked out to '{patron}'.")

def return_book(library, book):
    if book in library:
        patron = library.pop(book)
        print(f"Book '{book}' has been returned by '{patron}'.")
    else:
        print(f"Book '{book}' is not currently checked out.")

def display_library(library):
    print("\nCurrent Library Status:")
    for book, patron in library.items():
        print(f"Book: '{book}', Checked Out To: '{patron}'")

def main():
    library = {}

    while True:
        print("\nMenu:")
        print("1. Check Out Book")
        print("2. Return Book")
        print("3. Display Library")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            book = input("Enter the book name: ")
            patron = input("Enter the patron's name: ")
            check_out_book(library, book, patron)
        elif choice == '2':
            book = input("Enter the book name to return: ")
            return_book(library, book)
        elif choice == '3':
            display_library(library)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()