# Define a function named 'odd_product' that takes a list 'nums' as its argument.
def odd_product(nums):
    # Iterate through the indices of the 'nums' list using nested loops.
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Check if 'i' and 'j' are different indices to avoid multiplying the same number.
            if i != j:
                # Calculate the product of elements at indices 'i' and 'j'.
                product = nums[i] * nums[j]
                # Check if the product is an odd number (using bitwise AND with 1).
                if product & 1:
                    # If an odd product is found, return True immediately.
                    return True
    # If no odd product is found, return False.
    return False

# Define three lists of integers.
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]

# Call the 'odd_product' function for each list and print the result.
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
