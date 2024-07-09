# 1) install pandas : pip install pandas

# 2) import pandas
import pandas as pd

# 3) read csv file
csv = pd.read_csv('SampleTest.csv')

# 4) create excel writer
excelWriter = pd.ExcelWriter('newSampleTest.xlsx')

# 5) convert csv to excel
csv.to_excel(excelWriter)

# 6) save to excel file
excelWriter._save()