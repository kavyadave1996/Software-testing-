# Test Purpose: To validate that trim_filename() correctly trims filenames to a maximum allowed length, while preserving extensions when possible and without corrupting the filename structure.

- Input Generation: Random filenames (strings of letters, numbers, ., _, -) and random maximum lengths.

# Assertions:

- The result's length must be ≤ max_len (unless unavoidable due to extension size).
- The result must be a valid substring (no strange new characters).
- If trimming isn’t necessary, the filename remains unchanged.