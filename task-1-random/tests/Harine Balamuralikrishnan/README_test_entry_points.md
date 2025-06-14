# Entry Point Testing using Hypothesis

This repository contains a suite of Python tests written using the Hypothesis property-based testing library. These tests verify the behavior of the `find_entry_points` function across both modern and legacy plugin entry point APIs.

## Function Overview: `find_entry_points(entry_points, group)`

This function retrieves plugin entry points for a specified group. It supports both modern and legacy APIs.

### How It Works:

* Modern API: Uses '.select(group=...)` → returns a `list`.
* Legacy API: Uses '.get(group)' → returns a `set`.


## Test Case Explanations

Each test uses `hypothesis` to generate dynamic, randomized input values.

### `test_find_entry_points_modern`

* Tests modern API when the group exists.
* Input: Random short `group`, list of strings.
* Asserts: Output is a list matching the expected value.

### `test_find_entry_points_legacy`

* Tests legacy API when the group exists.
* Input: Same as above.
* Asserts: Output is a `set` of the expected values.

### `test_find_entry_points_modern_group_missing`

* Tests modern API when the group is missing.
* Input: Two different group names.
* Asserts: Output is an empty list (`[]`).

### `test_find_entry_points_legacy_group_missing`

* Tests legacy API with a missing group.
* Input: Mismatched group name.
* Asserts: Output is an empty set (`set()`).

##  Hypothesis Strategy Summary

| Parameter     | Strategy Used                                           | Purpose                                    |
| ------------- | ------------------------------------------------------- | ------------------------------------------ |
| `group`       | `st.text(min_size=1, max_size=5)`                       | Simulates realistic group names            |
| `values`      | `st.lists(st.text(min_size=1, max_size=5), max_size=3)` | Simulates short lists of entry point names |
| `assume(...)` | `assume(group != other_group)`                          | Ensures group-missing cases are tested     |


## Installation

Install required packages using pip:

bash : pip install pytest ,
bash : pip install hypothesis 

Make sure these packages are installed.

## How to Run the Tests

Navigate to the project directory and run: pytest tests/test_entry_points.py


