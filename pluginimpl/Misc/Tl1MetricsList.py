import os
from lxml import etree

""" Script to generate the metric details for each metric group id per template in a profile-xml 
    Creates csv files corresponding to each template with all the metrics supported by it according to the plugin
"""


def printfields(id, templateName):
    """ Prints the details of all metrics by searching all the pm files in a profile xml
        id is a list which contains all the metric groupids of a specific template
        templateName is the name of the pm-template
    """
    if pmFiles:
        for i in pmFiles:
            filePath = "/home/sthummala/workspace/repo/centina/sa/profiles/" + i
            ref=i.split("/")
            reference=ref[1].replace(".xml","")

            parser = etree.XMLParser(strip_cdata=False)
            pmfile = etree.parse(filePath, parser)
            for groupId in pmfile.iter("metricGroup"):
                if groupId.get("id") in id:
                    metric = groupId.findall("metric")
                    parameter = groupId.find
                    temp = templateName.split(r'/')  # getting the template name to create the results file
                    temp1 = temp[10].split(r'.')
                    name = temp1[0]
                    f = open("results/" + name + ".csv", "a")  # opening file with template name in append mode
                    try:
                        if protocol == "SNMP":
                            for m in metric:
                                f.write(str(groupId.get("name")) + "," + str(m.get("name")) +reference+ "," + str(
                                    m.find("parameter").get("oid"))+"\n")
                                print(m.get("name"),groupId.get("name"),reference)
                        else:
                            # todo if multiple parameters are present
                            for m in metric:
                                f.write(str(groupId.get("id")) +','+str(m.get('id'))+ "," + str(m.get("name")) + "," + str(
                                    m.find("parameter").get("oid")) + "," + str(m.get("units"))+","+str(m.get("location")) + "," + str(
                                    m.get("direction")) + "\n")
                    except:
                        print("Exception while looping through the metricgroup id", str(groupId.get("id")))
                        exit()
                    finally:
                        f.close()
    else:
        print("No pm xml files present while parsing" + templateName)


# to clean files in the results folder if they are already present
files=os.listdir("results/")
for file in files:
    os.remove("results/"+file)

pmFiles = []
metricGroupId = []
pluginName = input("Please enter the plugin name: ")
# todo modification to have a generic path
profileXml = '/home/sthummala/workspace/repo/centina/sa/profiles/' + pluginName + '.xml'
parser = etree.XMLParser(strip_cdata=False)
root = etree.parse(profileXml, parser)
meta = root.find("meta")
protocol = meta.find("protocol").get("name")
dependencies = root.find("dependencies")

file = dependencies.findall("file")
for a in file:
    if a.get("path").startswith("pm/templates"):
        if a.get("path").endswith(".dtd"):
            continue
        pmtemplate = "/home/sthummala/workspace/repo/centina/sa/profiles/" + a.get("path")
        print("Found pm template ", pmtemplate)
        # try:
        # template = getParser(pmtemplate,"template")
        parsertemplate = etree.XMLParser(strip_cdata=False)
        template = etree.parse(pmtemplate, parsertemplate)
        perftemplate = template.find("perf-template")
        pmmetricgroups = perftemplate.find("pm-metric-groups")
        for i in pmmetricgroups.findall("value"):
            metricGroupId = metricGroupId + [i.text]
        print("Metric Groups are", metricGroupId)
        printfields(metricGroupId , pmtemplate)  # Function prints all the parms for the id's passed to it looping in the PM xml paths added in the profile xml
        metricGroupId = []

    # except:
    #     print("Error during the template parsing")
    elif a.get("path").startswith("pm/"):
        if a.get("path").endswith(".dtd"):
            continue
        pmFiles = pmFiles + [a.get("path")]
