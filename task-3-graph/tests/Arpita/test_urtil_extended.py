from util import split_version  # adjust import as needed

def test_full_version():
    assert split_version("1.2.3") == (1, 2, 3)

def test_more_than_three_parts():
    assert split_version("1.2.3.4.5") == (1, 2, 3)  # last parts ignored

def test_less_than_three_parts():
    assert split_version("1.2") == (1, 2)

def test_single_part():
    assert split_version("42") == (42,)

def test_empty_string():
    assert split_version("") == ()

def test_non_integer_mid():
    assert split_version("1.two.3") == (1,)  # stops at 'two'

def test_non_integer_first():
    assert split_version("a.2.3") == ()  # fails at first part

def test_non_integer_last():
    assert split_version("1.2.c") == (1, 2)

def test_trailing_dot():
    assert split_version("1.2.") == (1, 2)

def test_leading_dot():
    assert split_version(".2.3") == ()  # first part is empty string → ValueError
