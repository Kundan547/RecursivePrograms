def subtract(minuend, subtrahend):
  """
  This function subtracts two numbers using recursion (corrected version).

  Args:
      minuend: The number from which we subtract.
      subtrahend: The number we subtract.

  Returns:
      The difference between minuend and subtrahend.
  """

  # Base case: If subtrahend is 0, return minuend (no change).
  if subtrahend == 0:
    return minuend

  # Recursive case: Subtract 1 from minuend and decrement subtrahend (effectively adding the negative of subtrahend).
  # This ensures termination by making subtrahend closer to zero in each recursion.
  return subtract(minuend - 1, subtrahend - 1)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = subtract(num1, num2)
print("The subtraction of the given numbers is:", result)
