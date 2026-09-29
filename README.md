# LIBRARY-MANAGEMENT-SYSTEM
Library Management System is a software solution that automates operations like tracking book inventory, issuing and returning materials, and managing patron records. It replaces manual paperwork with digital cataloging, real-time tracking, and automated fine calculation, improving library efficiency. 
A simple, beginner-friendly console application for managing a small library, written in pure Python.

## Overview

This project lets a librarian add books, track how many copies are available, search the catalogue, issue books to borrowers, record returns, and delete books, all from a text-based menu in the terminal.

It uses only Python's built-in features (lists, dictionaries, functions, and loops). There are no external libraries and no other languages. All data is stored in memory, so it resets each time the program exits.

## Features

- **Add a book**: store the title, author, and number of copies. Each book gets a unique auto-incremented ID.
- **View all books**: display a formatted table with ID, title, author, and available copies.
- **Search for a book**: case-insensitive search by title or author keyword.
- **Issue a book**: lend a copy to a named borrower, only if copies are available.
- **Return a book**: record the return of a copy from a specific borrower.
- **Delete a book**: remove a book from the catalogue, only if no copies are currently issued.
- **Input validation**: handles empty fields, non-numeric IDs, invalid copy counts, and invalid menu choices without crashing.
- **Duplicate-issue protection**: the same borrower cannot issue the same book twice.

## Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| Python 3.6+ | Core programming language (uses f-strings) |
| Built-in data structures (`list`, `dict`) | In-memory storage of books and borrowers |
| Terminal / Command Prompt | Running and interacting with the program |

No third-party packages are required.

## Project Structure

```
library-management-system/
├── library.py     # Main program (rename to match your file name)
└── README.md
```

## Installation & Running the Project

### 1. Prerequisites

Make sure Python 3.6 or newer is installed:

```bash
python --version
```

If the command is not found, try `python3 --version`. If Python is missing, download it from https://www.python.org/downloads/

### 2. Get the code

Download or clone the project into a folder:

```bash
git clone <your-repository-url>
cd library-management-system
```

Or simply place the `.py` file in a folder of your choice.

### 3. Run the program

```bash
python library.py
```

(Use `python3 library.py` on macOS/Linux if `python` does not work.)

### 4. Use the menu

```
========================================
     LIBRARY MANAGEMENT SYSTEM
========================================
1. Add a Book
2. View All Books
3. Search for a Book
4. Issue a Book
5. Return a Book
6. Delete a Book
0. Exit
========================================
```

Type the number of an option and press **Enter**. Choose `0` to exit.

## Instructions for Testing

The project is tested manually through the console. Run the program and follow the scenarios below, checking that the actual result matches the expected result.

### Test cases

| # | Scenario | Steps | Expected result |
|---|----------|-------|-----------------|
| 1 | Add a valid book | Option 1 → title `Python Basics`, author `John Doe`, copies `3` | Success message with ID 1 |
| 2 | Empty title or author | Option 1 → leave title blank | Error: title and author cannot be empty |
| 3 | Invalid copy count | Option 1 → copies `abc`, `0`, or `-2` | Error: copies must be a positive whole number |
| 4 | View books (empty) | Option 2 before adding any book | "No books available" message |
| 5 | View books | Add a book, then Option 2 | Table shows the book with correct available copies |
| 6 | Search (match) | Option 3 → `python` (any letter case) | Matching book(s) listed with availability |
| 7 | Search (no match) | Option 3 → `zzz` | "No matching books found" |
| 8 | Issue a book | Option 4 → ID `1`, borrower `Alice` | Success; available copies decrease by 1 |
| 9 | Issue with invalid ID | Option 4 → `abc` or `99` | Error for non-numeric or unknown ID |
| 10 | Duplicate issue | Issue book 1 to `Alice` again | Error: already issued to this borrower |
| 11 | No copies left | Issue a 1-copy book to two different borrowers | Second attempt fails: no copies available |
| 12 | Return a book | Option 5 → ID `1`, borrower `Alice` | Success; available copies increase by 1 |
| 13 | Return by wrong borrower | Option 5 → borrower who never issued it | Error: no record of that borrower |
| 14 | Delete while issued | Issue a book, then Option 6 on it | Error: cannot delete, copies still issued |
| 15 | Delete a book | Return all copies, then Option 6 | Book deleted successfully |
| 16 | Invalid menu choice | Enter `9` or `hello` | "Invalid choice" message, menu shown again |
| 17 | Exit | Enter `0` | Goodbye message and program ends |

### Quick end-to-end check

1. Add a book with 2 copies.
2. Issue it to two different borrowers, and confirm availability drops to 0.
3. Try to issue it to a third borrower, which should fail.
4. Return one copy, and confirm availability is 1.
5. Try to delete the book, which should fail.
6. Return the other copy, then delete the book, which should succeed.

## Known Limitations

- Data is not saved to disk; everything is lost when the program closes.
- Borrowers are identified by name only (names are case-sensitive).
- No due dates or fines.

## Possible Future Improvements

- Save and load data using a file (JSON or CSV).
- Track issue and return dates, with overdue fines.
- Add unit tests using Python's built-in `unittest` module.


