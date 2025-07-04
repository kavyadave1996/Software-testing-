import pytest
from httpie.status import http_status_to_exit_status, ExitStatus  # Adjust import path as needed

# ---------- Clause Coverage (CC) ----------

def test_cc_redirect_clause_true():
    # 302 is in 300–399, follow is False → both clauses True
    assert http_status_to_exit_status(302, follow=False) == ExitStatus.ERROR_HTTP_3XX

def test_cc_redirect_clause_false_follow():
    # 302 is in 300–399, follow is True → second clause False
    assert http_status_to_exit_status(302, follow=True) == ExitStatus.SUCCESS


# ---------- Correlated Active Clause Coverage (CACC) ----------

def test_cacc_controlled_clause_effect():
    # Demonstrates how changing `follow` alone changes the outcome
    result1 = http_status_to_exit_status(301, follow=False)  # Both clauses True → redirect error
    result2 = http_status_to_exit_status(301, follow=True)   # Clause B False → skips to else
    assert result1 == ExitStatus.ERROR_HTTP_3XX
    assert result2 == ExitStatus.SUCCESS


# ---------- Inactive Clause Coverage (ICC) ----------

def test_icc_http_4xx():
    # Clause A+B from first predicate are irrelevant
    assert http_status_to_exit_status(404, follow=False) == ExitStatus.ERROR_HTTP_4XX
    assert http_status_to_exit_status(404, follow=True) == ExitStatus.ERROR_HTTP_4XX

def test_icc_http_5xx():
    assert http_status_to_exit_status(503, follow=True) == ExitStatus.ERROR_HTTP_5XX

def test_icc_success_2xx():
    assert http_status_to_exit_status(200, follow=True) == ExitStatus.SUCCESS

def test_icc_success_out_of_range():
    # Out of defined ranges → should be treated as SUCCESS
    assert http_status_to_exit_status(600, follow=False) == ExitStatus.SUCCESS
