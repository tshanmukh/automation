__author__ = 'Shanmukh'

import sys
from array import *
import xml.dom.minidom


# Function to generate the OID
def get_oid(doc, col):
    """
    :param col: colomn which requires the oid
    :param doc: The mib repository object
    :return result: returns all possible oid's of col
    """
    entry = doc.getElementsByTagName("entry")
    for id in entry:
        arg = ''

        if id.getAttribute("name") == col:
            print("suffix: ", id.getAttribute("id"), "colomn: ", id.getAttribute("name"), "\n")
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
        return result
    else:
        print("Didn't find a match for \"", col, "\"")


# Global Initializations
oid = []
result = []

# prompts and stores mib-repo name
mib_repository = input('Enter the mib-repository name: ')

# @todo get the mib-repository name from the user
# Parsing using dom
doc = xml.dom.minidom.parse("eltek-mib-repository.xml")

searchString = input()
oid = get_oid(doc, searchString)

print("OID: ", oid)

