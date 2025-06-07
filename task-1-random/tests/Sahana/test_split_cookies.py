import re
import pytest
from hypothesis import given
from hypothesis.strategies import text, characters
from httpie.utils import split_cookies

# Use the same regex HTTPie uses
RE_COOKIE_SPLIT = re.compile(r', (?=[^ ;]+=)')

# Restrict input to characters that commonly appear in cookies
cookie_chars = characters(
    min_codepoint=32,
    max_codepoint=126,
    blacklist_characters=["\n", "\r"]
)

@given(text(alphabet=cookie_chars, min_size=1, max_size=500))
def test_split_cookies(cookie_str):
    try:
        result = split_cookies(cookie_str)

        # Must return a list
        assert isinstance(result, list), f"Returned type: {type(result)}"

        # Each entry should be a string
        for entry in result:
            assert isinstance(entry, str)

        # Check if splitting behavior matches the regex definition
        expected = RE_COOKIE_SPLIT.split(cookie_str)
        assert result == expected, (
            f"Mismatch with RE_COOKIE_SPLIT:\nInput: {cookie_str!r}\n"
            f"Expected: {expected}\nGot: {result}"
        )

    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")

