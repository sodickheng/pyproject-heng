import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. Pandas Data Structures
# Creating a Pandas Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series:")
print(series)

# Creating a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# 3. Basic Operations
# Reading and Writing Data
# (Note: Uncomment and use actual file paths if you want to test file I/O)
# df = pd.read_csv('file.csv')
# df.to_csv('output.csv', index=False)

# Inspecting the DataFrame
print("\nInspecting DataFrame:")
print(df.head())  # Display the first few rows
print(df.tail())  # Display the last few rows
print(df.info())  # Display basic information about the DataFrame
print(df.describe())  # Display statistical summary of the DataFrame

# Selecting Data
print("\nSelecting Data:")
print(df['Name'])  # Selecting a single column
print(df[['Name', 'Age']])  # Selecting multiple columns
print(df.iloc[0])  # Selecting the first row by index
print(df.loc[0])  # Selecting the first row by label

# 4. Data Manipulation
# Filtering Data
filtered_df = df[df['Age'] > 30]  # Filter rows where 'Age' > 30
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Adding and Modifying Columns
df['Country'] = ['USA', 'USA', 'USA']  # Adding a new column
df['Age'] = df['Age'] + 1  # Modifying an existing column
print("\nDataFrame with new column and modified 'Age':")
print(df)

# Handling Missing Data
df_with_nan = df.copy()
df_with_nan.loc[1, 'Age'] = np.nan  # Introducing a NaN value
print("\nDataFrame with NaN:")
print(df_with_nan)
print(df_with_nan.isnull())  # Checking for missing data
df_with_nan.dropna(inplace=True)  # Dropping rows with missing data
print("\nAfter dropping rows with NaN:")
print(df_with_nan)

# 5. Grouping and Aggregation
grouped = df.groupby('City').mean()  # Grouping by 'City' and calculating the mean
print("\nGrouped DataFrame (mean by City):")
print(grouped)

agg = df.groupby('City').agg({'Age': ['mean', 'min', 'max']})  # Aggregating with multiple functions
print("\nAggregated DataFrame (mean, min, max of Age by City):")
print(agg)

# 6. Merging and Joining Data
# Creating another DataFrame for merging
data2 = {
    'Name': ['Alice', 'Bob', 'Dave'],
    'Salary': [70000, 80000, 90000]
}
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df, df2, on='Name', how='outer')  # Merging DataFrames
print("\nMerged DataFrame:")
print(merged_df)

# 7. Pivot Tables
pivot_table = df.pivot_table(index='City', columns='Name', values='Age', aggfunc='mean')  # Creating a pivot table
print("\nPivot Table:")
print(pivot_table)

# 8. Reshaping Data
# Melting DataFrames
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'City'])  # Melting the DataFrame
print("\nMelted DataFrame:")
print(melted_df)

# Pivoting DataFrames
pivoted_df = melted_df.pivot(index='Name', columns='variable', values='value')  # Pivoting the DataFrame
print("\nPivoted DataFrame:")
print(pivoted_df)

# Working with Time Series Data
date_rng = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
df_time_series = pd.DataFrame(date_rng, columns=['Date'])  # Creating a time series DataFrame
df_time_series['Data'] = np.random.randint(0, 100, size=(len(date_rng)))

df_time_series.set_index('Date', inplace=True)  # Setting the Date column as the index
print("\nTime Series DataFrame:")
print(df_time_series)

# Resampling time series data
resampled_df = df_time_series.resample('3D').mean()  # Resampling time series data (mean every 3 days)
print("\nResampled DataFrame (mean every 3 days):")
print(resampled_df)

# Visualization (optional, requires a display environment)
# df.plot(kind='bar')
# plt.show()
