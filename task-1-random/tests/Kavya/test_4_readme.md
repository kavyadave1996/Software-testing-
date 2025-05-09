# This test uses the Hypothesis library to perform property-based testing on the get_color function

- The goal is to verify that the function behaves correctly for random combinations of colors and shades, both valid and invalid.

## 🛠 Test Behavior

The test randomly generates:

- A color name (string)
- A shade name (string)

## The function's expected behavior

- If the given color does not exist in the palette → it should return None.

- If the color exists:
      - If the color is a dictionary of shades:
      - If the shade exists → return the corresponding color code.
      - If the shade does not exist → fallback to returning the full color dictionary.
      - If the color is a simple string (not a dict) → directly return the color code.

## 🔎 Why This Test Is Useful

- Ensures the get_color function handles unknown colors gracefully.
- Verifies behavior for colors with and without multiple shades.
- Automatically generates many combinations to catch unexpected errors.
- Confirms consistency of color lookup in the palette.

## 🧪 Tools Used

- Hypothesis – for property-based randomized test input generation.
- pytest – for running the tests and assertions.

## 🧹 Notes

- The palette used in the test includes:

      - Colors with multiple shades (red, blue)
      - Colors with a direct value (green)
      - You may need to adjust the handling if you want to raise an error when a shade is missing (currently, it falls back).
