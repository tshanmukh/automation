from lxml import etree

class pmfiles():
    def __init__(self,pmfilenames):
        self.filenames = pmfilenames

    def getrootelement(self,filename):
        """gets root element of file passed to it"""
        parser = etree.XMLPullParser(strip_cdata=False)
        root = etree.parse(filename,parser)
        return root

    def getdatafromfile(self,rootelement):
        """generator
            gets all the properties per metricgroup
            input: parserrootelement
            yeilds: dict with all the metricgroup id as key and two lists with metrics elements and parameter elements
            """
        for metricgroupid in rootelement.findall("metricGroup"):
            # print(etree.tostring(metricgroupid,pretty_print=True))
            groupid = metricgroupid.get("id")
            metric = metricgroupid.find("metric")
            metric_params = {i:j for i , j in metric.items()}
            parameter_parmas = {i:j for i , j in metric.find("parameter").items() }
            # pmfile_data[groupid] = (metric_params,parameter_parmas)

            yield (groupid,metric_params,parameter_parmas)




