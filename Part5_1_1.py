import re

string = input("Enter a string: ")
match = re.search(r'b[i|u|a]t|h[i|a|u]t', string)
if match:
    print("Match found!")
else:
    print("Match not found.")
