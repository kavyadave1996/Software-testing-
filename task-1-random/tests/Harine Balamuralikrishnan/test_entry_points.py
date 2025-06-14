import pytest
from hypothesis import given, assume, strategies as st


class MockEntryPointsModern:
    """
    Mimics modern-style entry_points with a `.select(group=...)` method.
    """
    def __init__(self, data):
        self._data = data

    def select(self, group):
        return self._data.get(group, [])


class MockEntryPointsLegacy(dict):
    """
    Mimics legacy-style entry_points that use .get(group, ...)
    """
    def get(self, group, default=None):
        return super().get(group, default)


def find_entry_points(entry_points, group):
    """
    Return entry points from a group, compatible with both modern and legacy APIs.
    """
    if hasattr(entry_points, "select"):
        return entry_points.select(group=group)
    else:
        return set(entry_points.get(group, ()))


# ----------- TEST CASE 1 -----------

@given(
    group=st.text(min_size=1, max_size=5),  # Random short group name
    values=st.lists(st.text(min_size=1, max_size=5), max_size=3)  # List of short strings
)
def test_find_entry_points_modern(group, values):
    """
    Test with modern entry_points where the group exists in the data.
    """
    modern = MockEntryPointsModern({group: values})  # Create mock with group -> values
    result = find_entry_points(modern, group)        # Call the function with modern-style mock
    assert isinstance(result, list)                  # Ensure return type is a list
    assert result == values                          # Ensure it returns the expected list


# ----------- TEST CASE 2 -----------

@given(
    group=st.text(min_size=1, max_size=5),
    values=st.lists(st.text(min_size=1, max_size=5), max_size=3)
)
def test_find_entry_points_legacy(group, values):
    """
    Test with legacy entry_points where the group exists in the data.
    """
    legacy = MockEntryPointsLegacy({group: values})  # Create legacy mock with group -> values
    result = find_entry_points(legacy, group)        # Call function with legacy-style mock
    assert isinstance(result, set)                   # Legacy should return a set
    assert result == set(values)                     # Ensure set conversion is correct


# ----------- TEST CASE 3 -----------

@given(
    group=st.text(min_size=1, max_size=5),
    other_group=st.text(min_size=1, max_size=5)
)
def test_find_entry_points_modern_group_missing(group, other_group):
    """
    Test modern entry_points when the group is not found.
    """
    assume(group != other_group)                              # Ensure the group is different
    modern = MockEntryPointsModern({other_group: ['x', 'y']}) # Group not present in mock data
    result = find_entry_points(modern, group)
    assert result == []                                       # Should return empty list


# ----------- TEST CASE 4 -----------

@given(
    group=st.text(min_size=1, max_size=5),
    other_group=st.text(min_size=1, max_size=5)
)
def test_find_entry_points_legacy_group_missing(group, other_group):
    """
    Test legacy entry_points when the group is not found.
    """
    assume(group != other_group)                               # Ensure the group is different
    legacy = MockEntryPointsLegacy({other_group: ['a', 'b']})  # Missing group in mock data
    result = find_entry_points(legacy, group)
    assert result == set()                                     # Should return empty set
