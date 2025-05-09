📄 `README_test_filename_from_url.md`

🧪 Hypothesis Testing for `filename_from_url()`

This project uses property-based testing with Hypothesis to test the `filename_from_url()` function, which derives a suitable filename from a URL and optional content type.

📜 About the Function
The `filename_from_url(url: str, content_type: Optional[str]) -> str` function:
- Extracts the path from the URL.
- Uses the base name as the filename.
- Defaults to `"index"` if the URL ends in a slash.
- Appends a file extension based on `content_type` (e.g. `.txt`, `.html`).

This function is essential for downloading files with meaningful names.

🧪 What the Test Does
The Hypothesis test generates:
- Random URL paths, simulating realistic and edge-case inputs.
- Optional `content_type` headers.

Assertions check that the function:
- Returns a non-empty filename.
- Does not include hidden files (`.` prefix).
- Properly handles missing file extensions.

✅ This Ensures That:
- Downloads generate valid and safe filenames.
- Content-Type headers are respected when inferring extensions.
- Index fallback is used correctly when paths are ambiguous.

🛠️ How to Run the Test
Install:pip install hypothesis pytest
