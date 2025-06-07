# 🧪 Hypothesis Testing for `split_cookies()`

This project uses property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) to verify the correctness of the `split_cookies()` function, which parses and safely splits `Set-Cookie` header strings in HTTP responses.

---

## 📜 About the Function

The `split_cookies(cookies: str)` function:

- Accepts a raw string containing multiple cookie entries, typically joined by commas.
- Uses a regular expression to **safely split** the cookie string only at valid boundaries.
- Avoids incorrect splitting when commas appear inside quoted cookie values or complex formats.
- Returns a list of individual cookie strings.

This function is essential for HTTP client libraries that need to handle `Set-Cookie` headers containing multiple cookies while avoiding parsing errors or unsafe splits.

---

## 🧪 What the Test Does

The Hypothesis-based test generates:

- Random strings using printable characters commonly found in cookie headers (letters, symbols, whitespace, `=`, `;`, `,`, etc.).

For each generated input:

- It verifies that `split_cookies()` returns a list.
- Ensures that each item in the list is a string.
- Compares the output of `split_cookies()` against the output of the exact regular expression that defines HTTPie’s cookie-splitting logic.
- Fails if the function’s output does not match the expected result from the regex.

✅ **This Ensures That:**

- The function correctly splits cookie headers according to its own logic.
- Complex or malformed cookie inputs do not crash or produce inconsistent results.
- Edge cases (e.g., multiple commas, spaces, quoted values) are handled safely and consistently.

---

## 🛠️ How to Run the Test

1. Install the required libraries:
   ```bash
   pip install hypothesis pytest
