# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pymysql

connection = pymysql.connect(host='172.31.5.21', user ='centina', password ='centina', port=3307, db='sa')

cursor = connection.cursor()

cursor.execute('show tables;')
for line in cursor.fetchall():
    if line[0] == 'topology_network_element':
        # cursor.execute('desc sa.topology_network_element')
        # for line in cursor.fetchall():
        #     print (line)
        cursor.execute('select id,profileId  from sa.topology_network_element where profileId like "%ciena%";')
        for l in cursor.fetchall():
            print(l)