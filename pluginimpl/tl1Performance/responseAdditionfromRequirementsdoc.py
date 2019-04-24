__author__ = 'Shanmukh'
__status__ = 'Development'

from metricsFromRequirementsdoc import parseexcel
import re
import numpy as np
from endpoints import getcsv

def formresponse(rows,sourcename,f):
    if rows[1] == "NEAR_END":
        direction = "NEND"
    elif rows[1] == "FAR_END":
        direction = "FEND"
    elif rows[1].lower() == "nend":
        direction = "NEND"
    elif rows[1].lower() == "fend":
        direction = "FEND"
    else:
        direction = "NA"

    if rows[2] == "RECEIVE":
        location = "RCV"
    elif rows[2] == "TRANSMIT":
        location = "TRMT"
    elif rows[2].lower() == "tx":
        location = "TRMT"
    elif rows[2].lower() == "rx":
        location = "RCV"
    else:
        location = "NA"

    Timeperiod = "15-MIN"

    value = str(np.random.random_integers(0,100))
    print(sourcename+":"+rows[0]+","+value+","+"TRUE,"+direction+","+location+","+Timeperiod+",01-22,02-00,1")
    f.write(sourcename+":"+rows[0]+","+value+","+"TRUE,"+direction+","+location+","+Timeperiod+",01-22,02-00,1\n")

sheet = parseexcel("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
print(len(sheet.pmsheets))

sourceId = getcsv()
print(sourceId)

for i in sheet.pmsheets:
    sheet.getmontypedetails(i,['Montype', 'Direction', 'Location', 'Binned', 'Nonbinned', '', 'Model', 'Enable', 'Metric', 'Units', 'Type', '', 'Verification Date', 'History PM', 'Live PM', '', 'Verification Date', 'History PM', 'Live PM'])
    record = sheet.sheetmontypedict
    del record['Montype']
    del record['']
    print(i)
    f = open("response/RTRV-PM-"+i+"-NULL.txt",'w')
    for j in record.keys():
        # print([j,record[j][3],record[j][4]])
        try:
            formresponse([j,record[j][3],record[j][4]], sourceId[i],f)
        except:
            print("No source type: ",i)
    f.close()