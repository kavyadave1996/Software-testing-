## Function Under Test
The function under test is `trim_filename_if_needed` located in the `httpie/downloads.py` module.

### What does `trim_filename_if_needed` do?

This function ensures that a given filename does not exceed a defined maximum length. If the filename is longer than the allowed limit:
- It trims the base name of the file (not the extension),
- Ensures the extension (e.g., `.txt`, `.log`) is preserved,
- Returns a safe, shortened version of the filename that fits within the limit.

It also handles special cases such as:
- Filenames with no extensions,
- Empty strings,
- Filenames with multiple dots (e.g., `data.backup.tar.gz`).

## Test Structure

Two test files were created to validate the function under different scenarios and graph coverage goals:

- `test_trim_filename_if_needed_graph.py`: Contains the **base test cases**, covering primary trim and no-trim logic.
- `test_trim_filename_if_needed_graph1.py`: Contains **extended test cases** targeting edge cases like:
  - Empty filenames,
  - Long extensions,
  - No extension,
  - Boundary-length checks,
  - Multiple dots in filenames.

## How to Run the Tests and Check Coverage

1. **Install the required tools**:
   bash : pip install pytest coverage

2. **Run tests with coverage** (for both files):
bash : coverage erase , bash : coverage run -m pytest tests/ , bash : coverage report -m


3. **Run each file individually** (for comparison):

   **Code 1**: test_trim_filename_if_needed_graph.py

   ```bash
   coverage erase
   coverage run -m pytest tests/test_trim_filename_if_needed_graph.py
   coverage report -m
   ```

   **Code 2**: test_trim_filename_if_needed_graph1.py

   ```bash
   coverage erase
   coverage run -m pytest tests/test_trim_filename_if_needed_graph1.py
   coverage report -m
   ```

## Coverage Summary

| Test File                                | Statement Coverage | Notes                           |
| ---------------------------------------- | ------------------ | ------------------------------- |
| `test_trim_filename_if_needed_graph.py`  | 54%                | Covers basic trim/no-trim paths |
| `test_trim_filename_if_needed_graph1.py` | 57%                | Adds edge case handling         |
