# Student Management System (NO AI WAS USED)

A command-line application for managing student records, built in Python. Students and their marks are stored in a local JSON file, with full support for adding, searching, updating, and deleting records, plus automatic grade calculation and report generation.

## Features

- **Add a student** — store name and roll number
- **View all students** — list every student currently in the system
- **Search for a student** — look up a student by name and view their details and marks
- **Update student information** — edit a student's name or roll number
- **Delete a student** — remove a student record, with confirmation required
- **Add marks** — record marks for Python, Math, or English
- **Generate report** — calculate per-subject grades and an overall grade, even for students with incomplete or missing marks

## Project Structure

```
.
├── student_app.py        # Core Student class: data logic, file I/O, grading
├── studentmanager.py      # StudentManager class: menu loop and user interaction
└── students.json          # Local data store (auto-created on first run)
```

## How to Run

```bash
python studentmanager.py
```

You'll be shown a menu:

```
----------MAIN--MENU---------
1.Add new student
2.search for the student
3.update the student information
4.view all students
5.Delete Student
6.add marks
7.generate report
```

Select an option by entering its number.

## Data Format

Each student is stored in `students.json` as:

```json
{
  "Prakash": {
    "roll_no": "190",
    "marks": {
      "python": 100.0,
      "math": 78.0,
      "english": 82.0
    }
  }
}
```

A student can exist with an empty `marks` dictionary if no marks have been recorded yet — the report generator handles this gracefully and shows `N/A` instead of crashing.

## Grading Scale

| Score Range (per subject, out of 100) | Grade |
|---|---|
| 80–100 | A |
| 70–79  | B |
| 60–69  | C |
| 50–59  | D |
| Below 50 | Fail |

The overall total (out of 300) uses the same percentage bands scaled up:

| Total Range (out of 300) | Grade |
|---|---|
| 240–300 | A |
| 210–239 | B |
| 180–209 | C |
| 150–179 | D |
| Below 150 | Fail |

## Design Notes

- **File path** is resolved relative to the script's own location (`Path(__file__).parent`), so the project runs correctly regardless of which machine or folder it's placed in.
- **Grading logic is centralized** in `_grade_marks()` and `_grade_total()` helper methods, avoiding repeated if/elif chains across subjects.
- **Missing data is handled defensively** — `.get()` and `isinstance()` checks ensure that a student with incomplete marks produces a clean `N/A` report instead of a crash.
- **Exception handling is targeted** — `try/except` blocks are placed only around the exact lines that can raise an exception (e.g. converting input to `int`/`float`), not wrapped indiscriminately around entire methods.

## Known Limitations / Possible Improvements

- [ ] Input/output is not yet fully separated from business logic in all methods (e.g. `search_student`, `delete_student`, `update_information` still mix `input()`/`print()` with logic in the same function)
- [ ] No automated tests yet (a good next step using `pytest`)
- [ ] Roll numbers are stored as plain strings/ints without validating uniqueness
- [ ] No support for editing or removing individual subject marks once entered

## What This Project Was Used to Practice

This project was built and then refactored as a learning exercise covering:

- Removing repeated code via helper functions (DRY principle)
- Defensive programming against missing or malformed data (`KeyError`, `TypeError` avoidance)
- Correct, targeted exception handling (`try`/`except`/`else`)
- Portable file path handling with `pathlib`
- (In progress) Separating input/output from core logic for testability and reuse