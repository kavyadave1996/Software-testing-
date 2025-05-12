# Hypothesis test for valid mime_type function
This phase 1 of our project aims to test a function using hypothesis library and evaluate the validity of the function. For the 1st test we are using mime_type function.

# key properties of the function

- Input is string

- Input can contain only one backslash

- output is string same as input.
- example:'text/csv'

# What the test does


- Ensures that the input string contains exactly one /, which is required in valid MIME types.

- Uses Hypothesis to generate randomized but structured test strings in the "type/subtype" format.

- Implement assertion to simulate real-world MIME types such as:

   1. text/html

   2. application/xml

   3. image/png


 # Why the Test is Valuable
 
- Tests syntactic correctness  

- Verifies semantic relevance, since MIME types are commonly used in HTTP headers and REST APIs

- Mimics realistic usage scenarios, ensuring the function works with actual formats seen in production systems.

# process of the test
To test the function we used VS code as our code editor.We installed python for our coding language.Then we set up an environment to run our code.We installed pytest, hypothesis and other necessary libraries for this test. Then we use different strategies for different functions to generate valid inputs.

- Environment set up:conda create --name myenv python=3.10

- Installing pytest:conda install pytest