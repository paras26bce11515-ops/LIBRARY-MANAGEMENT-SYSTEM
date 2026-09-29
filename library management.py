"""
Library Management System
--------------------------
A simple, beginner-friendly console program written in pure Python.
No external libraries or other programming languages are used.
"""

books = []
next_id = 1


def add_book():
    global next_id
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if title == "" or author == "":
        print("❌ Title and author cannot be empty.\n")
        return
    copies_input = input("Enter number of copies: ").strip()
    if not copies_input.isdigit() or int(copies_input) <= 0:
        print("❌ Number of copies must be a positive whole number.\n")
        return
    book = {"id": next_id, "title": title, "author": author,
            "copies": int(copies_input), "issued_to": []}
    books.append(book)
    print(f"✅ Book '{title}' added successfully with ID {next_id}.\n")
    next_id += 1


def view_books():
    if not books:
        print("📭 No books available in the library.\n")
        return
    print("\n" + "-" * 60)
    print(f"{'ID':<5}{'Title':<20}{'Author':<15}{'Available':<10}")
    print("-" * 60)
    for book in books:
        available = book["copies"] - len(book["issued_to"])
        print(f"{book['id']:<5}{book['title']:<20}{book['author']:<15}{available:<10}")
    print("-" * 60 + "\n")


def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def search_book():
    keyword = input("Enter title or author to search: ").strip().lower()
    if keyword == "":
        print("❌ Search keyword cannot be empty.\n")
        return
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if not results:
        print("🔍 No matching books found.\n")
    else:
        print(f"\n🔍 Found {len(results)} matching book(s):")
        for book in results:
            available = book["copies"] - len(book["issued_to"])
            print(f"  ID {book['id']}: '{book['title']}' by {book['author']} "
                  f"(Available: {available}/{book['copies']})")
        print()


def issue_book():
    try:
        book_id = int(input("Enter Book ID to issue: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric Book ID.\n")
        return
    book = find_book_by_id(book_id)
    if book is None:
        print("❌ No book found with that ID.\n")
        return
    available = book["copies"] - len(book["issued_to"])
    if available <= 0:
        print(f"❌ No copies of '{book['title']}' are currently available.\n")
        return
    borrower = input("Enter the borrower's name: ").strip()
    if borrower == "":
        print("❌ Borrower name cannot be empty.\n")
        return
    if borrower in book["issued_to"]:
        print(f"❌ '{borrower}' has already issued this book.\n")
        return
    book["issued_to"].append(borrower)
    print(f"✅ '{book['title']}' issued to {borrower}.\n")


def return_book():
    try:
        book_id = int(input("Enter Book ID to return: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric Book ID.\n")
        return
    book = find_book_by_id(book_id)
    if book is None:
        print("❌ No book found with that ID.\n")
        return
    borrower = input("Enter the borrower's name: ").strip()
    if borrower not in book["issued_to"]:
        print(f"❌ No record of '{borrower}' having issued this book.\n")
        return
    book["issued_to"].remove(borrower)
    print(f"✅ '{book['title']}' returned by {borrower}.\n")


def delete_book():
    try:
        book_id = int(input("Enter Book ID to delete: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric Book ID.\n")
        return
    book = find_book_by_id(book_id)
    if book is None:
        print("❌ No book found with that ID.\n")
        return
    if book["issued_to"]:
        print(f"❌ Cannot delete '{book['title']}' — some copies are still issued.\n")
        return
    books.remove(book)
    print(f"✅ Book '{book['title']}' deleted successfully.\n")


def print_menu():
    print("=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. Delete a Book")
    print("0. Exit")
    print("=" * 40)


def main():
    menu_actions = {
        "1": add_book, "2": view_books, "3": search_book,
        "4": issue_book, "5": return_book, "6": delete_book,
    }
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("👋 Exiting the Library Management System. Goodbye!")
            break
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("❌ Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()
