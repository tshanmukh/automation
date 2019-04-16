__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd
import re
from collections import OrderedDict
import json
from enum import Enum

""" Lists the specificProblems in the requirements doc"""


workbook=''
try:
    # workbook = xlrd.open_workbook('alarms.xlsx')
    workbook = xlrd.open_workbook('/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx')
except:
    print("Unable to open excell")


if workbook is not None:
    # sheet = workbook.sheet_by_name("Alarms with classification-raw")
    sheet = workbook.sheet_by_name("1GE")
    # sheet = workbook.sheet_by_index(0)
    montype = sheet.col_values(0)
    direction = sheet.col_values(1)
    location = sheet.col_values(2)
    metric = sheet.col_values(8)
    units = sheet.col_values(9)
    metrictype = sheet.col_values(10)

montypedict = OrderedDict()

for i in zip(montype,metric,units,metrictype):
    montypedict[i[0]] = (i[1],i[2],i[3])

print(json.dumps(montypedict))