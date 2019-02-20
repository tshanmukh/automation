__author__ = 'Shanmukh'

import sys
from array import *
import xml.dom.minidom
from lxml import etree


class oid:

    def get_oid(self, doc, col):
        """
        :param col: colomn which requires the oid
        :param doc: The mib repository object
        :return result: returns all possible oid's of col
        """
        doc = xml.dom.minidom.parse(doc)
        result = []
        entry = doc.getElementsByTagName("entry")
        suffix = ''
        for id in entry:
            arg = ''

            if id.getAttribute("name") == col:
                suffix = id.getAttribute("id")
                ancestors = []
                value = id.getAttribute("id")
                ancestors.append(int(value))
                parent = id.parentNode
                while parent is not None:
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
                # print(suffix)
                return result
            except:
                print('No match for ', col)
        else:
            # print("Didn't find a match for \"", col, "\"")
            return None


if __name__ == '__main__':
    # Global Initializations
    result = []
    path = '/home/sthummala/workspace/repo/centina/sa/profiles/'

    # prompts and stores mib-repo name
    mib_repository = input('Enter the mib-repository name: ')

    searchString = input('Enter the object name')
    obj = oid()

    oid = obj.get_oid("eltek-mib-repository.xml", str(searchString))

    print("OID: ", oid)
