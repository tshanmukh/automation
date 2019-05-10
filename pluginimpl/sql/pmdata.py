# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pymysql

connection = pymysql.connect(host='172.31.6.133', user ='centina', password ='centina', port=3307, db='pm')

cursor = connection.cursor()

def getpmsourcetypes():
    pm = set()
    cursor.execute("select distinct ep2.sourcetype from sa.end_point ep2,sa.managed_object mo2 where ep2.id=mo2.id and mo2.longid in ( select pointid from (select pointid from perf_cable_cmts_current union all select pointid from perf_cable_device_cmts_current union all select pointid from perf_cable_device_modem_current union all select pointid from perf_cable_device_mta_current union all select pointid from perf_cable_modem_docsis_current union all select pointid from perf_cable_stream_current union all select pointid from perf_current union all select pointid from perf_eth_fp_current union all select pointid from perf_eth_if_current ) a where pointid in (select mo.longid from sa.end_point ep,sa.managed_object mo where mo.id=ep.id and  ep.networkElementName='MNRGKSXBOS1-RFW95005'));")
    for l in cursor.fetchall():
        pm.add(l[0])
    return pm


# cursor.execute('show tables;')
# for i in cursor.fetchall():
#     print (i)
# cursor.execute('show tables;')
# for line in cursor.fetchall():
#     if line[0] == 'topology_network_element':
#         # cursor.execute('desc sa.topology_network_element')
#         # for line in cursor.fetchall():
#         #     print (line)
#         cursor.execute("select distinct ep2.sourcetype from sa.end_point ep2,sa.managed_object mo2 where ep2.id=mo2.id and mo2.longid in ( select pointid from (select pointid from perf_cable_cmts_current union all select pointid from perf_cable_device_cmts_current union all select pointid from perf_cable_device_modem_current union all select pointid from perf_cable_device_mta_current union all select pointid from perf_cable_modem_docsis_current union all select pointid from perf_cable_stream_current union all select pointid from perf_current union all select pointid from perf_eth_fp_current union all select pointid from perf_eth_if_current ) a where pointid in (select mo.longid from sa.end_point ep,sa.managed_object mo where mo.id=ep.id and  ep.networkElementName='MNRGKSXBOS1-RFW95005'));")
#         for l in cursor.fetchall():
#             print(l)