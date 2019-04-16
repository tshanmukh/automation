import os
import xml.etree.ElementTree as ET
from typing import List


class xmlparsing():
    """This class does the job of creating metrics in an xml and formating making it to human readable"""

    def __init__(self):
        # self.path = "/home/rupesh/TL1/pm/"
        # self.xmlname = "pm" + "_tl1_montype.xml"
        self.path=input("Enter the directory in which you want to generate the pm xml\nFor example: /home/rupesh/TL1/pm/\n")
        self.xmlname=input("Enter the name of the xml you want to create\nFor example: pm_tl1_2_montypes.xml\n")



    def montype_result(self, montype, metric, units, Type):
        """This function generates an xml with one metricgroup for every montype.
        Each metricgroup contains a metric with all the 9 combinations of direction(Rx,Tx,NA) and location(NE,FE,NA)"""



        # la,la_1 for location and da,da_1 for direction
        la = ["NE", "FE", "NA"]
        la_1 = ["NEAR_END", "FAR_END", "NA"]
        da = ["Tx", "Rx", "NA"]
        da_1 = ["TRANSMIT", "RECEIVE", "NA"]

        root = ET.Element("metricGroup", id=montype+" Statistics.TL1", name=montype+" Statistics TL1", protocol="TL1",displayType="Normal")


        for i in range(3):
            for j in range(3):

                doc = ET.SubElement(root, "metric",
                            id=montype + "." + la[i] + " " + da[j],
                            name= montype + " " + la[i] + " " + da[j],
                            desc=metric,
                            protocol="TL1",
                            units=' ' if units is None else units,
                            conversion_function="PER_PERIOD" if ((Type == 'counter') or (Type == 'COUNTER') or (Type == 'Counter') or (Type == 'Counter')) else "NONE",
                            consolidation_function="SUM" if ((Type == 'counter') or (Type == 'COUNTER') or (Type == 'Counter') or (Type == 'Counter')) else "AVG",
                            location=la_1[i],
                            direction=da_1[j],
                            min="0",
                            displayType="lineSeries-hist" if (
                                    (Type == 'gauge') or (Type == 'GAUGE')) else "verticalBar-hist",
                            displayColor="BLUE")

                ET.SubElement(doc, "parameter", name=montype,
                      collector="TL1",
                      Par_Type='COUNTER' if ((Type == 'counter') or (Type == 'COUNTER') or (Type == 'Counter')) else 'GAUGE' if (
                              (Type == 'gauge') or (Type == 'GAUGE') or (
                              Type == 'Gauge')) else 'NA',
                      oid=montype)

                ET.SubElement(doc, "value", parameter=montype)

        tree = ET.ElementTree(root)

        print(montype, type(Type))
        cwd = os.getcwd()
        os.chdir(self.path)
        tree.write(self.xmlname)
        os.chdir(cwd)



    def format_xml(self):
        """This function will format the  generated xml into human readable"""
        print(os.getcwd())
        os.chdir(self.path)
        with open(self.xmlname) as f:
            filedata = f.read()
        filedata = filedata.replace('</metric>', '\n\t</metric>')
        filedata = filedata.replace('consolidation_function', '\n\t\tconsolidation-function')
        filedata = filedata.replace('conversion_function', '\n\t\tconversion-function')
        filedata = filedata.replace("desc=\"", "\n\t\tdesc=\"")

        filedata = filedata.replace("direction=\"", "\n\t\tdirection=\"")

        filedata = filedata.replace("displayColor", "\n\t\tdisplayColor")

        filedata = filedata.replace("\" displayType=\"", "\"\n\t\tdisplayType=\"")
        filedata = filedata.replace("hist\" id=\"", "hist\" \n\t\tid=\"")
        filedata = filedata.replace("location=\"", "\n\t\tlocation=\"")
        filedata = filedata.replace("\" min=\"0\" ", "\"\n\t\tmin=\"0\"\n\t\t")
        filedata = filedata.replace("protocol=\"TL1\" units=\"", "\n\t\tprotocol=\"TL1\" \n\t\tunits=\"")
        filedata = filedata.replace("<parameter", "\n\n\t\t <parameter")
        filedata = filedata.replace("><", ">\n\t<")
        filedata = filedata.replace("<metricGroup", "\t<metricGroup")

        filedata = filedata.replace("<value parameter", "\t <value parameter")
        filedata = filedata.replace("<metric", "\t<metric")
        filedata = filedata.replace("\t\t<metric", "\t<metric")
        filedata = filedata.replace("</metricGroup", "\t</metricGroup")
        filedata = filedata.replace("\t<metricGroup", "  <metricGroup")
        filedata = filedata.replace("\t</metricGroup", "  </metricGroup")
        filedata = filedata.replace("\t  </metricGroup>", "  </metricGroup>")
        filedata = filedata.replace(">\n\n\t\t <", "\n\t >\n\n\t\t <")
        filedata = filedata.replace("Par_Type","type")

        filedata = filedata.replace("<metricGroup", "\n\n<metricGroup")
        # NA is renamed as No in sheet to overcome exception.
        #
        #
        # Hence it has to be renamed after processing the data.
        #
        # Below line to to do the same
        filedata = filedata.replace(" No\"", " NA\"")

        with open(self.xmlname, 'w') as f:
            f.write(filedata)




xml = xmlparsing()

xml.montype_result("CVL","description","packets","gauge")
xml.format_xml()
