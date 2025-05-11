import pytest
from hypothesis import given, strategies as st
from httpie.utils import url_as_host

@given(st.text(min_size=1, max_size=200))
def test_url_as_host(url):
    try:
        result = url_as_host(url)

        # Must return a string
        assert isinstance(result, str)

        # The result should not contain credentials (no "@")
        assert "@" not in result, (
            f"Host should not contain '@': got {result!r} from url {url!r}"
        )

        # Force failure for known bad pattern
        if url.strip().startswith("://") or result.strip() == "":
            assert False, f"Possibly invalid or empty host extracted from {url!r}"

    except Exception as e:
        pytest.fail(f"Unexpected crash for url={url!r}: {e}")
