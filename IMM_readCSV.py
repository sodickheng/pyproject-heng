import pandas as pd
import numpy as np

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '181102-094919_GL30_0228_00001370_NG_WAVE.csv'
#csv_file_path = 'xGL200A_T0020_00011906_OK_DATA.csv' # one row
#csv_file_path = 'TestEnglishGL200A_COND.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path,encoding='utf-8')

# Print the content of the CSV file
#print(df)

print(df.iloc[7:11, 0:7])
#print(df.dtypes)  # to check data types
#print(type(df))

# Time column
value1 = df.iloc[8,6]  # row and column
converted_value1 = pd.to_numeric(df.iloc[8,6])
print(converted_value1)

# Time column
value2 = df.iloc[9,6]  # row and column
converted_value2 =pd.to_numeric(df.iloc[9,6])
print(converted_value2)

total = converted_value1 + converted_value2
print(f'Sum of converted time : {total}')


# conversion of objects to numeric
#df['column'] = pd.to_numeric(df['column'])

# get values of int64 or objects from dtypes for calculation
#print(df.at[9, "Time"])
#print(df.at[0, "Total Shot No."])






