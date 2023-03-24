import pandas as pd

# Load the CSV file
df = pd.read_csv('data.csv')

# Clean up the data by removing any rows with missing or incorrect data
df = df.dropna()  # Remove any rows with missing data
df = df[df['age'] >= 18]  # Remove any rows with invalid age data

# Calculate the mean age and salary
mean_age = df['age'].mean()
mean_salary = df['salary'].mean()

# Replace any missing data in the age and salary columns with the mean values
df['age'].fillna(mean_age, inplace=True)
df['salary'].fillna(mean_salary, inplace=True)

# Display the cleaned data
print(df)
