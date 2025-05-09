import os
from email.message import Message
from typing import Optional
from hypothesis import given, strategies as st


def filename_from_content_disposition(content_disposition: str) -> Optional[str]:
    msg = Message()
    msg['Content-Disposition'] = content_disposition
    filename = msg.get_filename()
    if filename:
        # Basic sanitation
        filename = os.path.basename(filename).lstrip('.').strip()
        if filename:
            return filename
    return None


@given(
    base=st.text(min_size=1, max_size=10).filter(lambda s: all(c not in s for c in ['"', ';'])),
    ext=st.sampled_from([".txt", ".log", ".tar.gz", ""]),
    disposition_type=st.sampled_from(["attachment", "inline"]),
    quote=st.booleans(),
    pad=st.booleans()
)
def test_filename_from_content_disposition_llm(base, ext, disposition_type, quote, pad):
    """
    Test the function using randomized header formats and filenames.
    """
    raw_name = base + ext
    filename = f'"{raw_name}"' if quote else raw_name
    header = f"{disposition_type}; filename={filename}"
    if pad:
        header = f"  {header}  "

    expected = os.path.basename(raw_name).lstrip('.').strip()
    result = filename_from_content_disposition(header)

    assert result == expected
