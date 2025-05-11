# 🧪 Hypothesis Testing for `url_as_host()`

This project uses property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) to verify the correctness of the `url_as_host()` function, which extracts the hostname from a given URL string.

---

## 📜 About the Function

The `url_as_host(url: str)` function:

- Extracts the **host portion** from a full URL string.
- Handles URLs that may contain schemes (e.g., `http://`), user credentials (e.g., `user:pass@`), and ports (e.g., `:8080`).
- Removes unwanted parts such as credentials and protocol prefix, returning only the hostname.

This function is commonly used in HTTP clients and tools where it's important to isolate and process the actual host (e.g., `example.com`) from user-supplied URLs.

---

## 🧪 What the Test Does

The Hypothesis-based test generates:

- Random strings that represent URLs, including malformed or edge-case strings.

For each generated input:

- It checks that the result of `url_as_host(url)` is a string.
- Asserts that the returned hostname does **not** contain credentials (i.e., `@` characters should not be present).
- Fails if the returned host is empty or clearly invalid based on basic structure assumptions.
- Catches any unexpected exceptions that might occur when handling malformed input.

✅ **This Ensures That:**

- The function can reliably extract hostnames from both valid and malformed URLs.
- It handles common edge cases such as missing schemes, double slashes, or embedded credentials.
- It never crashes unexpectedly, even with odd or malformed input.

---

## 🛠️ How to Run the Test

1. Install the required libraries:
   ```bash
   pip install hypothesis pytest
