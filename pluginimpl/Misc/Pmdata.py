import csv
import numpy as np

# template = input("Enter the file name: ")
template = "ciena-6500-ots-tl1.csv"

sourcename = input("Enter the source name: ")
rows = []
count=0

with open("results/"+template,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append([row[3],row[5],row[6]])

for res in rows:
    if res[1] == "NEAR_END":
        direction = "NEND"
    elif res[1] == "FAR_END":
        direction = "FEND"
    else:
        direction = "NA"

    if res[2] == "RECEIVE":
        location = "RCV"
    elif res[2] == "TRANSMIT":
        location = "TRMT"
    else:
        location = "NA"

    Timeperiod = "15-MIN"

    value = str(np.random.random_integers(0,100))
    count +=1
    print(sourcename+":"+res[0]+","+value+","+"TRUE,"+direction+","+location+","+Timeperiod+",01-22,02-00,1")
print("Count is ",count)