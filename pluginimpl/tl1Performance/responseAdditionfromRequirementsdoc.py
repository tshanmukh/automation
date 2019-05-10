__author__ = 'Shanmukh'
__status__ = 'Development'

from metricsFromRequirementsdoc import parseexcel
import re
import numpy as np
from endpoints import getcsv

def formresponse(rows,sourcename,f):
    """params:
        rows = ['Montype', location, dircetion]
        sourcename = sourceid from the endpoint
        f = file reference to which the output is to be returned

    """
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
    # print(sourcename+":"+rows[0]+","+value+","+"TRUE,"+direction+","+location+","+Timeperiod+",01-22,02-00,1")
    f.write(sourcename+":"+rows[0]+","+value+","+"TRUE,"+direction+","+location+","+Timeperiod+",01-22,02-00,1\n")

sheet = parseexcel("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-4100ES_v1-3.xlsx")
print(len(sheet.pmsheets))

sourceId = getcsv()  # funtion returns SourceType:SourceId dict read from endpoints.csv
print(sourceId)

for i in sheet.pmsheets:
    sheet.clearmontypedict() # function clears the previous sheets data from the dict
    sheet.getmontypedetails(i,['Montype', 'Direction', 'Location', 'Binned', 'Nonbinned', '', 'Model', 'Enable', 'Metric', 'Units', 'Type', '', 'Verification Date', 'History PM', 'Live PM', '', 'Verification Date', 'History PM', 'Live PM'])

    record = sheet.sheetmontypedict   # gets all the details like the montype direction from the sheet 'i' format is Number: (...values...)
    # print(i,record)
    try:
        f = open("response/RTRV-PM-"+i+"-"+sourceId[i]+".txt",'w')


        for k,j in record.items():
            if j[0] == 'Montype':
                continue
            elif len(j[0]) > 1:
                try:
                    formresponse([j[0],j[4],j[5]], sourceId[i],f)
                except:
                    print("No source type: ",i)
        f.close()
    except:
        print('error' + i)