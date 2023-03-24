import matplotlib.pyplot as plt
import csv

# Reading data from CSV file
with open('data.csv') as csv_file:
    data = list(csv.reader(csv_file))

# Extracting x and y values from data
x = [row[0] for row in data]
y = [int(row[1]) for row in data]

# Creating bar chart
plt.bar(x, y)
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Creating histogram
plt.hist(y, bins=5)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Creating pie chart
plt.pie(y, labels=x)
plt.title('Pie Chart')
plt.show()

# Creating line chart
plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
