import pandas as pd
import re
import json

def removeextracharecters(value):
    value = re.sub('\n.*', '',value)
    value = re.sub('<.*', '',value)
    value = re.sub('\(.*', '',value)
    value = re.sub(',.*', '',value)
    return value

sheet = pd.ExcelFile("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
alarms = pd.read_excel(sheet,'Alarms with classification-raw',usecols=['TL1 Condition/ (SNMP Condition)','Classification'])
# print( removeextracharecters(alarms['TL1 Condition/ (SNMP Condition)'][2]) )
alarmsdict = { removeextracharecters(s): [] for s in alarms['TL1 Condition/ (SNMP Condition)']}
# print(json.dumps(alarmsdict))
for i in alarms.index:
    matchword = removeextracharecters(alarms['TL1 Condition/ (SNMP Condition)'][i])
    if removeextracharecters(alarms['Classification'][i]) not in alarmsdict[matchword]:
        alarmsdict[matchword].append(removeextracharecters(alarms['Classification'][i]))

for i,j in alarmsdict.items():
     print('<entry tl1="{}" model="{}"/>'.format(i.strip(),*j))

 