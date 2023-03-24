# Get user input
num = int(input("Enter a number: "))

# Initialize variables
sum = 0
order = len(str(num))

# Calculate sum of cubes of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if number is an Armstrong number
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
