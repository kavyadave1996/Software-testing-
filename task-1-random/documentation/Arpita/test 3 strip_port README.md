# Hypothesis test for strip_port function
This test is designed to verify the correctness of the strip_port function, which removes a port number from a hostname string like "example.com:8080".

# Key Components of the Test

- full = f"{hostname}:{port}":
  Builds a combined string like "myserver:3000".


- result = strip_port(full):
Applies the function to remove the port.


- assert result == hostname:
Confirms that the returned result is exactly the original hostname (i.e., everything before the colon).
# what the Test Verifies

- That strip_port():Correctly splits the string at : and returns only the hostname part.
Works across hundreds of random valid hostname/port combinations.


- Prevents future regressions in string-splitting logic.