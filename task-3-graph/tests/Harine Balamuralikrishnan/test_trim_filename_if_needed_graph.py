import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from httpie.downloads import trim_filename_if_needed
# Node + Edge: Path N1 → N2 → N3 [True] → N4 (No trim)
def test_node_edge_no_trim(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 20)
    filename = "short.txt"
    result = trim_filename_if_needed(filename)
    assert result == filename
# Node + Edge: Path N1 → N2 → N3 [False] → N5 → N6 (Trim)
def test_node_edge_trim(monkeypatch):
    monkeypatch.setattr("httpie.downloads.get_filename_max_length", lambda _: 10)
    filename = "verylongfilename.txt"
    result = trim_filename_if_needed(filename)
    assert len(result) <= 10
