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
        self.pmsheets = []
        try:
            self.worksheet = xlrd.open_workbook(self.workbookpath)
            self.sheetnames = self.worksheet.sheet_names()
            # print(self.sheetnames)
        except:
            print("Unable to open excell")
        # self.getsheetnames()
        self.checksheet()


    def getmontypedetails(self,sheetname,rows):
        """Gets all the details from a sheet"""

        self.sheetmontypedict = {} # variable used by response generation script to read in montypes per sheet

        if self.worksheet is not None:
            sheetname = sheetname
            sheet = self.worksheet.sheet_by_name(sheetname)
            montype = sheet.col_values(rows.index("Montype"))
            self.temp = montype

            try:
                metric = sheet.col_values(rows.index("Metric"))
            except ValueError:
                self.logger.warning('There is no metric column in the sheet {}'.format(sheetname))
                metric = ['' for i in sheet.col_values(rows.index("Montype"))]
            try:
                units = sheet.col_values(rows.index("Units"))
            except ValueError:
                self.logger.warning("There is no units tag in the sheet {}".format(sheetname))
                units = ['' for i in sheet.col_values(rows.index("Montype"))]

            try:
                metrictype = sheet.col_values(rows.index("Type"))
            except:
                self.logger.warning("There is not metrictype tag in the sheet {}".format(sheetname))
                metrictype = ['COUNTER' for i in sheet.col_values(rows.index("Montype"))]

            # Gets the loaction
            try:
                location = sheet.col_values(rows.index("Location"))
            except:
                self.logger.warning("There is not metrictype tag in the sheet {}".format(sheetname))
                location = [None for i in sheet.col_values(rows.index("Montype"))]

            # Gets the direction
            try:
                direction = sheet.col_values(rows.index("Direction"))
            except:
                self.logger.warning("There is not metrictype tag in the sheet {}".format(sheetname))
                direction = [None for i in sheet.col_values(rows.index("Montype"))]


            # try:
            for i in zip(montype,metric,units,metrictype,location,direction):
                if None in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                if "" in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                if " " in i:
                    self.logger.error("Null at {} in sheet {}".format(i,sheetname))
                else:
                    temp = re.sub('<.*','',i[0])
                    self.montypedict[temp.strip()] = (i[1].strip(),i[2].strip(),i[3].strip(),i[4].strip(),i[5].strip())

            #code to take in all the data from the sheet as per line numbers
            for j,i in enumerate(zip(montype, metric, units, metrictype, location, direction)):
                if "<k>" in i[0] and "<i>" in i[0]:  # creates the metrics in all possible values of k and i
                    for k in ['0','1','2','2E','3','FLEX']:
                        for I in range(1,7):
                            # print(sheetname,i[0].replace('<k>',k).replace('<i>',str(I)))
                            self.sheetmontypedict[j] = (i[0].replace('<k>', k).replace('<i>',str(I)).strip(), i[1].strip(), i[2].strip(), i[3].strip(), i[4].strip(),i[5].strip())
                elif "<k>" in i[0] and not "<i>" in i[0]:
                    for k in ['0', '1', '2', '2E', '3', 'FLEX']:
                        # print(sheetname, i[0].replace('<k>', k))
                        self.sheetmontypedict[j] = (i[0].replace('<k>', k).strip(), i[1].strip(), i[2].strip(), i[3].strip(), i[4].strip(), i[5].strip())
                else:
                    self.sheetmontypedict[j] = (i[0].strip(),i[1].strip(),i[2].strip(),i[3].strip(),i[4].strip(),i[5].strip())
            # except:
            #     raise

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
                self.pmsheets.append(i)


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
    # sheet.checksheet()
    # sheet.printmontypedetails()
    print(sheet.pmsheets)

