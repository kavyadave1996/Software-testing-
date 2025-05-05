# Hypothesis Testing for add Method in Header Collection
- This project uses property-based testing with the Hypothesis library to test the behavior of the add method in a custom header collection class (similar to HTTP headers management).

# 📜 About the add Method
- The add(key, value) method:
- Adds a new header key-value pair.
- Updates an existing header value.
- Overwrites previous None values when necessary.
- If the given value is None, it sets the header key to None.

# Testing this method is important to ensure consistent and predictable behavior across a wide range of dynamic inputs.

# 🧪 What the Test Does: The test randomly generates:
- A header key (string of 1–20 characters).
- A header value, which can either be a random string or None.

For each random key and value:
- It first sets the header key to None.
- Then it adds the new generated value for the same key.
- It asserts that the final value associated with the key matches the newly added value.

# This helps ensure that: Adding a header works correctly.

- Updating a header correctly replaces old values.
- Setting a header to None behaves properly.

# 🛠 How to Run the Test
- Install the required libraries if you haven't already:
- pip install hypothesis pytest
- Save the test file (e.g., test_headers.py).
- Run the test with: pytest test_headers.py

# Hypothesis will automatically generate and run hundreds of randomized test cases to find any potential issues.

