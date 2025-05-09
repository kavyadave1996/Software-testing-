from hypothesis import given, strategies as st
import os

def trim_filename_if_needed(filename: str, directory='.', extra=0) -> str:
    max_len = 255 - extra  # fixed max length
    if len(filename) > max_len:
        name, ext = os.path.splitext(filename)
        trim_by = len(filename) - max_len
        if trim_by >= len(name):
            filename = filename[:-trim_by]
        else:
            filename = name[:-trim_by] + ext
    return filename

def get_unique_filename(filename: str, exists=os.path.exists) -> str:
    attempt = 0
    while True:
        suffix = f'-{attempt}' if attempt > 0 else ''
        try_filename = trim_filename_if_needed(filename, extra=len(suffix))
        try_filename += suffix
        if not exists(try_filename):
            return try_filename
        attempt += 1

def make_mock_exists(taken_names):
    def exists_mock(name):
        return name in taken_names
    return exists_mock

@given(
    base=st.text(min_size=1, max_size=20),
    ext=st.sampled_from([".txt", ".log", ".csv"]),
    taken_count=st.integers(min_value=0, max_value=5)
)
def test_get_unique_filename(base, ext, taken_count):
    """
    Tests get_unique_filename() by simulating existing filenames
    and ensuring a new unique name is generated correctly.
    """
    filename = base + ext
    taken = set()

    for i in range(taken_count):
        suffix = f"-{i}" if i > 0 else ""
        taken.add(filename + suffix)

    mock_exists = make_mock_exists(taken)
    unique = get_unique_filename(filename, exists=mock_exists)

    assert unique not in taken
    assert unique.startswith(base)
    assert ext in unique
