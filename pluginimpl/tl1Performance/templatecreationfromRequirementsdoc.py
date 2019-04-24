__author__ = 'Shanmukh'
__status__ = 'Development'

from metricsFromRequirementsdoc import parseexcel
import re

sheet = parseexcel("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
print(len(sheet.pmsheets))
for i in sheet.pmsheets:
    f = open("templates/fujitsu-fw-9500-"+i+"-tl1.xml",'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE objects PUBLIC "pm/templates/pmTemplate.dtd" "pmTemplate.dtd">\n\n\n<objects version="UNCLEAN">\n\n  <perf-template name="fujitsu-fw-9500-{}-tl1">\n\n    <description>{} stats</description>\n\n    <templateType>PLUGIN</templateType>\n    <pm-metric-groups type="String">\n'.format(i,i))
    sheet.getmontypedetails(i,['Montype', 'Direction', 'Location', 'Binned', 'Nonbinned', '', 'Model', 'Enable', 'Metric', 'Units', 'Type', '', 'Verification Date', 'History PM', 'Live PM', '', 'Verification Date', 'History PM', 'Live PM'])
    print("-------------------------------------------------------------\n"+i+"\n----------------------------------------------------")
    for j in set(sheet.temp[2::]):
        if len(j) > 1:
            if not j.startswith('<'):
                f.write("\t\t<value>{} Statistics.TL1</value>\n".format(re.sub('<.*','',j)))
                print(j)
    f.write('</pm-metric-groups>\n\n    <pm-threshold-policies type="String">\n    </pm-threshold-policies>\n\n  </perf-template>\n\n</objects>')
    f.close()