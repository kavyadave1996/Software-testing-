# Test Suite for `parse_content_range` Function

## Function Under Test

**Location:** `httpie/downloads.py`  
**Function:** `parse_content_range(value, bytes_written)`

This function parses the `Content-Range` HTTP header and returns the expected content length or total file size. It is used in the HTTPie download utility to determine how much of a file has been received or is expected.

- If the header is valid and complete, it returns the total size.
- If the header uses a wildcard (`*`), it calculates the length from the byte range.
- If the header is invalid, it raises `ContentRangeError`.

---

## Test Cases

| Test Case | Description |
|-----------|-------------|
| `test_valid_range_with_total` | Tests a valid range: `"bytes 100-199/200"`<br>Expected return: `200`. |
| `test_valid_range_with_unknown_total` | Tests a range with unknown total: `"bytes 100-199/*"`<br>Expected return: `200` (199+1). |
| `test_single_byte_range` | Tests a single-byte range: `"bytes 100-100/*"`<br>Expected return: `101`. |
| `test_invalid_format_missing_bytes_prefix` | Tests a malformed header without `"bytes"` prefix.<br>Expected: `ContentRangeError`. |
| `test_range_mismatch_start_not_equal_to_bytes_written` | Tests a mismatch between provided bytes and range start.<br>Expected: `ContentRangeError`. |
| `test_invalid_range_syntax` | Tests invalid range with non-numeric values.<br>Expected: `ContentRangeError`. |

---

## How to Run the Tests

### Prerequisites:
- Python 3.7+
- [pytest](https://pytest.pypa.io/en/stable/) installed
- The `httpie` module must be available in your Python environment

### Run Command:

bash : pytest tests/test_parse_content_range.py

### To run the complete project: 

bash : coverage run --source=. -m pytest 

### Optional:

To see detailed output, use: coverage report -m    



