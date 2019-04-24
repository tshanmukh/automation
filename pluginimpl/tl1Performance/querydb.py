# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pymysql

class querydb():
    def __init__(self,host,db,user='centina',password='centina',port=3307):
        self.connection = pymysql.connect(host=host, user =user, password =password, port=3307, db=db)
        self.cursor = self.connection.cursor()

    def getpmsourcetypes(self, nodename):
        pm = set()
        self.cursor.execute("select distinct ep2.sourcetype from sa.end_point ep2,sa.managed_object mo2 where ep2.id=mo2.id and mo2.longid in ( select pointid from (select pointid from perf_cable_cmts_current union all select pointid from perf_cable_device_cmts_current union all select pointid from perf_cable_device_modem_current union all select pointid from perf_cable_device_mta_current union all select pointid from perf_cable_modem_docsis_current union all select pointid from perf_cable_stream_current union all select pointid from perf_current union all select pointid from perf_eth_fp_current union all select pointid from perf_eth_if_current ) a where pointid in (select mo.longid from sa.end_point ep,sa.managed_object mo where mo.id=ep.id and  ep.networkElementName='"+nodename+"'));")
        for l in self.cursor.fetchall():
            pm.add(l[0])
        return pm

if __name__ == "__main__":
    db = querydb(host="172.31.6.133",db='pm')
    print(db.getpmsourcetypes('MNRGKSXBOS1-RFW95005'))