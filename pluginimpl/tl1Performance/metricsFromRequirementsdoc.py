__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd
from collections import OrderedDict
import json
import logging
import re

""" Lists the specificProblems in the requirements doc"""

class parseexcel():

    def __init__(self, workbookpath):
        self.worksheet= ''
        self.workbookpath=workbookpath
        self.montypedict = OrderedDict()
        logging.basicConfig(filename='debug.log',
                            filemode='w',
                            format='%(asctime)s, %(levelname)s \t%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("something")
        try:
            self.worksheet = xlrd.open_workbook(self.workbookpath)
            self.sheetnames = self.worksheet.sheet_names()
            print(self.sheetnames)
        except:
            print("Unable to open excell")
        # self.getsheetnames()
        self.checksheet()


    def getmontypedetails(self,sheetname,rows):
        if self.worksheet is not None:
            sheetname = sheetname
            sheet = self.worksheet.sheet_by_name(sheetname)
            montype = sheet.col_values(rows.index("Montype"))
            try:
                metric = sheet.col_values(rows.index("Metric"))
            except:
                self.logger.warning('There is no metric column in the sheet {}'.format(sheetname))
                print("something")
            try:
                units = sheet.col_values(rows.index("Units"))
            except:
                self.logger.warning("There is no units tag in the sheet {}".format(sheetname))

            try:
                metrictype = sheet.col_values(rows.index("Type"))
            except:
                self.logger.warning("There is not metrictype tag in the sheet {}".format(sheetname))


        try:
            for i in zip(montype,metric,units,metrictype):
                if None in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                if "" in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                if " " in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                else:
                    temp = re.sub('<.*','',i[0])
                    self.montypedict[temp.strip()] = (i[1].strip(),i[2].strip(),i[3].strip())
        except:
            self.logger.info("For loop skipped")



    def getsheetnames(self):
        indexPerformance = self.sheetnames.index("Performance")
        print(indexPerformance)
        # self.sheetnames= self.sheetnames[indexPerformance+1::]
        # print(self.sheetnames)

    def checksheet(self):
        for i in self.sheetnames:
            sheet=self.worksheet.sheet_by_name(i)
            rows = sheet.row_values(1)
            if "Montype" in rows:
                value = self.getmontypedetails(i,rows)


    # def getmontypes(self):
    #     for i in self.sheetnames:
    #         self.getmontypedetails(i)
        try:
            del self.montypedict['Montype']
            del self.montypedict[""]
        except KeyError:
            print("Key error")
            raise

    def printmontypedetails(self):
        print(json.dumps(self.montypedict))

if __name__ == "__main__":
    sheet = parseexcel("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
    sheet.checksheet()
    sheet.printmontypedetails()

