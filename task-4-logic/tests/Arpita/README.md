# Phase 4: Logic Coverage – HTTPie CLI

## 🧠 Objective

This phase focuses on applying logic coverage criteria to the function `http_status_to_exit_status(http_status, follow)` from the HTTPie CLI project. The goal is to:
- Achieve logic coverage using Clause Coverage (CC), Correlated Active Clause Coverage (CACC), and Inactive Clause Coverage (ICC)
- Extend test coverage and improve line/branch coverage metrics
- Ensure correctness across all return paths and edge conditions

---

## 🧩 Function Under Test

```python
def http_status_to_exit_status(http_status, follow):
    if 300 <= http_status <= 399 and not follow:
        return ExitStatus.ERROR_HTTP_3XX
    elif 400 <= http_status <= 499:
        return ExitStatus.ERROR_HTTP_4XX
    elif 500 <= http_status <= 599:
        return ExitStatus.ERROR_HTTP_5XX
    else:
        return ExitStatus.SUCCESS
File: httpie/status.py

This function determines the correct program exit code based on HTTP status codes and the follow flag.

🧪 Running the Tests
🔹 Run Only the Logic Coverage Tests
cd code/cli/tests
pytest test_http_status_logic_coverage.py
