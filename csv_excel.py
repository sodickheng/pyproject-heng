import csv
import openpyxl

csv_data =[]
with open('Sample.csv') as file_obj:
    reader = csv.reader(file_obj)
    for row in reader:
        csv_data.append(row)

    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in csv_data:
        sheet.append(row)

    wb.save('Sample.xlsx')
