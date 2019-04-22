__author__ = 'shanmukh'
__status__ = 'Development'

import os
from lxml import etree
import pickle
import glob

class profilexml():
    def __init__(self,profilexml):
        self.profilexml = profilexml
        self.profile = repopath + 'centina/sa/profiles/' + pluginName + '.xml'
        parser = etree.XMLParser(strip_cdata=False)
        self.root = etree.parse(self.profile, parser)
        self.pmtemplatepaths = []
        self.pmfilepaths = []
        self.inventoryfilepaths = []
        self.trapfilepaths = []
        self.meta()
        self.dependenciespath()
        self.filenames()



    def meta(self):
        self.meta = self.root.find("meta")
        self.protocol = self.meta.find("protocol").get("name")

    def dependenciespath(self):
        self.dependencies = self.root.find("dependencies")

    def parsetemplates(self,pmtemplate):
        parsertemplate = etree.XMLParser(strip_cdata=False)
        template = etree.parse(pmtemplate, parsertemplate)
        perftemplate = template.find("perf-template")
        pmmetricgroups = perftemplate.find("pm-metric-groups")
        metricGroupId = []
        for i in pmmetricgroups.findall("value"):
            metricGroupId = metricGroupId + [i.text]
        return metricGroupId

    def filenames(self):
        self.filepaths = self.dependencies.findall("file")
        for a in self.filepaths:
            if a.get("path").startswith("pm/templates"):
                if a.get("path").endswith(".dtd"):
                    continue
                pmtemplate = repopath + "centina/sa/profiles/" + a.get("path")
                # print("Found pm template ", pmtemplate)
                self.pmtemplatepaths.append(pmtemplate)


            elif a.get("path").startswith("pm/"):
                # todo save all the other paths
                if not a.get("path").endswith(".dtd"):
                    self.pmfilepaths.append(a.get("path"))

            elif a.get("path").startswith("snmp/inventory/"):
                if not a.get("path").endswith(".dtd"):
                    self.inventoryfilepaths.append(a.get("path"))
            elif a.get("path").startswith("snmp/trap/"):
                if not a.get("path").endswith(".dtd"):
                    self.trapfilepaths.append(a.get("path"))

    def checkmetricgroupids(self,id):
        found = set()
        founddict = {}
        if self.pmfilepaths:
            for i in self.pmfilepaths:
                filePath = repopath + "centina/sa/profiles/" + i
                ref = i.split("/")
                reference = ref[1].replace(".xml", "")
                parser = etree.XMLParser(strip_cdata=False)
                pmfile = etree.parse(filePath, parser)

                for groupId in pmfile.iter("metricGroup"):
                    if groupId.get("id") in id:
                        found.add(groupId.get("id"))
                        founddict[groupId.get("id")] = groupId.get("name")


        else:
            print("No pm xml files present to parsing")
        return found, founddict


if __name__ == '__main__':
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
        f = open(".repopath.pickle", 'wb')
        pickle.dump(variable, f)
        f.close()

    files = glob.glob(repopath+"centina/sa/profiles/*.xml")
    xmls = [f.split('/')[-1].replace('.xml','') for f in files]

    # for pluginName in xmls:
        # pluginName = input("Please enter the plugin name: ")
    pluginName = 'opterna-am-omni2000'
        # plugin = pluginName.split('/')[-1].replace('.xml','')
    profile = profilexml(pluginName)

    # print(profile.pmtemplatepaths)
    # print(" the metric groupid's are {}".format(profile.parsetemplates(profile.pmtemplatepaths[0])))
    # print(profile.pmtemplatepaths[0],profile.parsetemplates(profile.pmtemplatepaths[0]))
    show = True
    for i in profile.pmtemplatepaths:

        metricgroupids = profile.parsetemplates(i)
        found,founddict = profile.checkmetricgroupids(metricgroupids)

        if bool(set(metricgroupids)-found):
            if show:
                print("---------------------------------------------------------------------------------------------")
                print("plugin: "+pluginName + "--"+profile.protocol)
                print("---------------------------------------------------------------------------------------------")
                show = False
            print("Template: "+str(i.split('/')[-1])+" Missing id's "+str(set(metricgroupids)-found))