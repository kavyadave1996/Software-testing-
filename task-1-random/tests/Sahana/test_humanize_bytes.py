import pytest
from hypothesis import given, assume
from hypothesis.strategies import integers
from httpie.utils import humanize_bytes

VALID_UNITS = ["B", "kB", "MB", "GB", "TB", "PB"]

@given(
    integers(min_value=0, max_value=2**60),  # valid byte sizes
    integers(min_value=0, max_value=5)       # valid precision values
)
def test_humanize_bytes_format(n, precision):
    assume(n != 1)  # skip the special case where it returns "1 B"

    result = humanize_bytes(n, precision)

    # Must return a string
    assert isinstance(result, str)

    # Output must be of the form "<number> <unit>"
    parts = result.split()
    assert len(parts) == 2, f"Unexpected format: {result}"

    number_part, unit = parts

    # Unit must be one of the expected values
    assert unit in VALID_UNITS, f"Unexpected unit: {unit}"

    # Number part must be float-convertible
    try:
        float(number_part)
    except ValueError:
        assert False, f"Not a valid float: {number_part}"

    # Number must respect precision
    if precision == 0:
        assert number_part.endswith(".0") or "." not in number_part
    else:
        if "." in number_part:
            decimal_part = number_part.split(".")[1]
            assert len(decimal_part) <= precision, (
                f"Too many decimals: {number_part} with precision={precision}"
            )
