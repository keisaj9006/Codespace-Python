# Get numbers from user
num1 = float(input())
num2 = float(input())
num3 = float(input())

# Check if numbers are in increasing order
if num1 < num2 < num3:
    print("Increasing order")
# Check if numbers are in decreasing order
elif num1 > num2 > num3:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing order")