🧪 Hypothesis Testing for `filename_from_content_disposition()`
This project uses property-based testing with Hypothesis to verify the correctness of the `filename_from_content_disposition()` function, which extracts file names from `Content-Disposition` headers in HTTP responses.

📜 About the Function

The `filename_from_content_disposition(header: str)` function:
- Parses the `Content-Disposition` header.
- Extracts the filename if present.
- Sanitizes the filename by:
  - Stripping leading dots (to avoid hidden files),
  - Removing whitespace,
  - Using only the base file name.

This function is crucial for determining safe and usable file names when downloading files from a URL.

🧪 What the Test Does
The Hypothesis test generates:
- Valid file name strings (excluding `"` and `;` characters).
- Header prefixes like `"attachment"` or `"inline"`.
- Optional spaces around header syntax to mimic real-world variations.

The test constructs realistic headers and checks whether the function:
- Correctly extracts the intended filename.
- Applies the expected sanitation rules.

✅ This Ensures That:
- The function works with a wide variety of valid filenames.
- Edge cases like extra whitespace or quoted names are handled.
- Invalid or malformed headers don't cause crashes.

🛠️ How to Run the Test
Install requirements:pip install hypothesis pytest
