# Phase 2: Input Space Partitioning – `split_version` Function

## 🧪 Objective

This phase demonstrates **Input Space Partitioning (ISP)** for the `split_version` function, which parses semantic version strings into tuples of integers. We:
- Identified input characteristics
- Derived equivalence classes
- Created representative values
- Built test vectors using `hypothesis`
- Wrote test cases using `pytest`

---

## 🧰 Tools Used

| Tool | Purpose |
|------|---------|
| `pytest` | For running unit and parameterized tests |
| `hypothesis` | For generating test vectors from equivalence classes |

---

## 📝 Function Under Test

```python
def split_version(version: str) -> Tuple[int, ...]:
    parts = []
    for part in version.split(".")[:3]:
        try:
            parts.append(int(part))
        except ValueError:
            break
    return tuple(parts)
