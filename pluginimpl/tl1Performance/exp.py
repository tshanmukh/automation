"""Script to chech which sourcetypes are collection pm from db """

from metricsFromRequirementsdoc import parseexcel
from querydb import querydb

db = querydb(host="172.31.6.133",db='pm')
sourceid = db.getpmsourcetypes('MNRGKSXBOS1-RFW95005')

sheet = parseexcel("/home/sthummala/Downloads/Test sheet/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
pmsourcetypes = set(sheet.pmsheets)

diff = pmsourcetypes - sourceid

print(len(diff))
print(diff)