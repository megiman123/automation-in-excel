import openpyxl as xl
from openpyxl.chart import Reference,BarChart
wb = xl.load_workbook('Book1.xlsx')
sheet = wb['Sheet1']
cell = sheet.cell(1,1)
for row in range (2,sheet.max_row+1):
    cell =  sheet.cell(row,3)
    correct = cell.value * 0.9
    corrected_cell = sheet.cell(row,4)
    corrected_cell.value = correct
wb.save('Book2.xlsx')
