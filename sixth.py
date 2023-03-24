# Initialize variables
largest_odd = None

# Get user input
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    # Check if number is odd and larger than current largest_odd
    if num % 2 == 1 and (largest_odd is None or num > largest_odd):
        largest_odd = num

# Display result
if largest_odd is not None:
    print(f"The largest odd number is {largest_odd}.")
else:
    print("No odd number was found.")
