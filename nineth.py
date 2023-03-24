# Get string input from user
string = input("Enter a string: ")

# a) Count Number of Vowel in given string
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

# b) Count Length of string (do not use Len ())
count = 0
for char in string:
    count += 1
print(f"Length of string: {count}")

# c) Reverse string
rev_string = ""
for i in range(len(string)-1, -1, -1):
    rev_string += string[i]
print(f"Reversed string: {rev_string}")

# d) Find and replace operation
find_str = input("Enter string to find: ")
replace_str = input("Enter string to replace: ")
new_string = string.replace(find_str, replace_str)
print(f"New string: {new_string}")

# e) Check whether string entered is a palindrome or not
if string == string[::-1]:
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
