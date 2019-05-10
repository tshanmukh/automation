import os
import xml.etree.ElementTree as ET
import re



class metricCreation():
    """Takes the metric elements and returns a metric in xml format"""

    def __init__(self,metricgroupid,metricgroupname,metricid,metricname,description,metricunits,Type,location,direction,parametername,oid,oidsuffix):
        self.metricgroupid = metricgroupid
        self.metricgroupname = metricgroupname
        self.metricid = "s100-pm-interfaces."+metricid+" Ne Rx".replace(' ','#')
        self.metricname = ("S100 Near End Rx "+metricname).replace(' ','#')
        self.description = description.replace(' ','#')
        self.metricunits = metricunits.replace(' ','#')
        self.Type = Type
        self.location = location
        self.direction = direction
        self.parametername = parametername.replace(' ','#')
        self.oid = oid
        self.oidsuffix = oidsuffix
        self.montype_result()
        self.formatmetric()

    def montype_result(self):
        """This function generates an xml with one metricgroup for every montype.
        Each metricgroup contains a metric with all the 9 combinations of direction(Rx,Tx,NA) and location(NE,FE,NA)
        If any of the columns(metric, units and Type) is empty, montype is used in the associated the pm fields."""

        # la,la_1 for location and da,da_1 for direction


        root = ET.Element("metricGroup", id=self.metricgroupid, name=self.metricgroupname, protocol="SNMP",displayType="Normal")
        doc = ET.SubElement(root, "metric",
                            ___aid=self.metricid,
                            ___bname= self.metricname,
                            ___cdesc=self.description,
                            ___dprotocol="SNMP",
                            ___eunits=self.metricunits,
                            ___fconversion_function="NONE" if (self.Type.lower() == 'gauge') else "PER_PERIOD",
                            ___gconsolidation_function="AVG" if (self.Type.lower() == 'gauge') else "SUM",
                            ___hlocation=self.location,
                            ___idirection=self.direction,

                            ___jdisplayType="lineSeries-hist" if (
                                    (self.Type == 'gauge') or (self.Type == 'GAUGE')) else "verticalBar-hist",
                            ___kdisplayColor="BLUE" if ( self.direction == 'TRANSMIT') else "DARK_GREEN")

        ET.SubElement(doc, "parameter", ___aname=self.parametername,
                      ___bcollector="SNMP",
                      ___ctype='COUNTER' if ((self.Type == 'counter') or (self.Type == 'COUNTER') or (self.Type == 'Counter')) else 'GAUGE' if (
                              (self.Type == 'gauge') or (self.Type == 'GAUGE') or (
                              self.Type == 'Gauge')) else 'COUNTER',
                      ___doid=self.oid, ___eoidSuffix = self.oidsuffix)

        ET.SubElement(doc, "value", parameter=self.parametername)
        tree = ET.ElementTree(root)

        tree.write("abc.xml")

    def _modifier(self, element):
        a = re.sub('^___[a-z]', '', element)
        return a

    def modify(self,element):
        return element.replace(' ','#')

    def formatmetric(self):
        f = open('abc.xml')
        data = f.readlines()
        lines = data[0].replace('><','>\n<').split('\n')
        # print(lines)
        line2 = list(map(self._modifier, lines[1].split(' ')))  #stores the metric tag by removing the ___[a-z]
        line3 = list(map(self._modifier, lines[2].split(' ')))  #stores the parameter line by removing the ___[a-z]
        # print(len(line2))

        print('{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t\n\t\t{}\n\t\t{}\n\t{} {} {} {} {} {}{}\n\t{}\n{}'\
              .format(line2[0],line2[1].replace('#',' '),line2[2].replace('#',' '),line2[3].replace('#',' '),line2[4],line2[5],line2[6],line2[7],line2[8],line2[9],line2[10],line2[11],line3[0],line3[1],line3[2],line3[3],line3[4],line3[5],line3[6],lines[3],lines[4]))


if __name__ == "__main__":
    metric = metricCreation(metricgroupid="s100-pm-eqpt.s100 pm eqpt port stats", metricgroupname="s100 pm eqpt port NE NA stats",metricid="s100-pm-eqpt.laserBiasCurrent#NE#NA", metricname="S100 Near End NA Laser Current" , description="FEC Uncorrected Code words" , metricunits="Amp" , direction="NA" , location="NEAR_END" , parametername="laserBiasCurrent", oid=".1.3.6.1.4.1.211.1.24.11.2.1.1.41.1.13.1.7", Type="GUAGE",oidsuffix='1.3.6')
