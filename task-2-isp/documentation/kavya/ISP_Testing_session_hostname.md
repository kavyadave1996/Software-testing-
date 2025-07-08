# ISP Testing for `session_hostname_to_dirname`

This test module applies **Input Space Partitioning (ISP)** and **property-based testing** using the `hypothesis` library to the `session_hostname_to_dirname` method from the `httpie.sessions` module.

## 🧪 Test Overview

We combine multiple partitions of two input arguments:

- `hostname`
- `session_name`

Each test case checks that:

- Colons in hostnames are replaced with underscores.
- The generated path is valid and ends in `.json`.
- The path format matches the expected structure: `sessions/<hostname>/<session_name>.json`.

## 🔢 Input Partitions

We identified the following characteristics and blocks:

| Characteristic        | Block ID | Description                              |
|----------------------|----------|------------------------------------------|
| Host Format          | H1       | Standard domain name                     |
|                      | H2       | Domain name with port                    |
|                      | H3       | IP address                               |
| Hostname Length      | L1       | Short (<= 10 characters)                 |
|                      | L2       | Medium (11–20 characters)                |
|                      | L3       | Long (> 20 characters)                   |
| Session Name Content | S1       | Alphanumeric                             |
|                      | S2       | Special characters                       |
|                      | S3       | Empty string                             |
| Session Name Length  | N1       | Empty                                    |
|                      | N2       | Normal length (5–15 chars)               |
|                      | N3       | Long (> 20 characters)                   |

> **Partition rule:** At least one partition (hostname length) includes ≥ 3 blocks.

## 🧪 Generated Combinations (6 × 4 = 24)

We used `@given()` with `st.sampled_from()` to select specific representative values from each partition.

```python
@given(
    hostname=st.sampled_from([...]),
    session_name=st.sampled_from([...])
)
```

## 📈 Hypothesis Settings

- @settings(max_examples=6) limits test execution to 6 randomly selected input combinations (you can increase this during debugging).

- Each test prints the values it runs with.

## ✅ Assertions

Each test verifies:

- The result is a valid session path.

- Colons are correctly replaced.

- The directory and file formatting is consistent.

## 🗂 Example Output

Sample printed during test run:

```csharp

Testing with: hostname='example.com:443', session_name='dev@2024!'
```

Resulting path:

```bash
sessions/example.com_443/dev@2024!.json
```

## 🛠 How to Run

Ensure you have pytest and hypothesis installed:

```bash
pip install pytest hypothesis
```

Run the tests:

```bash
pytest test_session_hostname.py -s
```

Use -s to show print() output from Hypothesis-generated examples.

## 📌 Notes

- The tests are derived from a systematic input domain model.

- You can expand the partitions or combinations for full path or condition coverage.