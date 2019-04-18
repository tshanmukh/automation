import csv
from collections import OrderedDict,Counter
import json

class profileconfigcsv():
    def __init__(self,file="profile-configs.csv"):
        f = open(file)
        self.csvFileR = csv.reader(f, delimiter=',')
        self.profilename = []
        self.duplicate = []
        self.file = OrderedDict()   # dictionary with line numbers
        self.filedict = OrderedDict()   # dictionary with plugin names as key
        self.readfile() # creates the file and filedict dictionaries
        self.updations = OrderedDict() # to store the plugins which got updated and their versions

    def readfile(self):
        """
        Reads the complete file and returns two dicts first one with profilename as key and second with line numbers
        """
        for row,value in enumerate(self.csvFileR):
            self.file[row] = value
        for row in self.file.values():
            try:
                self.filedict[row[1]] = row
            except:
                print(row)
        return self.file,self.filedict

    def findduplicates(self):
        for row in self.file.values():
            self.profilename.append(row[1])
        count = Counter(self.profilename)
        for key,value in count.items():
            if value > 1:
                print("Found "+key+" "+str(value)+" times")
                self.duplicate.append((key,value))
        if len(self.duplicate) > 0:
            return True
        else:
            return False

    def writeprofileconfigs(self, internal, pluginNames):
        file = open("profileConfigs.csv",'w')
        writer = csv.writer(file)
        writer.writerow(self.file.get(0))
        writer.writerow(self.file.get(1))
        for plugin in pluginNames:
            try:
                writer.writerow(internal.get(plugin))
                self.updations[plugin] = internal.get(plugin)[5]
            except:
                print("Entry not found for the plugin",plugin)
                exit(1)

        for i,j in self.filedict.items():
            if i not in pluginNames:
                if i == '' or i == 'name':
                    continue
                writer.writerow(j)

        return True


if __name__ == "__main__":
    external = profileconfigcsv("profile-configs.csv")
    data, dict =  external.readfile()
    # print(json.dumps(data))
    # print(json.dumps(dict))
    internal = profileconfigcsv("profile-configs-internal.csv")
    dataInternal, dict_Internal = internal.readfile()
    # print(json.dumps(data))
    # print(json.dumps(dict))
    listofplugins = input("Enter the space seperated file names: ").split(" ")
    external.writeprofileconfigs(dict_Internal,listofplugins)
    print(json.dumps(external.updations))

