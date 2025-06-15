import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from httpie.downloads import trim_filename_if_needed


# 🧪 Test 1: No trimming needed (short name)
# Node + Edge: N1 → N2 → N3 [True] → N4
def test_node_edge_no_trim(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 20)
    filename = "short.txt"
    result = trim_filename_if_needed(filename)
    assert result == filename


# 🧪 Test 2: Trimming required (long name)
# Node + Edge: N1 → N2 → N3 [False] → N5 → N6
def test_node_edge_trim(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 10)
    filename = "verylongfilename.txt"
    result = trim_filename_if_needed(filename)
    assert len(result) <= 10


# 🧪 Test 3: Trimming a filename with no extension
# Node + Edge: N1 → N2 → N3 [False] → N5 → N6 → N7 → N8
def test_trim_filename_no_extension(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 8)
    result = trim_filename_if_needed("verylongname")
    assert len(result) <= 8


# 🧪 Test 4: Trimming a filename where extension is very long
# Node + Edge: N1 → N2 → N3 [False] → N5 → N6 → N7 → N8
def test_trim_filename_with_long_extension(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 10)
    result = trim_filename_if_needed("datafile.reallylongext")
    assert result.endswith(".reallylongext"[:10]) or len(result) <= 10


# 🧪 Test 5: Filename length exactly equal to max limit
# Node + Edge: N1 → N2 → N3 [True] → N4
def test_trim_filename_exact_boundary(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 12)
    result = trim_filename_if_needed("123456789.txt")  # Length = 12
    assert len(result) <= 12
    assert result.endswith(".txt")


# 🧪 Test 6: Empty filename
# Node + Edge: N1 → N2 → N3 [True] → N4 (or early return logic if present)
def test_trim_empty_filename(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 5)
    result = trim_filename_if_needed("")
    assert result == ""


# 🧪 Test 7: Filename with multiple dots (e.g., archive.backup.tar.gz)
# Node + Edge: N1 → N2 → N3 [False] → N5 → N6 → N7 → N8
def test_trim_filename_multiple_dots(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 12)
    result = trim_filename_if_needed("archive.backup.tar.gz")
    assert result.endswith(".gz")
    assert len(result) <= 12


# 🧪 Test 8: When max length is too small to fit the suffix, base name is returned
# Node + Edge: N1 → N2 → N3 [False] → N5 → N6
def test_trim_filename_only_suffix_fits(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 4)
    result = trim_filename_if_needed("superlongfilename.log")
    # With max_len = 4, expect the filename to be truncated to just 4 characters
    assert result == "supe"

