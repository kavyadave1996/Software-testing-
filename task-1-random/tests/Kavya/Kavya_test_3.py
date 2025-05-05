

import os
import tempfile
import pytest
from hypothesis import given, strategies as st

class KeyValueArg:
    def __init__(self, orig, value):
        self.orig = orig
        self.value = value

class ParseError(Exception):
    pass

def load_text_file(item: KeyValueArg) -> str:
    path = item.value
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except OSError as e:
        raise ParseError(f'{item.orig!r}: {e}')
    except UnicodeDecodeError:
        raise ParseError(
            f'{item.orig!r}: cannot embed the content of {item.value!r},'
            ' not a UTF-8 or ASCII-encoded text file'
        )

@given(
    content=st.binary(min_size=0, max_size=100)
)
def test_load_text_file(content):
    # Create a temporary file manually
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(content)
        tmp_filename = tmp.name

    try:
        arg = KeyValueArg(orig=tmp_filename, value=tmp_filename)

        try:
            expected_text = content.decode('utf-8')
            # if decoding succeeds
            result = load_text_file(arg)
            assert isinstance(result, str)
            assert result == expected_text
        except UnicodeDecodeError:
            # if decoding fails
            with pytest.raises(ParseError):
                load_text_file(arg)
    finally:
        os.remove(tmp_filename)
