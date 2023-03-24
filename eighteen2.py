# Open the CSV file for reading
with open('data.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Create an empty list to store the rows of data
    rows = []
    
    # Read each row of data from the CSV file and append it to the list
    for row in csv_reader:
        rows.append(row)
