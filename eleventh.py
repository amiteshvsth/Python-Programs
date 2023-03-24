def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Get input from user
n = int(input("Enter a number: "))

# Display Fibonacci sequence up to n
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))
