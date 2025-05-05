
class ContentRangeError(ValueError):
    pass

import os
from hypothesis import given, strategies as st
import string   

def trim_filename(filename: str, max_len: int) -> str:
    if len(filename) > max_len:
        trim_by = len(filename) - max_len
        name, ext = os.path.splitext(filename)
        if trim_by >= len(name):
            filename = filename[:-trim_by]
        else:
            filename = name[:-trim_by] + ext
    return filename

@given(
    filename=st.text(
        min_size=0,
        max_size=300,
        alphabet=string.ascii_letters + string.digits + "._-"
    ),
    max_len=st.integers(min_value=0, max_value=300)
)

def test_trim_filename(filename, max_len):
    trimmed = trim_filename(filename, max_len)

    # 1. The trimmed filename should not be longer than max_len
    assert len(trimmed) <= max(max_len, len(os.path.splitext(filename)[1]))

    # 2. If the filename was already short enough, it should remain the same
    if len(filename) <= max_len:
        assert trimmed == filename

    # 3. The trimmed filename should still contain only characters from the original
    assert set(trimmed).issubset(set(filename))

    # 4. If the original had an extension, the trimmed filename should still end with that extension (unless fully trimmed)
    name, ext = os.path.splitext(filename)
    if ext and len(name) > 0 and len(filename) > max_len:
        # If possible, the extension should be preserved
        assert trimmed.endswith(ext) or len(trimmed) < len(ext)