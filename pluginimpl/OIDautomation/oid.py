__author__ = 'Shanmukh'

import sys
from array import *
import xml.dom.minidom
from lxml import etree


class oid(object):

    def __init__(self,doc):
        self.doc = xml.dom.minidom.parse(doc)

    def get_oid(self, col):
        """
        :param col: colomn which requires the oid
        :param doc: The mib repository object
        :return result: returns all possible oid's of col
        """

        result = []
        entry = self.doc.getElementsByTagName("entry")
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

    searchString = True
    obj = oid(mib_repository)
    while searchString:
        searchString = input('Enter the object name: ')
        if searchString is '':
            continue

        try:
            oid = obj.get_oid(searchString)
            if oid is not None:
                print("OID: ", *oid)
            else:
                print("Entry not found")
        except:
            print("Exiting")
            searchString = False


