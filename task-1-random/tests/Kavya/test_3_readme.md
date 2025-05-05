# This test uses the Hypothesis library to perform property-based testing on the load_text_file function.
- It generates random binary file contents to ensure that the function correctly handles both:
-✅ Valid UTF-8 text files
-🚫 Invalid binary files that are not UTF-8

# 🛠 Test Behavior
For each generated random content:
- If the file content can be decoded as UTF-8, load_text_file must return the decoded text as a string.
- If the file content cannot be decoded as UTF-8, load_text_file must raise a ParseError.
- The test automatically detects whether decoding should succeed or fail by attempting to decode the random bytes.

# Why This Is Important
- Ensures the function is robust against different types of file content.
- Automatically checks thousands of random edge cases without writing them manually.
- Detects subtle bugs related to Unicode handling and file reading.

# Tools Used
- Hypothesis – for random input generation and property-based testing.
- pytest – to manage assertions and error checking.