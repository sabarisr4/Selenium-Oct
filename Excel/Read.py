import openpyxl
path="Example.xlsx"
wbobj=openpyxl.load_workbook(path) #load the workbook

sheet=wbobj.active #open the sheet


max_col=sheet.max_column
print("max no of columns",max_col)
max_row=sheet.max_row
print("max no of rows",max_row)


c1=sheet.cell(row=2,column=1)
print(c1.value)


c6=sheet["B2"]
print(c6.value)

c4=sheet["C2"]
print(c4.value)

print("printing column",c4.value) #Print the column value

for i in range (1,max_row+1):
    ce=sheet.cell(row=i,column=2)
    print(ce.value)

for i in range(1, max_col + 1):
    cell = sheet.cell(row=1, column=i)
    print(cell.value)

