__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd
from collections import OrderedDict
import json

""" Lists the specificProblems in the requirements doc"""

class parseexcel():

    def __init__(self, workbookpath):
        self.worksheet= ''
        self.workbookpath=workbookpath
        self.montypedict = OrderedDict()
        try:
            self.worksheet = xlrd.open_workbook(self.workbookpath)
        except:
            print("Unable to open excell")

    def getmontypedetails(self,sheetname):
        if self.worksheet is not None:
            # sheet = worksheet.sheet_by_name("Alarms with classification-raw")
            self.sheetname = sheetname
            sheet = self.worksheet.sheet_by_name(self.sheetname)
            # sheet = worksheet.sheet_by_index(0)
            montype = sheet.col_values(0)
            direction = sheet.col_values(1)
            location = sheet.col_values(2)
            metric = sheet.col_values(8)
            units = sheet.col_values(9)
            metrictype = sheet.col_values(10)



        for i in zip(montype,metric,units,metrictype):
            self.montypedict[i[0]] = (i[1],i[2],i[3])

        return self.montypedict

    def printmontypedetails(self):
        print(json.dumps(self.montypedict))



