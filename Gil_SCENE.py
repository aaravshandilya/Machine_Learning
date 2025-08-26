#from pyqubo import Array
# come up with a python program that comes up with a 100 random positive number or even 10.
# then convert to array and then check difference
#===================================================================================================================================================================================
#Python Script for generating a array for a 100 random integers
import random

def generate_random_integer_list(length, min_val, max_val):
  """
  Generates a list of random integers.

  Args:
    length: The desired number of integers in the list.
    min_val: The minimum possible value for the random integers (inclusive).
    max_val: The maximum possible value for the random integers (inclusive).

  Returns:
    A list containing 'length' random integers within the specified range.
  """
  random_integers = [random.randint(min_val, max_val) for _ in range(length)]
  return random_integers

# Example usage:
# Generate a list of 100 random integers between 1 and 100
pyquboList = generate_random_integer_list(10, 0, 100)
print(pyquboList)

#==================================================================================================================================================================================