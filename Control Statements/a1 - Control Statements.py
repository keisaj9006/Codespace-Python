# Get numbers from user
num1 = float(input())
num2 = float(input())
num3 = float(input())

# Check if numbers are equal
if num1 == num2 == num3:
    print("All numbers are equal")
# Check if numbers are all different
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different")
else:
    print("Neither all are equal or different")