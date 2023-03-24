import csv

# Open the CSV file and create a CSV reader object
with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    # Print each row in the CSV file
    for row in csvreader:
        print(row)

    # Reset the file pointer to the beginning
    csvfile.seek(0)

    # Skip the header row
    next(csvreader)

    # Calculate the total sales
    total_sales = 0
    for row in csvreader:
        total_sales += int(row[1])

    print(f"Total sales: {total_sales}")
