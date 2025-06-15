
import os
from hypothesis import given, strategies as st, settings
from httpie.sessions import session_hostname_to_dirname  # adjust if needed

SESSIONS_DIR_NAME = "sessions"

# ISP Test Cases: 6 × 4 = 24 combinations

@settings(max_examples=6)
@given(
    hostname=st.sampled_from([
        "example.com",                       # H1 + L2
        "example.com:443",                   # H2 + L2
        "192.168.0.1",                       # H3 + L1
        "short.io",                          # H1 + L1
        "midrange.com",                      # H1 + L2
        "verylongsubdomain.example",         # H1 + L3
    ]),
    session_name=st.sampled_from([
        "mysession1",                        # S1 + N2
        "dev@2024!",                         # S2 + N2
        "",                                  # S3 + N1
        "averyverylongsessionname1",         # S1 + N3
    ])
)
def test_session_hostname_to_dirname(hostname, session_name):
    """ISP: Combined test of hostname and session_name partitions"""

    print(f"\nTesting with: hostname='{hostname}', session_name='{session_name}'")

    result = session_hostname_to_dirname(hostname, session_name)

    # Replace colons in hostname
    expected_host = hostname.replace(":", "_")
    expected_path = os.path.join(SESSIONS_DIR_NAME, expected_host, f"{session_name}.json")

    # === Assertions ===
    assert result == expected_path
    assert result.startswith(SESSIONS_DIR_NAME)
    assert result.endswith(".json")
    assert ":" not in result.split(os.sep)[-2]  # Confirm port was replaced
