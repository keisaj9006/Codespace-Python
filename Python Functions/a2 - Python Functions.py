# Function to calculate the factorial
def factorial(n):
    # Check if the number is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # Check if the number is zero
    elif n == 0:
        return 1
    else:
        result = 1
        # Calculate the factorial
        for i in range(1, n + 1):
            result *= i
        return result

# Test the factorial function
number = int(input("Enter a non-negative integer: "))
print("Factorial of", number, "is", factorial(number))
