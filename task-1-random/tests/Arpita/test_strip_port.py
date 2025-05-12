
def strip_port(hostname: str) -> str:
    return hostname.split(':')[0]

from hypothesis import given, strategies as st
@given(
    hostname=st.text(min_size=1, max_size=20, alphabet=st.characters(blacklist_characters=":")),
    port=st.integers(min_value=1, max_value=65535)
)
def test_strip_port_valid(hostname, port):
    print(f"Generated input: {repr(hostname)}, {port}")
    full = f"{hostname}:{port}"
    result = strip_port(full)
    assert result == hostname, f"Expected '{hostname}', got '{result}'"

   