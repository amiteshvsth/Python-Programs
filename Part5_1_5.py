import re

string = input("Enter a string: ")
match = re.search(r'\d+\s+\w+(\s\w+)*\s+\w+\.', string)
if match:
    print("Match found!")
else:
    print("Match not found.")
