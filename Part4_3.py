import pandas as pd

# read csv file and create a dataframe
df = pd.read_csv('example.csv')

# display the first 5 rows of the dataframe
print(df.head())

# display the shape of the dataframe
print('Shape of dataframe:', df.shape)

# display the last 5 rows of the dataframe
print(df.tail())

# select a particular column of the dataframe
print(df['Name'])

# select a particular row of the dataframe
print(df.loc[1])

# find the maximum value in a particular column
print('Maximum Age:', df['Age'].max())

# find the minimum value in a particular column
print('Minimum Age:', df['Age'].min())

# display statistical information of the dataframe
print(df.describe())

# perform a query on the dataframe
print(df[df['Age'] > 30])

# drop rows with missing data
df = df.dropna()

# display the dataframe after handling missing data
print(df)
