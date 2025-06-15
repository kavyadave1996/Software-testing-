import pytest
from typing import Tuple

# Function to test
def split_version(version: str) -> Tuple[int, ...]:
    parts = []
    for part in version.split('.')[:3]:
        try:
            parts.append(int(part))
        except ValueError:
            break
    return tuple(parts)

# 6 test cases derived from earlier test vectors
test_cases = [
    ("1.2.3", (1, 2, 3)),
    ("4.5.6", (4, 5, 6)),
    ("1.b.3", (1,)),
    ("1.2-3", (1,)),   # "2-3" is invalid int
    ("1.2.a", (1, 2)),
    ("123", (123,)),
]

@pytest.mark.parametrize("version_str, expected", test_cases,
    ids=[f"{v[0]} -> {v[1]}" for v in test_cases]  # friendly test names
)
def test_split_version(version_str, expected):
    result = split_version(version_str)
    assert result == expected, f"For input '{version_str}', expected {expected}, got {result}"
