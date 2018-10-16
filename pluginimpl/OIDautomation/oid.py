from typing import List, Any, Union

__author__ = 'Shanmukh'

import sys
from array import *
import xml.dom.minidom
from lxml import etree


# Function to generate the OID
def get_oid(doc, col):
    """
    :param col: colomn which requires the oid
    :param doc: The mib repository object
    :return result: returns all possible oid's of col
    """
    result=[]  # type: List[Union[str, Any]]
    entry = doc.getElementsByTagName("entry")
    for id in entry:
        arg = ''

        if id.getAttribute("name") == col:
            # print("suffix: ", id.getAttribute("id"), "colomn: ", id.getAttribute("name"), "\n")
            suffix=id.getAttribute("id")
            ancestors = []
            value = id.getAttribute("id")
            ancestors.append(int(value))
            parent = id.parentNode
            while parent != None:
                try:
                    id = parent.getAttribute("id")
                except:
                    pass
                try:
                    ancestors.append(int(id))
                except:
                    pass
                parent = parent.parentNode
            OID = ancestors[::-1]

            for i in OID:
                arg = arg + "."
                arg = arg + str(i)
            result.append(arg)

    if len(result) != 0:
        try:
            print (suffix)
            return result
        except:
            print('No match for ',col)
    else:
        print("Didn't find a match for \"", col, "\"")


# Global Initializations
result = []
path='/home/sthummala/workspace/vsure/centina/sa/profiles/'

# prompts and stores mib-repo name
# mib_repository = input('Enter the mib-repository name: ')

# @todo get the mib-repository name from the user
# Parsing using dom
doc = xml.dom.minidom.parse("eltek-mib-repository.xml")

# searchString = input()

oid = get_oid(doc, 'alarmUserConfigurable8Trap')

print("OID: ", oid)

profileXml='/home/sthummala/workspace/vsure/centina/sa/profiles/eltek.xml'
parser = etree.XMLParser(strip_cdata=False)
root = etree.parse(profileXml, parser)

dependency=root.find('dependencies')

for i in dependency.findall('file'):
    temp=i.get('path')
    if 'snmp/inventory/' in temp:
        if '.dtd' not in temp and 'if-mib' not in temp and 'pm/templates/' not in temp:
            parser=etree.XMLParser(strip_cdata=False)
            inventoryFile=etree.parse(path+temp,parser)
            table=inventoryFile.findall('table')
            for i in table:
                print (i.get('name'))
                print (get_oid(doc, i.get('name')))
            # print (temp)
    if 'pm' in temp:
        if '.dtd' not in temp and 'if-mib' not in temp and 'pm/templates/' not in temp:
            pmRoot = etree.parse(path+temp, parser)
            for mg in pmRoot.iter('metricGroup'):
                for met in mg.findall('parameter'):
                    met.attrib['oid']=get_oid(doc, met.get('name'))

                    print (met.get('oid') )




