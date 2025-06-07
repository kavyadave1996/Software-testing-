# HTTPHeadersDict Testing with Pytest and Hypothesis

This project contains tests for the `HTTPHeadersDict` class, which extends `CIMultiDict` to manage HTTP headers with case-insensitivity and multi-value support.

---

## Test Overview

The `add` method of `HTTPHeadersDict` is tested with 4 key scenarios:

1. **Add a header with a `None` value**, verifying it stores `None` correctly.
2. **Replace a header value that was `None` with a new string value**, ensuring previous `None` is removed.
3. **Add multiple values to the same header key**, confirming all values are stored and retrieved.
4. **(Optional) Basic add with manual/static values** — can be included as needed.

---

## Testing Frameworks Used

- **[pytest](https://docs.pytest.org/)** for test discovery and assertions.
- **[Hypothesis](https://hypothesis.readthedocs.io/)** for property-based testing and automatic input generation.

---

## Hypothesis Decorators Explained

- `@given(...)`  
  Auto-generates test inputs based on specified strategies. For example:

```python
@given(key=st.text(min_size=1, max_size=10))
```

generates random strings of length 1 to 10 as the key argument.

- @settings(...)

Controls how Hypothesis runs tests:

- max_examples limits the number of generated test cases per test.

- verbosity controls the amount of logging output during test runs.

## Example

```python
@settings(verbosity=Verbosity.verbose, max_examples=3)
```

## How to Run the Tests

1. Install dependencies

```bash
pip install pytest hypothesis multidict
```

2.Run tests with pytest

```bash
pytest -s
```

- The -s option allows printing output during test runs.

- Hypothesis tests will print generated inputs to the console for transparency.

## Example Test Function Using Hypothesis

```python
from hypothesis import given, strategies as st, settings, Verbosity

@settings(verbosity=Verbosity.verbose, max_examples=3)
@given(
    key=st.text(min_size=1, max_size=10),
    value=st.text(min_size=1, max_size=10)
)
def test_add_method(key, value):
    headers = HTTPHeadersDict()
    headers.add(key, value)
    assert headers.getone(key) == value
```

This test automatically tries 3 different randomly generated keys and values.

## Notes

We exclude control characters from test inputs to avoid invalid header keys/values.

The tests ensure the add method behaves correctly when:

- Adding new headers.

- Adding None values.

- Replacing None values.

- Handling multiple values under the same header key