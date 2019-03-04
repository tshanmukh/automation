import csv
import collections

class profileconfigcsv():
    def __init__(self,file="profile-configs.csv"):
        f = open(file)
        self.csvfile = csv.reader(f,delimiter=',')
        self.profilename = []
        self.duplicate = []

    def findduplicates(self):
        for row in self.csvfile:
            self.profilename.append(row[1])
        count = collections.Counter(self.profilename)
        for key,value in count.items():
            if value > 1:
                print("Found "+key+" "+str(value)+" times")
                self.duplicate.append((key,value))
        if len(self.duplicate) > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    check = profileconfigcsv("profile-configs.csv")
    print(check.findduplicates())

