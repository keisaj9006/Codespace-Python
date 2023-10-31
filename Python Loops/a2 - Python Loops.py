# Get the input number
number = int(input("Input a number: "))

# Create the multiplication table
for i in range(1, 11):
    result = number * i # Calculate multiplication
    print(f"{number} x {i} = {result}")
