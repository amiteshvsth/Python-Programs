# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum number
maximum = num1
if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

# Find the minimum number
minimum = num1
if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3

# Display the results
print(f"The maximum number is {maximum}.")
print(f"The minimum number is {minimum}.")
