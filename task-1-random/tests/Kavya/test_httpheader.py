
import pytest
from hypothesis import given, strategies as st, assume
from multidict import MultiDict, CIMultiDict
from collections import OrderedDict
from hypothesis import settings, Verbosity
import string
# Global counter for Hypothesis test executions
hypothesis_case_count = 0

class BaseMultiDict(MultiDict):
    """
    Base class for all MultiDicts.
    """
class HTTPHeadersDict(CIMultiDict, BaseMultiDict):
    """
    Headers are case-insensitive and multiple values are supported
    through the `add()` API.
    """

    def add(self, key, value):
            """
            Add or update a new header.

            If the given `value` is `None`, then all the previous
            values will be overwritten and the value will be set
            to `None`.
            """
            if value is None:
                self[key] = value
                return None

            # If the previous value for the given header is `None`
            # then discard it since we are explicitly giving a new
            # value for it.
            if key in self and self.getone(key) is None:
                self.popone(key)

            super().add(key, value)
@settings(verbosity=Verbosity.verbose, max_examples=1)
@given(
     key =st.text(min_size=1, max_size=2,alphabet=string.ascii_letters),
     value =st.text(min_size=1, max_size=2,alphabet=string.ascii_letters),
)

# Assuming HTTPHeadersDict and add method as defined in your code above.

def test_add_new_header(key, value):  # ✅ Accept parameters
    headers = HTTPHeadersDict()
    headers.add(key, value)
    assert headers.getone(key) == value


@settings(verbosity=Verbosity.verbose, max_examples=1)
@given(key=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"])))
def test_add_none_value_overwrites(key):
    headers = HTTPHeadersDict()
    headers.add(key, None)
    print(f"Trying example: test_add_none_value_overwrites(key='{key}', value=None)")
    assert headers[key] is None

@settings(verbosity=Verbosity.verbose, max_examples=1)
@given(
    key=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"])),
    value=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"]))
)
def test_replace_none_with_value(key, value):
    headers = HTTPHeadersDict()
    headers.add(key, None)
    headers.add(key, value)
    print(f"Trying example: test_replace_none_with_value(key='{key}', value='{value}')")
    assert headers.getall(key) == [value]

@settings(verbosity=Verbosity.verbose, max_examples=1)
@given(
    key=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"])),
    value1=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"])),
    value2=st.text(min_size=1, max_size=10, alphabet=st.characters(blacklist_categories=["Cs"]))
)
def test_add_multiple_values_same_key(key, value1, value2):
    assume(value1 != value2)  # optional: to avoid duplicate test input
    headers = HTTPHeadersDict()
    headers.add(key, value1)
    headers.add(key, value2)
    print(f"Trying example: test_add_multiple_values_same_key(key='{key}', value1='{value1}', value2='{value2}')")
    assert headers.getall(key) == [value1, value2]
