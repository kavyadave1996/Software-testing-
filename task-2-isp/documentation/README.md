This repository contains a Python function and a Hypothesis-based test suite using Input Space Partitioning (ISP) to verify the behavior of cookie expiration logic.

##  What the Function Does

### `get_expired_cookies(cookies: str, now: float = None) -> List[dict]`

This function parses an input string that mimics HTTP cookie headers and returns all cookies that are expired at the specified `now` timestamp.

### Step-by-Step Logic

1. **Input**:  
   - `cookies`: a string containing one or more cookies  
   - `now`: a Unix timestamp (float). If `None`, uses `time.time()`

2. **Parsing**:
   - Splits the input on commas (`,`) to identify multiple cookies.
   - Further splits each cookie on semicolons (`;`) to extract key-value pairs.

3. **Extracting Fields**:
   - Builds a dictionary for each cookie:
     - `name`: the first key
     - `expires`: if present and valid, converted to float
     - `path`: defaulted to `'/'`

4. **Logic**:
   - If a cookie has a valid `expires` field and `expires <= now`, it is considered expired.

5. **Output**:
   - Returns a list of expired cookies in simplified format:  
     `[{ 'name': 'cookie_name', 'path': '/' }]`


##  What the Test Code Does

The `test_get_expired_cookies_isp.py` file uses the **Hypothesis** testing library and **manual Input Space Partitioning (ISP)** to verify the function’s correctness.

###  ISP Test Design

We identified these characteristics and blocks:

| Characteristic     | Equivalence Classes (Blocks)                          |
|--------------------|--------------------------------------------------------|
| Cookie Format      | Proper (`expires` present), Missing `expires`, Invalid |
| Expiry Timing      | Expired, Future, Boundary                              |
| Number of Cookies  | Single, Multiple                                       |

We created 12 test vectors covering all combinations across these partitions.

###  Test Strategy

- Uses `@given(st.sampled_from([...]))` to randomly run one of the 12 vectors per test
- Each test vector includes:
  - `cookie_str`: the cookie string input
  - `now`: the current time reference
  - `expected`: list of expired cookies expected in output
- Asserts that the result from the function exactly matches the expected list

##  Requirements

bash : pip install pytest ,bash : pip install hypothesis

##  Running the Tests

To run the ISP tests:
bash : pytest test_get_expired_cookies_isp.py -v


