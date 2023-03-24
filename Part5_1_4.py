import re

string = input("Enter a string: ")
match = re.search(r'www\.[a-zA-Z0-9-]+\.com', string)
if match:
    print("Match found!")
else:
    print("Match not found.")
