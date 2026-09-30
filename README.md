# LIBRARY-MANAGEMENT-SYSTEM
Library Management System refers to the software that manages the library and supports such operations like inventory management, book issue and return, and storing and maintaining records of library patrons. It makes paperless processes possible, improves tracking, and automates such operations as fine calculation.

A small-scale library management command-line application for a librarian to manage the books catalog, keep track of available books, issue books to borrowers, and accept returns from them.
## Summary

This project is a library management utility that allows adding books, viewing their records, searching, issuing, and returning books in a command-line interface. It uses only Python built-in libraries and functions.

This utility has several features:

- Adding books with titles, authors, and number of copies;

- Viewing all books in a catalog;
- Searching for books by title or author;
- Issuing a book to a borrower;
- Returning books;
- Removing books when they are not issued;
- Input validation;

- Preventing the same book issuing to the same person twice.

The application is built using only Python 3.6+ built-in libraries.
The following table describes the tools used in the project:
Tool Purpose
Python 3.6+ The main programming language (some features require Python 3.6+)
Built-in data structures Storage of books and borrowers information
Terminal\Command prompt Executing the program
The directory structure looks like this:
library-management-system/
├── library.py # the program file (change library.py to your preferable name)
└── README.md
## How to install and use the project
### Prerequisites
Ensure that Python is installed on your computer:
Terminal
python --version
If you get an error that python is not found, try python3 --version . If Python is not installed, you can download it from https://www.python.org/downloads/
### Getting the code
You can download or clone the repository to your local machine:
Terminal
git clone
cd library-management-system
Or put the .py file you have downloaded somewhere in your filesystem.
### Running the program
Terminal
python library.py
On macOS/Linux, you might need to use python3 library.py instead
The program will print the following menu to the terminal:
Console
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
To make a choice, enter the corresponding number and press Enter. To exit, enter 0 .
The following step-by-step instructions describe how to test the application by performing operations described in the project description and ensuring that the actual results match the expected ones.
### Testing instructions
This project uses manual testing. You need to run the program in a terminal/command prompt window and perform the following steps:
1. Add a Book: Make sure that the record is added successfully with the specified book title, author, and number of copies with a generated ID.
2. Empty title or author: Ensure that adding a book with empty title or author fails with an appropriate error message.
3. Copy count validation: Try to add a book with 0, negative number, or non-integer copies to ensure that it is not allowed, and an error is raised.
4. View All Books: Ensure that when there are no books in the catalog, a message about the emptiness of the catalog is shown.
5. View All Books: Add a book and then view all books to ensure that it is added and displayed correctly with the specified details.
6. Search: Search for a book using a book title or author name to ensure that it is found with a case-insensitive match.
7. Search: Ensure that when searching for a book that is not in the catalog, a message about the absence of the book is displayed.
8. Issue: Issue a book to make sure that it is issued to the specified borrower, and the number of available copies is updated.
9. Issue: Try to issue a book with invalid ID (non-integer or not existing) to ensure that it is not issued, and an error is raised.
10. Issue: Issue the same book to the same borrower again to ensure that it is not issued, and an error is raised.
11. Issue: Issue a book with only one copy to two different borrowers to ensure that the second issue is denied, since there are no more available copies.
12. Return: Return a book to ensure that it is marked as returned, and the number of available copies is updated.
13. Return: Try to return a book that was not issued to a particular borrower to ensure that it is not allowed, and an error is raised.
14. Delete: Issue a book and then try to delete it to ensure that it cannot be deleted while it is issued.
15. Delete: Return issued books (if any), then delete a book to ensure that it is deleted successfully.
16. Invalid Choice: Enter different invalid numbers to ensure that the program shows an error message about an invalid choice.
17. Exit: Ensure that when you enter 0 , the program displays a goodbye message and exits.
The following is a brief list of the test steps you can do to check the program's functionality:
1. Add a book with two copies
2. Issue this book to two different borrowers and check that the available copies are now zero
3. Try to issue this book to a third borrower and make sure that it is not allowed
4. Return one copy of this book and check that the available copies are now one
5. Try to delete this book and make sure that it is not allowed
6. Return the second copy of this book and then try to delete it again to make sure that it is now deleted
### Known limitations
- Data is not stored on disk; it is kept only in memory and is lost when the program terminates.
- Libraries are not tracked; a borrower is identified by their name (case-sensitive).
- Fine calculation and due date tracking are not implemented.
### Future improvements
- Add support for saving/loading data to/from a file/disk.
- Add a feature for fine calculation and tracking of issued/returned dates.
- Add unit tests using Python's built-in assert statements or the unittest module.

- ## AUTHOR
- NAME :- PARAS VATS
- REGISTRATION NUMBER :- 26BCE11515
