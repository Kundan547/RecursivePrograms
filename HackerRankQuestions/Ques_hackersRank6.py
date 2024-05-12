def recursive_product(x, y):
  """
  This function calculates the product of two numbers (x and y) using a recursive approach.

  Args:
      x (int): The first number.
      y (int): The second number.

  Returns:
      int: The product of x and y.

  Raises:
      ValueError: If either x or y is zero.
  """

  if x == 0 or y == 0:
    raise ValueError("Product of zero with any number is zero. Use a non-zero value for both arguments.")
  elif y == 1:
    return x  # Base case: product of x and 1 is simply x
  else:
    # Recursive case: product of x and y is x multiplied by the product of x and (y-1)
    return x * recursive_product(x, y - 1)

# Example usage
product = recursive_product(5, 3)
print(product)  # Output: 15
