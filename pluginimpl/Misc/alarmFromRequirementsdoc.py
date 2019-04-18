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
    # worksheet = xlrd.open_workbook('alarms.xlsx')
    workbook = xlrd.open_workbook('/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx')
except:
    print("Unable to open excell")

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

if workbook is not None:
    # sheet = worksheet.sheet_by_name("Alarms with classification-raw")
    sheet = workbook.sheet_by_name("Alarming-NEW")
    # sheet = worksheet.sheet_by_index(0)
    specific = sheet.col_values(1)
    classification = sheet.col_values(3)

    alarmDict = OrderedDict()
    for _alarm, _class in zip(specific[1::],classification[1::]):
        _alarm = re.sub("\<.*", " ", _alarm)
        _alarm = re.sub(",.*", " ", _alarm)
        _alarm = re.sub("\..*", " ", _alarm)
        _alarm = re.sub("\(.*", "", _alarm).strip()
        _class = re.sub("\(.*", "", _class).strip()
        if _class in classificationEnum.__members__:
            alarmDict[_alarm.replace(' ','')] = _class
        else:
            print("Classification enum error",_class)
    for alarm, value in alarmDict.items():
        # print('<entry tl1="{}"  model="{}"/>'.format(alarm,value))
        print('1-3-E1,100GE:MJ,{},SA,01-02,01-47-25,NEND,RCV:\\"Dummy generated alm responses\\"'.format(alarm,value))


