# Library Book Management System (NO AI)

A command-line application for managing a library's book inventory, built in Python. Books, copy counts, and borrower records are stored in a local JSON file, with full support for adding, searching, updating, deleting, borrowing, and returning books, plus a summary report across the whole library.

## Features

- **Add a new book** — store title, author, book ID, and total copies; optionally mark it as already borrowed at creation time
- **View all books** — list every book currently in the library
- **Search for a book** — look up a book by ID or by title
- **Update book information** — edit a book's title, author, or total copies (with safeguards against invalid changes)
- **Delete a book** — remove a book record, with confirmation required; blocked if any copies are currently borrowed
- **Borrow a book** — check out a copy to a named borrower, if one is available
- **Return a book** — check a copy back in for a named borrower
- **Generate a report** — show per-book details and library-wide totals (copies, availability, borrowers)

## Project Structure

```
.
├── library.py             # Core Library class: data logic, file I/O, validation
├── librarymanager.py       # LibraryManager class: menu loop and user interaction
└── library.json            # Local data store (auto-created on first run)
```

## How to Run

```bash
python librarymanager.py
```

You'll be shown a menu:

```
1>Add New Book
2>View all books
3>Search Book
4>update book info
5>Delete a book
6>borrow a book
7>return a book
8>Generate a report
9>exit
```

Select an option by entering its number.

## Data Format

Each book is stored in `library.json` as:

```json
{
  "9780134853987": {
    "title": "Effective Python",
    "author": "Brett Slatkin",
    "total_copies": 3,
    "available_copies": 2,
    "borrowed_by": ["Prakash"]
  }
}
```

`available_copies` and `borrowed_by` are always kept consistent with each other — a book is never saved with mismatched numbers (e.g. full availability while still showing an active borrower).

## Design Notes

- **File path** is resolved relative to the script's own location (`Path(__file__).parent`), so the project runs correctly regardless of which machine or folder it's placed in.
- **Input validation is centralized** in a single `_validate_input()` helper, reused across every method that needs a non-empty text field, rather than repeating the same check everywhere.
- **Numeric input is validated with targeted exception handling** — `try`/`except`/`else` blocks wrap only the exact line doing the conversion (e.g. `int(input(...))`), not entire methods.
- **Borrow/return logic protects against invalid states:**
  - A book can't be borrowed if `available_copies` is 0.
  - A return only succeeds if the borrower's name is actually on record for that book.
  - `total_copies` can't be reduced below the number of copies currently borrowed.
  - A book can't be deleted while any copies are still borrowed.
- **Search and update logic is separated into helper methods** (`_search_by_book_id`, `_search_by_title`, `_perform_update`), keeping the menu-facing methods focused on input/output while the helpers handle the underlying logic.
- **Report generation avoids repeated calculation logic** by reusing a single `_calculate_borrow()` helper for every book, rather than recomputing borrowed counts inline in multiple places.

## Known Limitations / Possible Improvements

- [ ] Input/output is not yet fully separated from business logic in every method (some methods still mix `input()`/`print()` with logic in the same function)
- [ ] No automated tests yet (a good next step using `pytest`)
- [ ] Book IDs are not validated for format (e.g. ISBN structure) — any non-empty string is accepted
- [ ] Invalid menu selections in some submenus (e.g. search type, update field) fail silently rather than showing an explicit error message

## What This Project Was Used to Practice

This project was built as a follow-up to an earlier Student Management System, specifically to test whether the following habits had become consistent rather than one-off fixes:

- Designing internally consistent data relationships from the start (e.g. `available_copies` always derived from `total_copies` and active borrowers, never entered independently)
- Defensive validation loops for input that must match a specific set of values (e.g. y/n prompts), not just non-empty checks
- Business-rule safeguards applied proactively (blocking deletes/updates that would corrupt data) rather than only after a crash is found
- Targeted, correct exception handling — catching only what can actually be raised, where it's actually raised