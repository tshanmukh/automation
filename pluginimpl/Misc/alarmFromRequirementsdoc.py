__author__ = 'shanmukh'
__status__ = 'Prototype'

import xlrd
import re
from collections import OrderedDict
import json
from enum import Enum

""" Lists the specificProblems in the requirements doc"""


class alarmFromRequirementsdoc():
    def __init__(self,workbookname):
        try:
            self.workbook = xlrd.open_workbook(workbookname)
        except:
            print("Unable to open excell")

    def readalarmsheet(self,sheetname):

        if self.workbook is not None:
            # sheet = workbook.sheet_by_name("Alarms with classification-raw")
            sheet = self.workbook.sheet_by_name(sheetname)
            header = sheet.row_values(1)
            specific = header.index("Specific Problem")
            sever = header.index("Severity")
            classific = header.index("Classification")
            self.specificproblem = sheet.col_values(specific)
            self.classification = sheet.col_values(classific)
            self.severity = sheet.col_values(sever)

    def formclassificationdict(self):
        alarmDict = OrderedDict()
        for _alarm, _class in zip(self.specificproblem[1::],self.classification[1::]):
            _alarm = re.sub("\<.*", " ", _alarm)
            _alarm = re.sub(",.*", " ", _alarm)
            _alarm = re.sub("\..*", " ", _alarm)
            _alarm = re.sub("\(.*", "", _alarm).strip()
            _class = re.sub("\(.*", "", _class).strip()
            if _class in classificationEnum.__members__:
                alarmDict[_alarm.replace(' ','')] = _class
            else:
                print("Classification enum error",_class)
        return alarmDict
            # for alarm, value in alarmDict.items():
            #     # print('<entry tl1="{}"  model="{}"/>'.format(alarm,value))
            #     print('1-3-E1,100GE:MJ,{},SA,01-02,01-47-25,NEND,RCV:\\"Dummy generated alm responses\\"'.format(alarm,value))

    def formseveritydict(self):
        alarmDict = OrderedDict()
        for _alarm, _class in zip(self.specificproblem[1::], self.severity[1::]):
            _alarm = re.sub("\<.*", " ", _alarm)
            _alarm = re.sub(",.*", " ", _alarm)
            _alarm = re.sub("\..*", " ", _alarm)
            _alarm = re.sub("\(.*", "", _alarm).strip()
            _class = re.sub("\(.*", "", _class).strip()

            alarmDict[_alarm.replace(' ', '')] = _class

        return alarmDict


# Enums for classification
class classificationEnum(Enum):
    NODE_FAILURE = 100
    REACHABILITY_FAILURE = 200
    CARD_FAILURE = 300
    PORT_FAILURE = 350
    EQUIPMENT_FAILURE = 400
    INTERFACE_FAILURE = 500
    LAYER_1_FAILURE = 600
    LAYER_2_FAILURE = 700
    LAYER_3_FAILURE = 800
    APPLICATION_FAILURE = 900
    ABNORMAL_PERFORMANCE = 1000
    OTHER_FAILURE = 2000
    OTHER_SYMPTOM = 2100
    INFORMATION = 2150
    INDETERMINATE = 2200

if __name__ == "__main__":
    sheet = alarmFromRequirementsdoc("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-1finity-S100-reference.xlsx")
    sheet.readalarmsheet("Alarming S100")
    classification = sheet.formclassificationdict()
    for i,j in classification.items():
        print('<case input="{}" output="{}" />'.format(i,j))
    severity = sheet.formseveritydict()
