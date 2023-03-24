def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from user
n = int(input("Enter a number: "))

# Display factorial sequence up to n
if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("Factorial sequence:")
    for i in range(n+1):
        print(factorial(i))
