# Define a function named 'sum_of_cubes' that takes an integer 'n' as its argument.
def sum_of_cubes(n):
    # Decrement 'n' by 1 to exclude 'n' itself from the sum.
    n -= 1
    # Initialize a variable 'total' to keep track of the sum of cubes.
    total = 0
    
    # Use a 'while' loop to iterate through numbers from 'n-1' down to 1.
    while n > 0:
        # Calculate the cube of the current number 'n' and add it to 'total'.
        total += n * n * n
        # Decrement 'n' by 1 for the next iteration.
        n -= 1
    
    # Return the total sum of cubes.
    return total

# Call the 'sum_of_cubes' function with an argument '3' and print the result.
print("Sum of cubes smaller than the specified number: ", sum_of_cubes(3))
