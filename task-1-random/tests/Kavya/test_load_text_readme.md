# 📄 Text File Loader Test Suite

This repository contains a test for the `load_text_file` function, which reads a file path provided via a `KeyValueArg` wrapper and returns the file content if it's UTF-8 or ASCII encoded. The test uses **property-based testing** via [Hypothesis](https://hypothesis.readthedocs.io/) to verify behavior across a wide range of binary inputs.

---

## ✅ Function Under Test

```python
def load_text_file(item: KeyValueArg) -> str:
    path = item.value
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except OSError as e:
        raise ParseError(f'{item.orig!r}: {e}')
    except UnicodeDecodeError:
        raise ParseError(
            f'{item.orig!r}: cannot embed the content of {item.value!r},'
            ' not a UTF-8 or ASCII-encoded text file'
        )
```

## Class Definitions

```python

class KeyValueArg:
    def __init__(self, orig, value):
        self.orig = orig
        self.value = value

class ParseError(Exception):
    pass

```

## 🧪 Testing Strategy

We use property-based testing to:

1. Automatically generate various binary content (including non-UTF-8 data).

2. Write it to a temporary file.

3. Attempt to load it using load_text_file.

| Decorator      | Purpose                                                        |
|----------------|----------------------------------------------------------------|
| @given(...)    | Generates a wide range of binary content as input.           |
| @settings(...) | Controls verbosity and number of test cases generated per run.

## ✔️ Assertions Made

- If the file contains valid UTF-8 or ASCII, it must decode and return a str.

- If the file contains invalid binary content, a ParseError is expected.

- All files are cleaned up after the test using os.remove().

## 📂 How to Run

1. Install requirements

```bash
pip install pytest hypothesis
```

2. Run the tests

```bash
pytest -s
```

The -s option allows the print output from Hypothesis to appear in the terminal.

## 🔍 Example Output

```css
test_file_loader.py Trying example: test_load_text_file(content=b'\\xff\\xfe')
Generated content: b'\xff\xfe'
