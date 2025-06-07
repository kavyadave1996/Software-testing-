# 🎨 Color Palette Retrieval Test Suite

This repository provides a robust test suite for validating color lookup behavior using the `get_color` function. The tests are implemented using `pytest` and [Hypothesis](https://hypothesis.readthedocs.io/) to automatically generate a wide range of input scenarios.

---

## 📌 Function Under Test

```python
def get_color(color: PieColor, shade: str, *, palette=COLOR_PALETTE) -> Optional[str]:
    if color not in palette:
        return None
    color_code = palette[color]
    if isinstance(color_code, dict) and shade in color_code:
        return color_code[shade]
    else:
        return color_code
```

This function looks up color values from a nested color palette. The palette can contain:

- Flat color codes (e.g., "green": "#00ff00")

- Shade dictionaries (e.g., "red": {"light": "#ffcccc", "dark": "#990000"})

## ✅ Test Strategy

The test_get_color function performs property-based testing by generating random color and shade inputs. It then checks the correctness of the returned color code based on the test palette.

### 🧪 Sample Palette Used in Test

```python

palette = {
    "red": {"light": "#ffcccc", "dark": "#990000"},
    "blue": {"light": "#ccccff", "dark": "#000099"},
    "green": "#00ff00"
}
```

## ✅ Assertions Checked

- If the color is not in the palette → result should be None.

- If the color maps to a dictionary and the shade exists → correct shade value should be returned.

- If the color maps to a dictionary and the shade doesn't exist → None should be returned.

- If the color maps directly to a string → that string should be returned.

| Decorator      | Purpose                                                        |
|----------------|----------------------------------------------------------------|
| @given(...)    | Generates random strings for color and shade.           |
| @settings(...) | Controls verbosity and number of generated test cases

## ▶️ Running the Test

1. Install Dependencies

```bash
pip install pytest hypothesis
```

2. Run the Test

```bash
pytest -s
```

Use -s to show print() output for generated values.

## 💡 Example Output

```css

test_colors.py Trying example: test_get_color(color='red', shade='light')
Generated inputs -> color: red, shade: light