import os
import xml.etree.ElementTree as ET



class metricCreation():
    def __init__(self):
        pass

    def montype_result(self, montype, metric, units, Type,location,direction):
        """This function generates an xml with one metricgroup for every montype.
        Each metricgroup contains a metric with all the 9 combinations of direction(Rx,Tx,NA) and location(NE,FE,NA)
        If any of the columns(metric, units and Type) is empty, montype is used in the associated the pm fields."""

        # la,la_1 for location and da,da_1 for direction


        root = ET.Element("metricGroup", id=montype+" Statistics.TL1", name=montype+" Statistics TL1", protocol="TL1",displayType="Normal")
        doc = ET.SubElement(root, "metric",
                            ___aid=montype,
                            ___bname= montype,
                            ___cdesc=montype,
                            ___dprotocol="TL1",
                            ___eunits=montype,
                            ___fconversion_function="NONE" if (Type == 'gauge' or 'GAUGE') else "PER_PERIOD",
                            ___gconsolidation_function="AVG" if (Type == 'gauge' or 'GAUGE') else "SUM",
                            ___hlocation=location,
                            ___idirection=direction,

                            ___jdisplayType="lineSeries-hist" if (
                                    (Type == 'gauge') or (Type == 'GAUGE')) else "verticalBar-hist",
                            ___kdisplayColor="BLUE" if ( 'Tx'== 'Tx') else "DARK_GREEN")

        ET.SubElement(doc, "parameter", ___aname=montype,
                      ___bcollector="TL1",
                      ___cPar_Type='COUNTER' if ((Type == 'counter') or (Type == 'COUNTER') or (Type == 'Counter')) else 'GAUGE' if (
                              (Type == 'gauge') or (Type == 'GAUGE') or (
                              Type == 'Gauge')) else 'COUNTER',
                      ___doid=montype)

        ET.SubElement(doc, "value", parameter=montype)
        tree = ET.ElementTree(root)

        tree.write(montype+".xml")

    def formatmetric(self):
        f = open('abc.xml')
        data = f.readlines()
        lines = data[0].replace('><','>\n<').split('\n')
        print(len(lines))
        line2 = lines[1].split(' ')
        line3 = lines[2].split(' ')
        # print(line1,'\n',line2,'','\n',line3,'\n',line4,'\n',line5)
        print('{}\n\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t{}\n\t{}\n\t{}\n{}'\
              .format(lines[0],line2[0],line2[1].replace('___a',''),line2[2].replace('___b',''),line2[3].replace('___c',''),line2[4].replace('___d',''),line2[5].replace('___e',''),line2[6].replace('___f',''),line2[7].replace('___g',''),line2[8].replace('___h',''),line2[9].replace('___i',''),line2[10].replace('___j',''),lines[2],lines[3],lines[4],lines[5]))




if __name__ == "__main__":
    metric = metricCreation()
    metric.montype_result("abc",  "def", "ghi", "jkl","mno","pqr")
    metric.formatmetric()
