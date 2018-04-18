import sys
import openpyxl

total_population = 5607000
#peopl
total_landArea = 278.2
#mile^2
total_gdp = 297000000000
#billion $ USD 2016

def populationDensityCalc():
    return total_population/total_landArea

def gdpPercapita():
    return total_gdp/total_population

def calcWorkingPopLocal():
    wb1 = openpyxl.load_workbook(
        'data/workBook2.xlsx')  # load workBook2.xlsx this is about the household that is working etc.
    sheet1 = wb1['Sheet1']
    total_amount_of_households = sheet1.cell(row=8, column=4).value # stop at 21
    total_amount_of_households_thats_not_working = sheet1.cell(row=7, column=4) # stop at 21
    for x in range(4, 21):






def printf(format, *args):
    sys.stdout.write(format % args)



def main():
    printf("Population Density is: %d people/mi^2 \n", populationDensityCalc())
    printf("GDP per capita is: %d USD", gdpPercapita())


main()

