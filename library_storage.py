"""Reading and writing library data to a JSON file."""

import json
import os

from library import config


def _empty_data():
    return {"next_id": 1, "books": []}


def load_data(path=None):
    """Return saved data, or empty data if the file is missing or corrupt."""
    path = path or config.DATA_FILE
    if not os.path.exists(path):
        return _empty_data()
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if "books" not in data or "next_id" not in data:
            raise ValueError("Missing keys")
        return data
    except (ValueError, OSError):
        # Keep the damaged file as a backup instead of overwriting it.
        try:
            os.replace(path, path + ".bak")
        except OSError:
            pass
        return _empty_data()


def save_data(data, path=None):
    """Save data safely (write to a temp file, then replace the original)."""
    path = path or config.DATA_FILE
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    os.replace(temp_path, path)