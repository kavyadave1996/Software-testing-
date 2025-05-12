# Hypothesis test for drop_keys function 

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