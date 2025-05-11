import pytest
from hypothesis import given, strategies as st


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


@given(
    group=st.text(min_size=1, max_size=5),
    values=st.lists(st.text(min_size=1, max_size=5), max_size=3)
)
def test_find_entry_points_modern(group, values):
    """
    Test with modern entry_points that use .select(group).
    """
    modern = MockEntryPointsModern({group: values})
    result = find_entry_points(modern, group)
    assert isinstance(result, list)
    assert result == values


@given(
    group=st.text(min_size=1, max_size=5),
    values=st.lists(st.text(min_size=1, max_size=5), max_size=3)
)
def test_find_entry_points_legacy(group, values):
    """
    Test with legacy entry_points that use .get(group).
    """
    legacy = MockEntryPointsLegacy({group: values})
    result = find_entry_points(legacy, group)
    assert isinstance(result, set)
    assert result == set(values)
