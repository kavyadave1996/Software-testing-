# README for Test Suites

## Overview

This directory contains test suites for validating utility functions related to color handling, filename trimming, and text file loading. The tests utilize **Hypothesis** for property-based testing and **pytest** for assertions and exception handling.

---

## Files

### 1. `test_get_color.py`

- **Purpose:**  
  Tests the `get_color()` function, which retrieves hex color codes or ANSI color names from a palette based on a color and shade input.

- **Highlights:**  
  - Uses Hypothesis to generate random strings for colors and shades.  
  - Validates correct retrieval of color codes from nested dictionaries and direct strings.  
  - Returns `None` if the color or shade is missing in the palette.  
  - Updated `get_color()` to return `None` if a shade is missing inside a color dictionary, fixing previous assertion errors.

---

### 2. `test_trim_filename.py`

- **Purpose:**  
  Tests the `trim_filename()` function that shortens filenames to a specified maximum length while preserving file extensions when possible.

- **Highlights:**  
  - Generates filenames with letters, digits, dots, underscores, and hyphens of variable length.  
  - Ensures trimmed filenames do not exceed the maximum length or lose the file extension unless necessary.  
  - Checks the trimmed filename characters are a subset of the original filename characters.

---

### 3. `test_load_text.py`

- **Purpose:**  
  Tests the `load_text_file()` function, which reads file content and ensures it is UTF-8 or ASCII decodable.

- **Highlights:**  
  - Creates temporary files with random binary content to test loading.  
  - Asserts successful decoding or raises a custom `ParseError` on decoding or file access failures.

---

## Setup Instructions

1. Install required dependencies:

```bash
pip install pytest hypothesis
```

2. Ensure the modules containing the tested functions (get_color, trim_filename, load_text_file) are accessible in your Python environment.

## Running Tests

Run all tests with:

```bash
pytest -v
```

Run tests for a single file, for example:

```bash
pytest -v test_get_color.py
```

## Notes

- Tests use Hypothesis settings for verbose output and controlled example count for easier debugging.

- The tests cover typical cases, edge cases, and error conditions to maximize code coverage and robustness.