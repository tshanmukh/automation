__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd
import re
from collections import OrderedDict
import json
import pickle
import os

""" Lists the specificProblems in the requirements doc"""

class parseexcel():
    def __int__(self,workbookpath,sheetname):
        self.workbook=''
        self.workbookpath=workbookpath
        self.sheetname=sheetname
        self.montypedict = OrderedDict()
        try:
            workbook = xlrd.open_workbook(self.workbookpath)
        except:
            print("Unable to open excell")

    def getmontypedetails(self,sheetname):
        if self.workbook is not None:
            # sheet = workbook.sheet_by_name("Alarms with classification-raw")
            sheet = self.workbook.sheet_by_name(sheetname)
            # sheet = workbook.sheet_by_index(0)
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
        print(self.montypedict)

