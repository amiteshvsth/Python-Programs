import pandas as pd

# Reading CSV file using read_csv() method
data = pd.read_csv('data.csv')

# Creating DataFrame from dictionary
dict_data = {'Name': ['John', 'Sarah', 'David', 'Emily'], 'Age': [25, 30, 28, 22], 'Country': ['USA', 'Canada', 'UK', 'Australia']}
df_dict = pd.DataFrame(dict_data)

# Creating DataFrame from list of tuples
tuple_data = [('John', 25, 'USA'), ('Sarah', 30, 'Canada'), ('David', 28, 'UK'), ('Emily', 22, 'Australia')]
df_tuple = pd.DataFrame(tuple_data, columns=['Name', 'Age', 'Country'])

# Displaying Shape, head and tail of DataFrames
print('Shape of data DataFrame:', data.shape)
print('Head of data DataFrame:\n', data.head())
print('Tail of data DataFrame:\n', data.tail())
print('Shape of df_dict DataFrame:', df_dict.shape)
print('Head of df_dict DataFrame:\n', df_dict.head())
print('Tail of df_dict DataFrame:\n', df_dict.tail())
print('Shape of df_tuple DataFrame:', df_tuple.shape)
print('Head of df_tuple DataFrame:\n', df_tuple.head())
print('Tail of df_tuple DataFrame:\n', df_tuple.tail())

# Retrieving rows and columns from data DataFrame
print('\nRows and Columns from data DataFrame:')
print(data.loc[0:2, ['Name', 'Country']])
print(data.iloc[1:3, 1:4])

# Finding maximum and minimum values
print('\nMaximum and Minimum values in data DataFrame:')
print('Maximum Age:', data['Age'].max())
print('Minimum Age:', data['Age'].min())

# Displaying statistical information
print('\nStatistical Information of data DataFrame:')
print(data.describe())

# Performing queries
print('\nQuerying data DataFrame:')
print(data[data['Country'] == 'USA'])

# Data analysis using groupby()
print('\nGrouping data DataFrame by Country:')
grouped_data = data.groupby('Country')
print(grouped_data.mean())
