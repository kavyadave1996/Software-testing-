import time
from typing import List
from hypothesis import given, strategies as st, settings


# === Function Under Test ===

def get_expired_cookies(cookies: str, now: float = None) -> List[dict]:
    now = now or time.time()
    result = []

    if not cookies.strip():
        return result

    cookie_chunks = cookies.split(',')
    for chunk in cookie_chunks:
        parts = chunk.strip().split(';')
        cookie = {'path': '/'}
        for part in parts:
            if '=' in part:
                k, v = map(str.strip, part.split('=', 1))
                if 'name' not in cookie:
                    cookie['name'] = k
                elif k.lower() == 'expires':
                    try:
                        cookie['expires'] = float(v)
                    except ValueError:
                        cookie['expires'] = None
        if 'expires' in cookie and cookie['expires'] is not None:
            if cookie['expires'] <= now:
                result.append({'name': cookie['name'], 'path': cookie.get('path', '/')})
    return result


# === ISP-Style Hypothesis Test (6 × 1 style with 2 input blocks) ===

@settings(max_examples=6)
@given(
    cookie_str=st.sampled_from([
        "id=abc; expires=1000000000",                           # Expired
        "id=abc; expires=3000000000",                           # Not expired
        "id=abc; expires=2000000000",                           # Boundary
        "id=abc",                                               # No expires
        "a=1; expires=1000000000, b=2; expires=3000000000",     # Mixed
        "invalidformatcookie",                                  # Invalid format
    ]),
    now=st.sampled_from([
        1000000001,
        2000000000,
        2000000000,
        2000000000,
        2000000000,
        2000000000,
    ])
)
def test_get_expired_cookies_isp(cookie_str, now):
    print(f"\nTesting with: cookie_str='{cookie_str}', now={now}")
    result = get_expired_cookies(cookie_str, now)

    # Manually matched assertions based on expected output
    if cookie_str == "id=abc; expires=1000000000" and now == 1000000001:
        assert result == [{'name': 'id', 'path': '/'}]
    elif cookie_str == "id=abc; expires=3000000000" and now == 2000000000:
        assert result == []
    elif cookie_str == "id=abc; expires=2000000000" and now == 2000000000:
        assert result == [{'name': 'id', 'path': '/'}]
    elif cookie_str == "id=abc" and now == 2000000000:
        assert result == []
    elif cookie_str == "a=1; expires=1000000000, b=2; expires=3000000000" and now == 2000000000:
        assert result == [{'name': 'a', 'path': '/'}]
    elif cookie_str == "invalidformatcookie" and now == 2000000000:
        assert result == []
