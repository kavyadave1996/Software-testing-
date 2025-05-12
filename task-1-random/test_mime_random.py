from hypothesis import given, strategies as st
from hypothesis import settings
import pytest
import argparse
from httpie.cli.definition import response_mime_type  # adjust if it's in a different module

@given (major=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_characters='/')),
    minor=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_characters='/')))
@settings(max_examples=100) # Adjust the number of examples as needed
def test_response_mime_type_random(major, minor):
    mime = f"{major}/{minor}"
    print(f"Generated input: {repr(mime)}")
    result= response_mime_type(mime)
    assert isinstance(result, str), "The result should be a string."
    assert mime.count('/') == 1, "The mime type should contain exactly one '/' character."
    
    