# Haomin Shi City Study - Singapore - for SSCI 204
# 04/09/2018

# imports
import openpyxl
import sys

############

wb1 = openpyxl.load_workbook('data/workBook1.xlsx')
sheet1 = wb1['Sheet1']

# processing Sheets
# basic percentage of population
def process1(sheetT):
    print(type(sheetT))
    totalPopulation = sheetT.cell(row=3,column=2).value

    print("!!!MALE!!! data below")
    for x in range(4, 22):
        percentage = float((sheetT.cell(row=x,column=3).value)/totalPopulation)
        printf('age group is: %s, percentage of male in total population is: %f \n', sheetT.cell(row=x, column=1).value, percentage)
    print("-----------------------------------------------------------------")
    print("!!!FEMALE!!! data below")
    for x in range(4, 22):
        percentage = float((sheetT.cell(row=x,column=4).value)/totalPopulation)
        printf('age group is: %s, percentage of female in total population is: %f \n', sheetT.cell(row=x, column=1).value,percentage)



def printf(format, *args):
    sys.stdout.write(format % args)

def main():
    print("Welcome to Console\n")

    # load a1.xls A1- Resident Population by Age Group, Ethnic Group, Sex and Residential Status.xls

    print("in work book 1 you have: ")
    print(*wb1, sep=", ")
    process1(sheet1)

main()