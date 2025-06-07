import pytest
from hypothesis import given, settings, assume
from hypothesis.strategies import text
from httpie.utils import get_content_type
import mimetypes

@given(text(min_size=1, max_size=100))
@settings(max_examples=1000, deadline=None)

def test_get_content_type(filename):
    assume(not filename.isspace())  # avoid corner cases like all spaces
    try:
        expected = mimetypes.guess_type(filename, strict=False)[0]
        actual = get_content_type(filename)

        # Should match mimetypes guess exactly
        assert actual == expected, (
            f"Mismatch: expected {expected!r}, got {actual!r} for filename {filename!r}"
        )

        # Should be str or None
        assert actual is None or isinstance(actual, str), (
            f"Output type is not str or None: {type(actual)} for {filename!r}"
        )

    except Exception as e:
        pytest.fail(f"Unexpected exception for input {filename!r}: {e}")
