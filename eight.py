# Get user input
num = int(input("Enter a number: "))

# Convert number to string and reverse it
str_num = str(num)
rev_str_num = str_num[::-1]

# Check if number is palindrome
if str_num == rev_str_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome")

