import os
from mailbox import Message
from typing import Optional

import pytest
from hypothesis import given, strategies as st


def filename_from_content_disposition(content_disposition: str) -> Optional[str]:
    """
    Extract and sanitize the filename from a Content-Disposition header.
    """
    msg = Message(f'Content-Disposition: {content_disposition}')
    filename = msg.get_filename()
    if filename:
        filename = os.path.basename(filename).lstrip('.').strip()
        if filename:
            return filename
    return None


# Strategy: Ensure the filename is valid and doesn't confuse the parser
valid_filename = (
    st.text(min_size=1, max_size=20)
    .filter(lambda s: s.strip().strip('.') != '')
    .filter(lambda s: not any(c in s for c in ['"', ';', '\n', '\r']))
)

@given(
    name=valid_filename,
    prefix=st.sampled_from(["attachment", "inline"]),
    extra_spaces=st.booleans()
)
def test_filename_from_content_disposition(name, prefix, extra_spaces):
    """
    Test that filename is correctly extracted and sanitized from Content-Disposition headers.
    """
    quoted = f'"{name}"'
    header = f"{prefix}; filename={quoted}"
    if extra_spaces:
        header = f"  {header}  "

    result = filename_from_content_disposition(header)
    expected = os.path.basename(name).lstrip('.').strip()

    assert result == expected
