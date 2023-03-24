import csv

# Open the CSV file for reading
with open('data.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Create an empty list to store the rows of data
    rows = []
    
    # Read each row of data from the CSV file and append it to the list
    for row in csv_reader:
        rows.append(row)

# Generate the HTML table
html_table = '<table>\n'
for row in rows:
    html_table += '<tr>\n'
    for col in row:
        html_table += f'<td>{col}</td>\n'
    html_table += '</tr>\n'
html_table += '</table>'

# Print the HTML table to the console
print(html_table)
