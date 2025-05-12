# Hypothesis test for split_version function.
In this test we will generate random inputs for the function and will check if it is able to identify valid input and generate output which contains only integer values of any version.

# Key features of the function

- String input

- output is tuple of integers

- Remove '.' between integers.

# Key Components of the Test

- @given(...):

  
- [ ] Hypothesis decorates the test to automatically generate randomized version strings in the format "X.Y.Z", where:
  X, Y, Z are integers from 0 to 999.


st.tuples(...).map(...):
  - [ ] Creates a tuple of three integers.


- [ ] Maps it to a string "X.Y.Z".

split_version(version):This function under test should take a string like "2.5.9" and return (2, 5, 9).

# Assertions (What It Checks)

- result is a tuple

 - result has exactly 3 elements
-  Each element in the tuple is an integer

 # Why the test is valuable
 - Tests a Common Real-World Pattern
 - Uses Randomized Input for Wide Coverage
 - Verifies Function Contract

 #Used procedure
 


