import xlrd
import metricCreation
# from Misc.conversion import stringtoDecimal

def stringtoDecimal(value):
    oid = [str(ord(i)) for i in value]
    return str(len(oid))+'.'+'.'.join(oid)

def getrows():
    workbook = xlrd.open_workbook('metric.xlsx')
    sheet = workbook.sheet_by_index(6)  #change the sheet number accordingly

    value = [ sheet.row_values(i) for i in range(sheet.nrows)]
    print(value)

    return value

a = getrows()
# print(list(a))
for i in a[1::]:
    i[-1] = stringtoDecimal(i[-1])+".1.1.0.0"
    a=metricCreation.metricCreation(*i)