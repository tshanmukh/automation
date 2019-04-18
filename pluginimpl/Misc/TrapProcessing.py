__author__ = 'shanmukh'
__status__ = 'Prototype'

# Script to pick specific problem and corresponding classification in normal switch cases

from lxml import etree

profileXml='/home/sthummala/frx.xml'
parser = etree.XMLParser(strip_cdata=False)
root = etree.parse(profileXml, parser)

TrapGroup=root.findall("trap")

# TrapId=TrapGroup.find("trap")
SpecificProblem=None
Classification=None
SpecificProblemDict={}
ClassificationDict={}
for a in TrapGroup:
    if a.get("id") == "trapObjectMode":
        for b in a.iter("switch"):
            if b.get("id") == "specificProblem":
                SpecificProblem=b.findall("case")
            elif b.get("id") == "classification":
                Classification=b.findall("case")

        if SpecificProblem is not None:
            for i in SpecificProblem:
                temp={i.get("input"):i.get("output")}
                SpecificProblemDict.update(temp)
        if Classification is not None:
            for i in Classification:
                temp={i.get("input"):i.get("output")}
                ClassificationDict.update(temp)

for specific in SpecificProblemDict.keys():
    if ClassificationDict.get(specific):
        print(SpecificProblemDict.get(specific),",",ClassificationDict.get(specific))
    else:
        print(SpecificProblemDict.get(specific),",","OTHER_SYMPTOM")
