import os
import xml.etree.ElementTree as ET



class metricCreation():
    def __init__(self):
        pass

    def montype_result(self, metricgroupid,metricgroupname,metricid,metricname,description,metricunits,Type,location,direction,parametername,oid):
        """This function generates an xml with one metricgroup for every montype.
        Each metricgroup contains a metric with all the 9 combinations of direction(Rx,Tx,NA) and location(NE,FE,NA)
        If any of the columns(metric, units and Type) is empty, montype is used in the associated the pm fields."""

        # la,la_1 for location and da,da_1 for direction


        root = ET.Element("metricGroup", id=metricgroupid, name=metricgroupname, protocol="SNMP",displayType="Normal")
        doc = ET.SubElement(root, "metric",
                            ___aid=metricid,
                            ___bname= metricname,
                            ___cdesc=description,
                            ___dprotocol="SNMP",
                            ___eunits=metricunits,
                            ___fconversion_function="NONE" if (Type == 'gauge' or 'GAUGE') else "PER_PERIOD",
                            ___gconsolidation_function="AVG" if (Type == 'gauge' or 'GAUGE') else "SUM",
                            ___hlocation=location,
                            ___idirection=direction,

                            ___jdisplayType="lineSeries-hist" if (
                                    (Type == 'gauge') or (Type == 'GAUGE')) else "verticalBar-hist",
                            ___kdisplayColor="BLUE" if ( 'Tx'== 'Tx') else "DARK_GREEN")

        ET.SubElement(doc, "parameter", ___aname=parametername,
                      ___bcollector="SNMP",
                      ___ctype='COUNTER' if ((Type == 'counter') or (Type == 'COUNTER') or (Type == 'Counter')) else 'GAUGE' if (
                              (Type == 'gauge') or (Type == 'GAUGE') or (
                              Type == 'Gauge')) else 'COUNTER',
                      ___doid=oid)

        ET.SubElement(doc, "value", parameter=parametername)
        tree = ET.ElementTree(root)

        tree.write("abc.xml")

    def formatmetric(self):
        f = open('abc.xml')
        data = f.readlines()
        lines = data[0].replace('><','>\n<').split('\n')
        print(len(lines))
        line2 = lines[1].split(' ') #stores the metric tag
        line3 = lines[2].split(' ') #stores the parameter line
        print(line3[5])

        print('{}\n\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t{} {} {} {} {}{}\n\t{}\n\t{}\n{}'\
              .format(lines[0],line2[0],line2[1].replace('___a',''),line2[2].replace('___b',''),line2[3].replace('___c',''),line2[4].replace('___d',''),line2[5].replace('___e',''),line2[6].replace('___f',''),line2[7].replace('___g',''),line2[8].replace('___h',''),line2[9].replace('___i',''),line2[10].replace('___j',''),line3[0],line3[1].replace('___a',''),line3[2].replace('___b',''),line3[3].replace('___c',''),line3[4].replace('___d',''),line3[5],lines[3],lines[4],lines[5]))


if __name__ == "__main__":
    metric = metricCreation()
    metric.montype_result(metricgroupid="s100-pm-eqpt.s100 pm eqpt port stats", metricgroupname="s100 pm eqpt port NE NA stats",metricid="s100-pm-eqpt.laserBiasCurrent#NE#NA", metricname="S100#Near#End#NA#Laser#Current" , description="FEC#Uncorrected#Code#words" , metricunits="Amp" , direction="NA" , location="NEAR_END" , parametername="laserBiasCurrent", oid=".1.3.6.1.4.1.211.1.24.11.2.1.1.41.1.13.1.7", Type="GUAGE")
    metric.formatmetric()
