# 🧪 Hypothesis Testing for `humanize_bytes()`

This project uses property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) to verify the correctness of the `humanize_bytes()` function, which converts raw byte counts into human-readable strings such as `"1.00 MB"` or `"512 B"`.

---

## 📜 About the Function

The `humanize_bytes(n: int, precision: int)` function:

- Converts a numeric byte count into a formatted string with a size unit (e.g., B, kB, MB, GB, etc.).
- Accepts:
  - `n`: the byte count (must be non-negative),
  - `precision`: the number of decimal digits to include.
- Automatically selects the appropriate unit based on size.
- Returns a human-friendly string like `"123.45 kB"`.

This function is essential for displaying file sizes or memory usage in user-facing tools or CLI output.

---

## 🧪 What the Test Does

The Hypothesis-based test generates:

- Random byte values from `0` to `2^60`.
- Decimal precision values between `0` and `5`.

For each input pair, the test verifies that:

- The output is a string that ends with a valid unit.
- The string contains a numeric part that can be parsed as a float.
- The number of decimal places respects the given `precision`.
- The formatting is consistent (e.g., `"1.0 MB"` for precision 1).
- Edge cases such as `n = 0`, very large numbers, or `precision = 0` are correctly handled.

✅ **This Ensures That:**

- The formatting is consistent and readable.
- Units are applied accurately based on size thresholds.
- The decimal precision is strictly enforced.
- The function handles a wide range of inputs without crashing.

---

## 🛠️ How to Run the Test

1. Install the required libraries:
   ```bash
   pip install hypothesis pytest
