import os
import pandas as pd
import json
import pymysql
from tqdm import tqdm

import logging

logging.basicConfig(filename='pm_migration.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


old_file_path = 'old_metric_data.csv'
new_file_path = 'new_metric_data.csv'

old_file = pd.read_csv(old_file_path, header=None)

new_file = pd.read_csv(new_file_path, header=None)

new_file_dict = {(oid, loc, dir):id for oid, loc, dir, id in zip(new_file[0], new_file[1], new_file[2],new_file[3])} # creating a dictionary for the new metric id's
new_file_dict_id = {id:(oid, loc, dir) for oid, loc, dir, id in zip(new_file[0], new_file[1], new_file[2],new_file[3])} # creating a dictionary for the new metric id's

try:
    # connects to db
    connection = pymysql.connect(host='172.30.0.141', user ='centina', password ='centina', port=3307, db='sa', cursorclass=pymysql.cursors.DictCursor )
    connection.autocommit = True
    logging.info("Connected to database")
except:
    logging.ERROR("Connection to database failed")

cursor = connection.cursor() #obtaining the cursor

# deleting the old files if they are present
if os.path.isfile('db_ids.csv'):
    os.remove('db_ids.csv')

if os.path.isfile('db_ids_notfound.csv'):
    os.remove('db_ids_notfound.csv')



# copying the metric from old_metric_data.csv file and searching it in new_metric_data.csv
for metric in zip(old_file[0], old_file[1], old_file[2],old_file[3]):
    search_metric = (metric[0], metric[1], metric[2])

    if search_metric in new_file_dict.keys():
        # Get the longId and write to file
        cursor.execute('select longId from managed_object where id='+'"'+metric[3]+'"')
        for i in cursor.fetchall():
            old_longid = i

        cursor.execute('select longId from managed_object where id="'+new_file_dict.get(search_metric)+'"')
        for i in cursor.fetchall():
            new_longid = i

        # updating the database with the new values
        cursor.execute("select count(*) from pm.perf_raw where pmParmId='"+str(*old_longid)+"'") # checking the count in the database
        for i in cursor.fetchall():

            if i[0] > 0: # execute db command only if the cound is greated than 0
                logging.debug("Found {} entries".format(i[0]))
                logging.debug("Executing the update statement. \n" + "update pm.perf_raw set pmParmId = '" + str(*new_longid) + "' where pmParmId = '" + str(*old_longid) + "'")

                cursor.execute("update pm.perf_raw set pmParmId = '"+ str(*new_longid) + "' where pmParmId = '"+ str(*old_longid) +"'")
                for i in cursor.fetchall():
                    print(i)
                logging.debug("commiting the changes to database. {} ---> {} \n".format(old_longid,new_longid))

                try:
                    connection.commit()
                except:
                    connection.rollback()
                    logging.error("unable to commit the changes to database. Rolling back the changes")
                    raise

                with open('db_ids.csv','a') as f:
                    f.write('"{}","{}","{}","{}"\n'.format(metric[3],*old_longid,new_file_dict.get(search_metric),*new_longid))
                    logging.debug('"{}","{}","{}","{}"\n'.format(metric[3],*old_longid,new_file_dict.get(search_metric),*new_longid))

            else:
                logging.info("Skipped perf_raw updation as count is {}".format(i[0]))

        # updating the database with the new values
        cursor.execute("select count(*) from pm.perf_1_hour where pmParmId='" + str(
            *old_longid) + "'")  # checking the count in the database
        for i in cursor.fetchall():

            if i[0] > 0:  # execute db command only if the cound is greated than 0
                logging.debug("Found {} entries".format(i[0]))
                logging.debug(
                    "Executing the update statement. \n" + "update pm.perf_raw set pmParmId = '" + str(
                        *new_longid) + "' where pmParmId = '" + str(*old_longid) + "'")

                cursor.execute(
                    "update pm.perf_1_hour set pmParmId = '" + str(*new_longid) + "' where pmParmId = '" + str(
                        *old_longid) + "'")
                for i in cursor.fetchall():
                    print(i)
                logging.debug(
                    "commiting the changes to database. {} ---> {} \n".format(old_longid, new_longid))

                try:
                    connection.commit()
                except:
                    connection.rollback()
                    logging.error("unable to commit the changes to database. Rolling back the changes")
                    raise

            else:
                logging.info("skipping perf_1_hour updation as count is {}".format(i[0]))
        # updating the database with the new values
        cursor.execute("select count(*) from pm.perf_current where pmParmId='" + str(
            *old_longid) + "'")  # checking the count in the database
        for i in cursor.fetchall():

            if i[0] > 0:  # execute db command only if the cound is greated than 0
                logging.debug("Found {} entries".format(i[0]))
                logging.debug(
                    "Executing the update statement. \n" + "update pm.perf_raw set pmParmId = '" + str(
                        *new_longid) + "' where pmParmId = '" + str(*old_longid) + "'")

                cursor.execute(
                    "update pm.perf_1_hour set pmParmId = '" + str(*new_longid) + "' where pmParmId = '" + str(
                        *old_longid) + "'")
                for i in cursor.fetchall():
                    print(i)
                logging.debug(
                    "commiting the changes to database. {} ---> {} \n".format(old_longid, new_longid))

                try:
                    connection.commit()
                except:
                    connection.rollback()
                    logging.error("unable to commit the changes to database. Rolling back the changes")
                    raise

            else:
                logging.info("skipping perf_current updation as count is {}".format(i[0]))

        # updating the database with the new values
        cursor.execute("select count(*) from pm.perf_1_day where pmParmId='" + str(
            *old_longid) + "'")  # checking the count in the database
        for i in cursor.fetchall():

            if i[0] > 0:  # execute db command only if the cound is greated than 0
                logging.debug("Found {} entries".format(i[0]))
                logging.debug(
                    "Executing the update statement. \n" + "update pm.perf_raw set pmParmId = '" + str(
                        *new_longid) + "' where pmParmId = '" + str(*old_longid) + "'")

                cursor.execute(
                    "update pm.perf_1_day set pmParmId = '" + str(*new_longid) + "' where pmParmId = '" + str(
                        *old_longid) + "'")
                for i in cursor.fetchall():
                    print(i)
                logging.debug(
                    "commiting the changes to database. {} ---> {} \n".format(old_longid, new_longid))

                try:
                    connection.commit()
                except:
                    connection.rollback()
                    logging.error("unable to commit the changes to database. Rolling back the changes")
                    raise
            else:
                logging.info("skipping perf_1_day updation as count is {}".format(i[0]))
    else:
        with open('db_ids_notfound.csv', 'a') as g:
            g.write("{}\n".format(metric))
            logging.warning("Metric not found in new metrics list: {}".format(search_metric))

logging.info("End of process")
connection.close()
