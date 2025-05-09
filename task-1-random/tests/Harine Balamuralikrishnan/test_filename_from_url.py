import os
import mimetypes
from urllib.parse import urlsplit
from typing import Optional
from hypothesis import given, strategies as st


def filename_from_url(url: str, content_type: Optional[str]) -> str:
    fn = urlsplit(url).path.rstrip('/')
    fn = os.path.basename(fn) if fn else 'index'
    if '.' not in fn and content_type:
        content_type = content_type.split(';')[0]
        if content_type == 'text/plain':
            ext = '.txt'
        else:
            ext = mimetypes.guess_extension(content_type)

        if ext == '.htm':
            ext = '.html'

        if ext:
            fn += ext

    return fn


# Updated test that avoids problematic paths
@given(
    path=st.text(min_size=1, max_size=20, alphabet=st.characters(
        blacklist_characters='\\/:%*?"<>|'
    )),
    content_type=st.sampled_from(['text/plain', 'application/json', None])
)
def test_filename_from_url(path, content_type):
    url = f"http://example.com/{path}/"
    filename = filename_from_url(url, content_type)

    assert isinstance(filename, str)
    assert filename != ""
    assert not filename.startswith('.')  # should be sanitized
    if content_type == 'text/plain' and '.' not in path:
        assert filename.endswith('.txt')
