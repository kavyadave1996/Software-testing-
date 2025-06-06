# 🧪 Hypothesis Testing for `get_content_type()`

This project uses property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) to verify the correctness of the `get_content_type()` function, which determines the MIME type of a file based on its name or extension.

---

## 📜 About the Function

The `get_content_type(filename: str)` function:

- Uses the file extension of the given `filename` to guess its MIME type.
- Internally relies on Python’s `mimetypes.guess_type(filename)[0]`.
- Returns a MIME type string (e.g., `"text/plain"`, `"application/json"`), or `None` if the MIME type cannot be determined.

This function is essential for correctly identifying file types, especially when handling file uploads or downloads based on filenames.

---

## 🧪 What the Test Does

The Hypothesis-based test generates:

- Random filename strings up to 100 characters in length.

For each generated filename:

- It uses Python’s standard library (`mimetypes.guess_type()`) to compute the expected MIME type.
- It then compares that to the result of `get_content_type()`, ensuring exact match.
- It asserts that the return type is either a string or `None`.
- It avoids corner cases like strings made only of whitespace using `assume()`.

✅ **This Ensures That:**

- The function behaves exactly like the standard `mimetypes.guess_type()` function.
- No incorrect MIME types are returned.
- The function gracefully handles odd, malformed, or unknown filenames without crashing.

---

## 🛠️ How to Run the Test

1. Install the required libraries:
   ```bash
   pip install hypothesis pytest
