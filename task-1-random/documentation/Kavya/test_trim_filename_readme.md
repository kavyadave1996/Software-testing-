# Filename Trimmer Tests

This repository includes a test suite for the `trim_filename` function, which safely trims a filename to a specified maximum length while preserving its extension if possible.

---

## 🧪 Function Under Test

```python

def trim_filename(filename: str, max_len: int) -> str:
    if len(filename) > max_len:
        trim_by = len(filename) - max_len
        name, ext = os.path.splitext(filename)
        if trim_by >= len(name):
            filename = filename[:-trim_by]
        else:
            filename = name[:-trim_by] + ext
    return filename
```

## ✅ What the Function Does

- Trims a filename to fit within a given max_len limit.

- Attempts to preserve the file extension (.txt, .png, etc.) when trimming.

- If the extension cannot be preserved (due to space), the filename is shortened as much as possible.

## 🧪Test Strategy

The test is written using Hypothesis for property-based testing and pytest for test discovery and execution.

### Hypothesis Decorators Used

| Decorator      | Purpose                                                        |
|----------------|----------------------------------------------------------------|
| @given(...)    | Auto-generates a wide variety of valid test inputs.            |
| @settings(...) | Controls how many examples to test and how verbose the output is. |

## 🧾 Test Assertions

The test verifies the following conditions for each generated input:

1. Length Check:
The trimmed filename must not exceed the max_len (unless the extension alone is longer).

2. No Unnecessary Trim:
If the original filename is within the max_len, it should not change.

3. Character Integrity:
The trimmed filename must only contain characters from the original input.

4. Extension Preservation:
If possible, the file extension must be preserved after trimming.

## 📦 How to Run

Step 1: Install dependencies

```bash
pip install pytest hypothesis
```

Step 2: Run the test

```bash
pytest -s test_2.py
```

The -s flag allows print() statements to show in the console for debug output.

## 🔍 Example Test Output

With verbosity=Verbosity.verbose, Hypothesis will show input data:

```text
test_2.py Trying example: test_trim_filename(filename='abc.txt', max_len=5)
Generated inputs -> filename: abc.txt, max_len: 5
