# Hypothesis test for drop_keys function 
For the test 4 we used drop_key function which will block the keys that are not included in the dictionary and we will test the validity of the function with hypothesis test.
# Key Features of the Function

- Input: A dictionary (config) and a tuple of keys to remove (key_blacklist)

- Output: A new dictionary where all keys in key_blacklist are removed

- Non-destructive: Does not modify the original input dictionary

- Use case: Useful for filtering out sensitive or irrelevant keys (e.g., passwords, headers) from configurations or data before processing

# What the Test Does

- Uses Hypothesis to generate:

   - [ ] A random dictionary config (keys: short strings, values: integers)

   
   - [ ] A random list of keys blacklist (strings to be dropped)

  
- Converts the blacklist into a tuple (as required by drop_keys)
- Checks two main things:
   - [ ] All blacklisted keys are absent from the returned result.
   
   - [ ] All remaining keys in the result



# Why the Test Is Important

- Ensures correctness: Confirms drop_keys removes only specified keys while preserving valid ones and their values.

- Covers edge cases: Handles scenarios like empty blacklists, missing keys, or removing all keys.

- Prevents future bugs: Acts as a safeguard against regressions in key-filtering logic used in real-world tools.   

# Test process
To test the function we used VS code as our code editor.We installed python for our coding language.Then we set up an environment to run our code.We installed pytest, hypothesis and other necessary libraries for this test. Then we use different strategies for different functions to generate valid inputs.


- Environment set up:conda create --name myenv python=3.10



- Installing pytest:conda install pytest