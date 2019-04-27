__author__='Rupesh'
__status__="Prototype"


import glob
import errno
import os
import xml.etree.ElementTree as ET
from typing import List
import metricsFromRequirementsdoc
import subprocess
import json

current_directory=os.getcwd()
results_directory= os.path.join(current_directory, "results/")


#Creating results folder in the location where this script is located. Removing the contents of results folder if it is already existing
# if self.path.isdir("results/"):
#     files=os.listdir("results/")
#     for file in files:
#         os.remove("results/"+file)
# else:
#     os.system("mkdir results")



class xmlparsing():
    """This class does the job of creating metrics in an xml and formating making it to human readable"""

    def __init__(self):
        self.path = os.getcwd()
        print(self.path)

        # Creating results folder in the location where this script is located. Removing the contents of results folder if it is already existing
        if os.path.isdir(self.path+"results/"):
            files = os.listdir("results/")
            for file in files:
                os.remove("results/" + file)
        else:
            os.system("mkdir results")

        # To have the results directory without changing the current directory
        self.results_directory=os.path.join(self.path, "results/")


        print(os.getcwd())
        print(os.path)

        # a=os.path.relpath('results/', start=os.curdir)




        # self.xmlname = "pm" + "_tl1_montype.xml"
        # self.path=input("Enter the directory in which you want to generate the pm xml\nFor example: /home/rupesh/TL1/pm/\n")
        # self.xmlname=input("Enter the name of the xml you want to create\nFor example: pm_tl1_2_montypes.xml\n")



    def montype_result(self, montype, metric, units, Type):
        """This function generates an xml with one metricgroup for every montype.
        Each metricgroup contains a metric with all the 9 combinations of direction(Rx,Tx,NA) and location(NE,FE,NA)
        If any of the columns(metric, units and Type) is empty, montype is used in the associated the pm fields."""



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
                            desc=montype if not metric else metric,
                            protocol="TL1",
                            units=montype if not units else units,
                            conversion_function="NONE" if (Type.lower() == 'gauge') else "PER_PERIOD",
                            consolidation_function="AVG" if (Type.lower() == 'gauge') else "SUM",
                            location=la_1[i],
                            direction=da_1[j],
                            min="0",
                            displayType="lineSeries-hist" if (
                                    (Type.lower() == 'gauge')) else "verticalBar-hist",
                            displayColor="BLUE" if ( da[j]== 'Tx') else "DARK_GREEN")

                ET.SubElement(doc, "parameter", name=montype,
                      collector="TL1",
                      Par_Type='COUNTER' if ((Type.lower() == 'counter')) else 'GAUGE' if (
                              (Type.lower() == 'gauge')) else 'COUNTER',
                      oid=montype)

                ET.SubElement(doc, "value", parameter=montype)






        tree = ET.ElementTree(root)
        print(montype, type(Type))
        cwd = os.getcwd()
        os.chdir(self.results_directory)
        if montype != "Montype":
            try:
                tree.write(montype+"."+"xml")
            except IOError:
                print("File name too long")
            except:
                raise
        else:
            pass
        os.chdir(cwd)






    def format_xml(self):
        """This function will format the  generated xml into human readable"""


        # path = os.dir('results/*.xml')
        # path = '/home/rupesh/TL1/pm/*.xml'
        # files = glob.glob(self.results_directory)
        files = glob.glob(os.path.join(self.path, "results/*xml"))
        for name in files:
            try:
                with open(name) as f:
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


                with open(name,'w') as f:
                    f.write(filedata)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise

    def finishing(self):
        print("finishing",os.getcwd())

        os.chdir(self.results_directory)
        print(os.getcwd())

        read_files = os.listdir(os.getcwd())

        # read_files = glob.glob(self.results_directory)
        try:
            os.chdir(self.path+ "results/")
            os.remove("result.xml")

        except:
            pass
<<<<<<< Updated upstream
        with open("result.xml", "w") as outfile:
=======
        with open("result.xml", "w",encoding='utf-8') as outfile:
>>>>>>> Stashed changes

            # writing fixed content to the pm xml
            #
            # < ?xml version = "1.0" encoding = "UTF-8"? >
            # < !DOCTYPE pmProfile PUBLIC "pm/pmProfile.dtd" "pmProfile.dtd" >
            #
            # < pmProfile name = "fujitsu-flashwave-tl1" version = "UNCLEAN" >
            #
            #
            outfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            outfile.write("<!DOCTYPE pmProfile PUBLIC \"pm/pmProfile.dtd\" \"pmProfile.dtd\">\n\n")
            outfile.write("<pmProfile name=\"fw-tl1\" version=\"UNCLEAN\" >\n\n")
            for g in read_files:

                with open(g, "r") as infile:
                    outfile.write(infile.read())

            outfile.write("\n\n</pmProfile>")

        os.chdir(self.results_directory)
        for i, j in data.items():
            # below condition to ignore the montype if it is already existing
            if i not in output:
                xml.montype_result(i, j[0], j[1], j[2])
                print(i, j[0], j[1], j[2])


xml = xmlparsing()

# xml.montype_result("CVL","description","packets","gauge")


sheet = metricsFromRequirementsdoc.parseexcel("/home/sthummala/Downloads/SmartPlugin-TestSheet-fujitsu-flashwave-9500.xlsx")
data = sheet.montypedict
print(json.dumps(data))

print("dict keys length {}".format(len(data.keys())))



# removing the files in the below folder before the generation of pm xmls
# directory= "/home/rupesh/TL1/pm/*"


<<<<<<< Updated upstream
files = glob.glob(results_directory+"*.xml")
for i in files:
    os.remove(i)
=======
# files = glob.glob(results_directory)
# for i in files:
#     os.remove(i)
>>>>>>> Stashed changes



# gets all the montyeps from the result.xml
proc=subprocess.Popen('grep -o oid=.* /home/sthummala/workspace/repo/centina/sa/profiles/pm/fujitsu-fw-4100.xml | awk -F \'"\' \'{print$2}\' | sort -u', shell=True, stdout=subprocess.PIPE )
output=proc.communicate()[0].decode().split('\n')
print(output)


os.chdir(results_directory)

for i,j in data.items():
    # below condition to ignore the montype if it is already existing
    if i not in output:
        xml.montype_result(i,j[0],j[1],j[2])
        print(i,j[0],j[1],j[2])


xml.format_xml()

xml.finishing()