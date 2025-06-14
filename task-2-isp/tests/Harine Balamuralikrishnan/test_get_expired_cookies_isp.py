import time
from hypothesis import given, strategies as st
from typing import List


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


@given(
    st.sampled_from([
        # ---- Single Cookies ----
        ("id=abc; expires=1000000000", 1000000001, [{'name': 'id', 'path': '/'}]),  # T1: expired
        ("id=abc; expires=3000000000", 2000000000, []),                             # T2: future
        ("id=abc; expires=2000000000", 2000000000, [{'name': 'id', 'path': '/'}]),  # T3: boundary
        ("id=abc", 2000000000, []),                                                 # T4: no expires
        ("invalidformatcookie", 2000000000, []),                                    # T5: invalid format

        # ---- Multiple Cookies ----
        ("a=1; expires=1000000000, b=2; expires=3000000000", 2000000000, [{'name': 'a', 'path': '/'}]),  # T6: one expired
        ("a=1; expires=3000000000, b=2; expires=4000000000", 2000000000, []),                             # T7: both future
        ("a=1; expires=2000000000, b=2; expires=2000000000", 2000000000, [{'name': 'a', 'path': '/'}, {'name': 'b', 'path': '/'}]),  # T8: both boundary
        ("a=1, b=2", 2000000000, []),                                                                     # T9: no expires, multiple
        ("randomgarbage, moregarbage", 2000000000, []),                                                   # T10: malformed multiple

        # ---- Mixed Scenarios ----
        ("a=1; expires=1000000000, b=2", 2000000000, [{'name': 'a', 'path': '/'}]),                        # T11: one with and one without expires
        ("a=1; expires=1000000000, b=2; expires=2000000000", 2000000000, [{'name': 'a', 'path': '/'}, {'name': 'b', 'path': '/'}])   # T12: both expired
    ])
)
def test_get_expired_cookies_isp(data):
    cookie_str, now, expected = data
    result = get_expired_cookies(cookie_str, now)
    assert result == expected
