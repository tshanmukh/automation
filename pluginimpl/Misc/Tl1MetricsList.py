from lxml import etree

""" Script to generate the metric details for each metric group id per template in a profile-xml """
# def getParser(file,parsethis):
#     parser = etree.XMLParser(strip_cdata=False)
#     parsethis = etree.parse(file, parser)
#     return parsethis


def printfields(id, templateName): # templateName is pm-template name and id is the metric-group id in it
    """ Prints the details of all metrics by searching all the pm files in a profile xml"""
    if pmFiles:
        for i in pmFiles:
            # pmfile = getParser("/home/sthummala/workspace/vsure/centina/sa/profiles/" + i)
            filePath="/home/sthummala/workspace/vsure/centina/sa/profiles/" + i
            parser = etree.XMLParser(strip_cdata=False)
            pmfile = etree.parse(filePath, parser)
            for groupId in pmfile.iter("metricGroup"):
                if groupId.get("id") in id:
                    metric = groupId.findall("metric")
                    parameter=groupId.find
                    temp=templateName.split(r'/')
                    temp1=temp[10].split(r'.')
                    name=temp1[0]
                    f=open("results/"+name+".csv","a")
                    # with open("results/"+name+".csv","w") as f:
                    try:
                        for m in metric:
                            f.write(m.get("name")+","+m.find("parameter").get("oid")+","+m.get("location")+","+m.get("direction")+"\n")
                    except:
                        print("here")
    else:
        print("No pm xml files present while parsing" + templateName)


pmFiles = []
metricGroupId = []
profileXml = '/home/sthummala/workspace/vsure/centina/sa/profiles/fujitsu-flashwave-4100es-r10.xml'
parser = etree.XMLParser(strip_cdata=False)
root = etree.parse(profileXml, parser)
dependencies = root.find("dependencies")

file = dependencies.findall("file")
for a in file:
    if a.get("path").startswith("pm/templates"):
        if a.get("path").endswith(".dtd"):
            continue
        pmtemplate = "/home/sthummala/workspace/vsure/centina/sa/profiles/" + a.get("path").rstrip()
        print(pmtemplate)
        # try:
        # template = getParser(pmtemplate,"template")
        parsertemplate = etree.XMLParser(strip_cdata=False)
        template = etree.parse(pmtemplate, parsertemplate)
        perftemplate = template.find("perf-template")
        pmmetricgroups = perftemplate.find("pm-metric-groups")
        for i in pmmetricgroups.findall("value"):
            metricGroupId = metricGroupId + [i.text]
        print(metricGroupId)
        printfields(metricGroupId, pmtemplate)
        metricGroupId = []

    # except:
    #     print("Error during the template parsing")
    elif a.get("path").startswith("pm/"):
        if a.get("path").endswith(".dtd"):
            continue
        pmFiles = pmFiles + [a.get("path")]
