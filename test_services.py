"""Unit tests for the library logic. Run with:
    python -m unittest discover -s tests -v
"""

import os
import tempfile
import unittest

from library.services import Library, LibraryError


class LibraryTests(unittest.TestCase):
    def setUp(self):
        # Each test uses its own temporary data file.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.temp_dir.name, "books.json")
        self.library = Library(data_file=self.path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_valid_book(self):
        book = self.library.add_book("Python Basics", "John Doe", "3")
        self.assertEqual(book["id"], 1)
        self.assertEqual(book["copies"], 3)

    def test_ids_increment(self):
        first = self.library.add_book("A", "X", "1")
        second = self.library.add_book("B", "Y", "1")
        self.assertEqual(second["id"], first["id"] + 1)

    def test_add_empty_title_or_author(self):
        with self.assertRaises(LibraryError):
            self.library.add_book("", "John", "2")
        with self.assertRaises(LibraryError):
            self.library.add_book("Title", "  ", "2")

    def test_add_invalid_copies(self):
        for bad in ("abc", "0", "-2", ""):
            with self.assertRaises(LibraryError):
                self.library.add_book("Title", "Author", bad)

    def test_search_is_case_insensitive(self):
        self.library.add_book("Python Basics", "John Doe", "1")
        self.assertEqual(len(self.library.search_books("PYTHON")), 1)
        self.assertEqual(len(self.library.search_books("doe")), 1)
        self.assertEqual(len(self.library.search_books("zzz")), 0)

    def test_search_empty_keyword(self):
        with self.assertRaises(LibraryError):
            self.library.search_books("   ")

    def test_issue_reduces_availability(self):
        book = self.library.add_book("Book", "Author", "2")
        self.library.issue_book(book["id"], "Alice")
        self.assertEqual(self.library.available_copies(book), 1)

    def test_issue_invalid_id(self):
        with self.assertRaises(LibraryError):
            self.library.issue_book("abc", "Alice")
        with self.assertRaises(LibraryError):
            self.library.issue_book(99, "Alice")

    def test_duplicate_issue_blocked(self):
        book = self.library.add_book("Book", "Author", "2")
        self.library.issue_book(book["id"], "Alice")
        with self.assertRaises(LibraryError):
            self.library.issue_book(book["id"], "Alice")

    def test_no_copies_left(self):
        book = self.library.add_book("Book", "Author", "1")
        self.library.issue_book(book["id"], "Alice")
        with self.assertRaises(LibraryError):
            self.library.issue_book(book["id"], "Bob")

    def test_return_book(self):
        book = self.library.add_book("Book", "Author", "1")
        self.library.issue_book(book["id"], "Alice")
        self.library.return_book(book["id"], "Alice")
        self.assertEqual(self.library.available_copies(book), 1)

    def test_return_by_wrong_borrower(self):
        book = self.library.add_book("Book", "Author", "1")
        with self.assertRaises(LibraryError):
            self.library.return_book(book["id"], "Nobody")

    def test_cannot_delete_issued_book(self):
        book = self.library.add_book("Book", "Author", "1")
        self.library.issue_book(book["id"], "Alice")
        with self.assertRaises(LibraryError):
            self.library.delete_book(book["id"])

    def test_delete_book(self):
        book = self.library.add_book("Book", "Author", "1")
        self.library.delete_book(book["id"])
        self.assertEqual(self.library.list_books(), [])

    def test_data_persists_between_runs(self):
        self.library.add_book("Saved Book", "Author", "2")
        reloaded = Library(data_file=self.path)
        self.assertEqual(len(reloaded.list_books()), 1)
        self.assertEqual(reloaded.list_books()[0]["title"], "Saved Book")


if __name__ == "__main__":
    unittest.main()