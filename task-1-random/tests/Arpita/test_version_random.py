from hypothesis import given, strategies as st
from typing import Tuple
from util import split_version  # adjust if it's in a different module

@given(
    st.tuples(
        st.integers(min_value=0, max_value=999),
        st.integers(min_value=0, max_value=999),
        st.integers(min_value=0, max_value=999)
    ).map(lambda t: f"{t[0]}.{t[1]}.{t[2]}")
)
def test_split_version_random(version: str):
    print(f"Generated input: {repr(version)}")
    result = split_version(version)
    assert isinstance(result, Tuple), "The result should be a tuple."
    assert len(result) == 3, "The tuple must have 3 elements."
    for part in result:
        assert isinstance(part, int), "Each part must be an integer."
       

    import argparse
from httpie.cli.definition import response_mime_type  # Adjust import if needed

def test_valid_mime_type_text_csv():
    mime = "text/csv"
    result = response_mime_type(mime)
    assert result == "text/csv"