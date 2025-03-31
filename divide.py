# Get input from the user
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# Check for division by zero
if denominator != 0:
    result = numerator / denominator
    print("The result of the division is:", result)
else:
    print("Error: Division by zero is not allowed.")
