from main import get_data
import xlsxwriter
row = 0
column = 1
symbols_to_letters={1:'A',2:'B',3:'C',4:'D'}
workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Image')
worksheet.write('C1', 'Price')
worksheet.write('D1', 'Description')

data = get_data()
for cell in data:
    column +=1
    for char in cell:
        row+=1
        worksheet.write(f'{symbols_to_letters[row]}{column}', char) #make xl symbols
    row = 0

workbook.close()