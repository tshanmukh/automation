"""code to print all the montype and units pairs"""

from profilexml import profilexml
import utils
from pmfiles import pmfiles
repopath = utils.getrepopath()
profile = profilexml("fujitsu-flashwave-9500",repopath)

performance = pmfiles(profile.pmfilepaths) # initializing pmfiles class
pmfilenames = performance.filenames # storing file names
rootelement = performance.getrootelement(pmfilenames[0]) # passing in the file fujitsu-flashwave-metrics

data = performance.getdatafromfile(rootelement)
for value in data:
    print(value[2].get("oid"),value[1].get("units"))