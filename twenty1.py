import json

# Load JSON data from a file
with open('data.json') as json_file:
    data = json.load(json_file)

# Print the loaded data
print(data)

# Access specific data from the loaded JSON object
print(data['name'])
print(data['age'])

# Convert a Python object to JSON and write it to a file
new_data = {
    'name': 'Alice',
    'age': 25
}

with open('new_data.json', 'w') as json_file:
    json.dump(new_data, json_file)
