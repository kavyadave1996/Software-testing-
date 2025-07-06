"""
Test cases for the `parse_content_range` function in httpie/downloads.py
Function under test:
    def parse_content_range(value, bytes_written):
        ...
"""

import pytest
from httpie.downloads import parse_content_range, ContentRangeError


# Test Case 1:
# Valid range with known total (bytes 100–199 out of 200)
# Expected output is 200 (total size)
def test_parse_valid_range_known_total():
    assert parse_content_range('bytes 100-199/200', 100) == 200


# Test Case 2:
# Valid range with unknown total size (*)
# Expected output is 200 based on start and end offset
def test_parse_valid_range_unknown_total():
    assert parse_content_range('bytes 100-199/*', 100) == 200


# Test Case 3:
# Single byte range where start == end
# Expected output is end + 1 → 101
def test_parse_single_byte_range():
    assert parse_content_range('bytes 100-100/*', 100) == 101


# Test Case 4:
# Invalid input: `None` as Content-Range header
# Should raise ContentRangeError
def test_parse_missing_range():
    with pytest.raises(ContentRangeError):
        parse_content_range(None, 100)


# Test Case 5:
# Invalid header unit ("beers" instead of "bytes")
# Should raise ContentRangeError
def test_parse_wrong_unit():
    with pytest.raises(ContentRangeError):
        parse_content_range('beers 100-199/*', 100)


# Test Case 6:
# Invalid byte range where start > end
# Should raise ContentRangeError
def test_parse_invalid_byte_range():
    with pytest.raises(ContentRangeError):
        parse_content_range('bytes 100-99/199', 100)
