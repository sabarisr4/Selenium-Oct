#install excel - pip install openpyxl

import openpyxl

wb=openpyxl.Workbook() #Create workbook
sheet=wb.create_sheet() #Create sheet

#Another way
c1=sheet["A1"]
c1.value="name"
c2=sheet["B1"]
c2.value="gender"
c3=sheet["C1"]
c3.value="age"


c4=sheet["A2"]
c4.value="sabari"
c5=sheet["B2"]
c5.value="male"
c6=sheet["C2"]
c6.value="30"


wb.save("Example.xlsx")