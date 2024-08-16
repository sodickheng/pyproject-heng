import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
#csv_file_path = '181102-094919_GL30_0228_00001370_NG_WAVE.csv'
csv_file_path = 'xGL200A_T0020_00011906_OK_DATA.csv' # one row
#csv_file_path = 'TestEnglishGL200A_COND.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path,encoding='utf-8')

# Print the content of the CSV file
#print(df)
#print(df.head(5))
#print(df.tail(3))

#result = df[["OKNG", "Shot No.","Total Shot No."]]
#print(result.head())

#result = df[df["Total Shot No."] > 11905]
#print(result)

print(df.iloc[0:10, 2:5])
print(df[["Part Counts"]])

#print(df.iloc[2:10, 1:1].isnull().values.any())
