import re

string = input("Enter a string: ")
match = re.search(r'\b\w+,\s\w\.\b', string)
if match:
    print("Match found!")
else:
    print("Match not found.")
