📄 `README_test_get_unique_filename.md`

## 🧪 Hypothesis Testing for `get_unique_filename()`
This project applies Hypothesis-based property testing to validate the `get_unique_filename()` function, which ensures generated filenames do not conflict with previously used ones.

📜 About the Function
The `get_unique_filename(base: str, ext: str, taken: Set[str]) -> str` function:
- Starts with a base file name and extension.
- Checks if the name is taken.
- If taken, appends a suffix to make it unique (`base-1.ext`, `base-2.ext`, ...).
This is useful for handling file downloads, log rotation, or temporary file creation.

🧪 What the Test Does
The Hypothesis test generates:
- Random base names and extensions.
- Sets of already "taken" filenames.

It checks that:
- The generated name is not in the taken set.
- The name starts with the given base.
- The extension is preserved.

✅ This Ensures That:
- Filename conflicts are correctly avoided.
- Naming conventions are respected.
- Logic is consistent across hundreds of randomized scenarios.

🛠️ How to Run the Test
Install dependencies:pip install hypothesis pytest
