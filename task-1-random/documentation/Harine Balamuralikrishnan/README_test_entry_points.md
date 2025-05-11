🧪 Hypothesis Testing for `find_entry_points()` in Entry Point Collection

📜 About the `find_entry_points()` Function

The `find_entry_points()` function:

* Accepts an `entry_points` object and a `group` name.
* Returns a list (or set) of entry points for the given group.
* Supports both:

  * Modern API: `.select(group=...)`
  * Legacy API: `.get(group, default)`

This makes it adaptable to different Python packaging ecosystems and ensures backward compatibility.

🧪 What the Test Does

The test uses the Hypothesis library to randomly generate:

* A group name: a short string (1–5 characters)
* A list of values: 1–3 plugin strings, each 1–5 characters long

It checks behavior for both API styles:

1. Modern-style mock (`MockEntryPoints`) using `.select(group=...)`
2. Legacy-style dict (`LegacyEntryPoints`) using `.get(group, ...)`

For each randomly generated test case, it:

* Creates a simulated `entry_points` object.
* Calls `find_entry_points(...)`.
* Asserts the correct values are returned for the specified group.

✅ This Ensures That:

* Entry points are retrieved correctly for any valid group.
* Modern and legacy APIs are both fully supported.
* No unexpected exceptions are raised due to malformed group data.

🛠️ How to Run the Test
Make sure you have installed the required libraries: pip install hypothesis pytest
```
Then run the test using:pytest test_find_entry_points.py
```

Hypothesis will generate hundreds of combinations to robustly test the input space and confirm that all edge cases behave as expected.


