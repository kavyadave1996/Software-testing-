
import pytest
from hypothesis import given, strategies as st
from multidict import MultiDict, CIMultiDict
from collections import OrderedDict
from hypothesis import settings, Verbosity
import string



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
@settings(verbosity=Verbosity.verbose, max_examples=2)
@given(
     key =st.text(min_size=1, max_size=2,alphabet=string.ascii_letters),
     value =st.text(min_size=1, max_size=2,alphabet=string.ascii_letters),
)

def test_add_method(key, value):
    """
    Test the add method of HTTPHeadersDict class.
    """
    print(f"Generated key: {key}, value: {value}")  # Log the inputs
    headers = HTTPHeadersDict()
    headers.add(key, value)
    assert headers.getone(key) == value

def test_add_method_invalid_key_value():
    """
    Test the add method of HTTPHeadersDict class with invalid key and value.
    """
    headers = HTTPHeadersDict()
    headers.add(None, None)
    assert headers.getone(None) is None
    headers.add(None, "value")
    assert headers.getone(None) == "value"