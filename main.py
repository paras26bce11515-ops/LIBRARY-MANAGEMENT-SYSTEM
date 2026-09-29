"""
Library Management System
-------------------------
Entry point. Run with:  python main.py
"""

from library.services import Library
from library import ui


def main():
    library = Library()
    ui.run(library)


if __name__ == "__main__":
    main()