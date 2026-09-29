"""Console menu and user interaction."""

from library import config
from library.services import LibraryError


def print_menu():
    line = "=" * config.MENU_WIDTH
    print(line)
    print(f"     {config.APP_TITLE}")
    print(line)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. Delete a Book")
    print("0. Exit")
    print(line)


def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    copies = input("Enter number of copies: ").strip()
    try:
        book = library.add_book(title, author, copies)
    except LibraryError as error:
        print(f"❌ {error}\n")
        return
    print(f"✅ Book '{book['title']}' added successfully with ID {book['id']}.\n")


def view_books(library):
    books = library.list_books()
    if not books:
        print("📭 No books available in the library.\n")
        return
    line = "-" * config.TABLE_WIDTH
    print("\n" + line)
    print(f"{'ID':<5}{'Title':<20}{'Author':<15}{'Available':<10}")
    print(line)
    for book in books:
        available = library.available_copies(book)
        print(f"{book['id']:<5}{book['title']:<20}{book['author']:<15}{available:<10}")
    print(line + "\n")


def search_book(library):
    keyword = input("Enter title or author to search: ").strip()
    try:
        results = library.search_books(keyword)
    except LibraryError as error:
        print(f"❌ {error}\n")
        return
    if not results:
        print("🔍 No matching books found.\n")
        return
    print(f"\n🔍 Found {len(results)} matching book(s):")
    for book in results:
        available = library.available_copies(book)
        print(f"  ID {book['id']}: '{book['title']}' by {book['author']} "
              f"(Available: {available}/{book['copies']})")
    print()


def issue_book(library):
    book_id = input("Enter Book ID to issue: ").strip()
    borrower = input("Enter the borrower's name: ").strip()
    try:
        book = library.issue_book(book_id, borrower)
    except LibraryError as error:
        print(f"❌ {error}\n")
        return
    print(f"✅ '{book['title']}' issued to {borrower}.\n")


def return_book(library):
    book_id = input("Enter Book ID to return: ").strip()
    borrower = input("Enter the borrower's name: ").strip()
    try:
        book = library.return_book(book_id, borrower)
    except LibraryError as error:
        print(f"❌ {error}\n")
        return
    print(f"✅ '{book['title']}' returned by {borrower}.\n")


def delete_book(library):
    book_id = input("Enter Book ID to delete: ").strip()
    try:
        book = library.delete_book(book_id)
    except LibraryError as error:
        print(f"❌ {error}\n")
        return
    print(f"✅ Book '{book['title']}' deleted successfully.\n")


def run(library):
    """Main menu loop."""
    actions = {
        "1": add_book,
        "2": view_books,
        "3": search_book,
        "4": issue_book,
        "5": return_book,
        "6": delete_book,
    }
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("👋 Exiting the Library Management System. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(library)
        else:
            print("❌ Invalid choice. Please select a valid option.\n")