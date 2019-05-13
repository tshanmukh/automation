__author__ = 'shanmukh'
__status__ = 'Development'

from lxml import etree
import utils

class profilexml():
    def __init__(self,profilexml,repopath):
        self.profilexml = profilexml
        self.repopath = repopath
        self.profile = self.repopath + 'centina/sa/profiles/' + self.profilexml + '.xml'
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
                pmtemplate = self.repopath + "centina/sa/profiles/" + a.get("path")
                # print("Found pm template ", pmtemplate)
                self.pmtemplatepaths.append(pmtemplate)

            # loading the pmfilepaths
            elif a.get("path").startswith("pm/"):
                # todo save all the other paths
                if not a.get("path").endswith(".dtd"):
                    self.pmfilepaths.append(self.repopath + "centina/sa/profiles/"+a.get("path"))

            # loading inventory paths
            elif a.get("path").startswith("snmp/inventory/"):
                if not a.get("path").endswith(".dtd"):
                    self.inventoryfilepaths.append(a.get("path"))

            # loading trap paths
            elif a.get("path").startswith("snmp/trap/"):
                if not a.get("path").endswith(".dtd"):
                    self.trapfilepaths.append(a.get("path"))

    def checkmetricgroupids(self,id):
        found = set()
        founddict = {}
        if self.pmfilepaths:
            for i in self.pmfilepaths:
                filePath = self.repopath + "centina/sa/profiles/" + i
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
    repopath = utils.getrepopath()
