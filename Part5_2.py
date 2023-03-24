import re

# Sample input telephone numbers
telephone_numbers = ['800-555-1212', '555-1212', '(800) 555-1212', '5551212']

# Regular expression to match telephone numbers with optional area codes and parentheses/hyphens
pattern = re.compile(r'^(\(?(\d{3})\)?[-]?)?(\d{3})[-]?(\d{4})$')

for number in telephone_numbers:
    # Check if the number matches the pattern
    match = pattern.match(number)
    
    if match:
        # Extract the area code and phone number
        area_code = match.group(2) if match.group(2) else ''
        phone_number = '-'.join([match.group(3), match.group(4)])
        
        # Print the formatted number
        formatted_number = '-'.join([area_code, phone_number]) if area_code else phone_number
        print(formatted_number)
    else:
        print('Invalid telephone number:', number)
