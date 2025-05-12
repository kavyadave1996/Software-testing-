from typing import Dict, Any, Tuple
from hypothesis import given, strategies as st

from httpie.cli.options import drop_keys  # Replace with actual import

@given(
    config=st.dictionaries(keys=st.text(min_size=1, max_size=5), values=st.integers()),
    blacklist=st.lists(st.text(min_size=1, max_size=5), unique=True)
)
def test_drop_keys_removes_blacklisted(config: Dict[str, int], blacklist: list[str]):
    # Convert list to tuple as required by function signature
    print(f"Generated input: {repr(config)}, {repr(blacklist)}")
    key_blacklist = tuple(blacklist)

    result = drop_keys(config, key_blacklist)

    # Assert all blacklisted keys are not in the result
    for key in key_blacklist:
        assert key not in result

    # Assert all preserved keys have correct values
    for key in result:
        assert key in config
        assert result[key] == config[key]
