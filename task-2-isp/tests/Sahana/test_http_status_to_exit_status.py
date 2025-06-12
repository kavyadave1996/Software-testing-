import pytest
from hypothesis import given, strategies as st, settings
from httpie.status import http_status_to_exit_status, ExitStatus  # Adjust import path if needed

# ISP Test Cases: 6 combinations

@settings(max_examples=6)  # Run exactly 6 combinations
@given(
    http_status=st.sampled_from([
        200,  # A1 - C1: Success typical
        299,  # A1 - C2: Success boundary
        302,  # A2 - C1: Redirect typical
        399,  # A2 - C2: Redirect boundary
        404,  # A3 - C1: Client error
        600   # C3: Out-of-range
    ]),
    follow=st.sampled_from([False, True])  # B1 and B2
)
def test_http_status_to_exit_status_limited(http_status, follow):
    """ISP: Combined test of http_status (q1, q3) and follow flag (q2)"""

    print(f"\nTesting with: http_status = {http_status}, follow = {follow}")

    result = http_status_to_exit_status(http_status, follow)

    # === Assertions ===
    if 300 <= http_status <= 399 and not follow:
        assert result == ExitStatus.ERROR_HTTP_3XX
    elif 400 <= http_status <= 499:
        assert result == ExitStatus.ERROR_HTTP_4XX
    elif 500 <= http_status <= 599:
        assert result == ExitStatus.ERROR_HTTP_5XX
    else:
        assert result == ExitStatus.SUCCESS

# Annotations for ISP Blocks (for comments/documentation):
# You can annotate each test vector combination like this:

# Test: A2 (300–399) + B1 (follow = False) + C1 (typical)
# Input: http_status = 302, follow = False

# Testing with: http_status = 404, follow = True
# → A3 (Client Error) + B2 (follow = True) + C1

# @settings(max_examples=6) decorator added to ensure
# Hypothesis runs 6 combinations only (for controlled execution)

# In your @given decorator, you are combining:
# - 6 possible values for http_status (from q₁ and q₃)
#     → Includes typical (C1), boundary (C2), and invalid (C3)
# - 2 possible values for follow (False, True)
#     → Corresponds to B1 and B2

# Hypothesis will dynamically combine these while staying within the 6-test limit.
