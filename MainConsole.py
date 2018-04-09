# Haomin Shi City Study - Singapore - for SSCI 204
# 04/09/2018

# imports
import openpyxl

############

print("Welcome to Console\n")

# load a1.xls A1- Resident Population by Age Group, Ethnic Group, Sex and Residential Status.xls
wb1 = openpyxl.load_workbook('data/workBook1.xlsx')
print("in work book 1 you have: ")
print(*wb1, sep=", ")

sheet1 = wb1['Sheet1']

for x in range(4, 22):
    print(sheet1.cell(row = x,column=1).value)
