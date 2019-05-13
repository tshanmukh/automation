import glob
import pickle
import os
from profilexml import profilexml

pmFiles = []
metricGroupId = []
# pickling the repo
repopath = None
if os.path.isfile("../.repopath.pickle"):
    infile = open("../.repopath.pickle", 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    repopath = new_dict.get("repository")
    print("Repository path saved is {}".format(repopath))
else:
    repopath = input("Enter the path to the repository: ")
    variable = {"repository": repopath}
    f = open("../.repopath.pickle", 'wb')
    pickle.dump(variable, f)
    f.close()

files = glob.glob(repopath + "centina/sa/profiles/*.xml")
xmls = [f.split('/')[-1].replace('.xml', '') for f in files]

# for pluginName in xmls:
# pluginName = input("Please enter the plugin name: ")
pluginName = 'opterna-am-omni2000'
# plugin = pluginName.split('/')[-1].replace('.xml','')
profile = profilexml(pluginName,repopath)

# print(profile.pmtemplatepaths)
# print(" the metric groupid's are {}".format(profile.parsetemplates(profile.pmtemplatepaths[0])))
# print(profile.pmtemplatepaths[0],profile.parsetemplates(profile.pmtemplatepaths[0]))
show = True
for i in profile.pmtemplatepaths:

    metricgroupids = profile.parsetemplates(i)
    found, founddict = profile.checkmetricgroupids(metricgroupids)

    if bool(set(metricgroupids) - found):
        if show:
            print("---------------------------------------------------------------------------------------------")
            print("plugin: " + pluginName + "--" + profile.protocol)
            print("---------------------------------------------------------------------------------------------")
            show = False
        print("Template: " + str(i.split('/')[-1]) + " Missing id's " + str(set(metricgroupids) - found))