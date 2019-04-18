__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd

""" Script to get values between sheets. Here using the sheet1 col0 and col1 to give values to col1 of sheet3"""


workbook=''
try:
    workbook = xlrd.open_workbook('/home/sthummala/Documents/nwtel/fault-details.xlsx')
except:
    print("Unable to open excell")

es={}

if workbook is not None:
    sheet=workbook.sheet_by_index(0)
    specific=sheet.col_values(0)
    classi=sheet.col_values(2)
    es=dict(zip(specific,classi))
    # print(es)

cds={}

if workbook is not None:
    sheet=workbook.sheet_by_index(2)
    specific=sheet.col_values(0)
    classi=sheet.col_values(2)
    cds=dict(zip(specific,classi))
    # print(cds)

for a in cds.keys():
    if es.get(a) is not None:
        print(a+","+es.get(a))
    else:
        print(a+","+cds.get(a))






