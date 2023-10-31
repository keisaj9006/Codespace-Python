# Function to check if a number is prime
def isPrime(number):
    # Check if the number is less than or equal to 1
    if number <= 1:
        return False
    # Check if the number is divisible by any number from 2 to the number - 1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Test the isPrime function
number = int(input("Enter a number: "))
if isPrime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")
