# Function to calculate the factorial of a positive integer
def factorial(n):
    assert n >= 0, "Input must be a non-negative integer"  # Check that the input is non-negative

    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test the factorial function
print(factorial(5))  # This will work as expected, and the result is 120

# Now, let's test it with an invalid input
# print(factorial(-3))  # This will raise an AssertionError with the provided message
