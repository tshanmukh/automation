import re
import os
import json

tid = input("Enter the tid: ")
try:
    os.system("rm -f " + tid + '/*')
    os.system("mkdir " + tid)

except:
    pass

path = input("Enter file path: ")
nodeName = "RTRV.*" + tid + ".*;"

regex = {
    "command": re.compile(nodeName),
    "response": re.compile(r'^(")'),
    "nextcommand": re.compile(r'^_______________________________$'),
    "filechange": re.compile(r'^--$')

}


def _parse_line(line):
    """Searches the line for all the regexes defined in the dictionary regex"""
    for key, rx in regex.items():
        match = rx.search(line)
        if match:
            return key
    return None


def nonecheck(x):
    if len(x) is 0:
        return "NULL"
    else:
        return x


i = 0
file = False

allcommands = {}
with open(path, 'r') as f:
    l = f.readline().strip()
    while l:
        comm = re.compile(nodeName)
        if comm.search(l):
            command = l.strip()
            if command.split(":")[0] not in allcommands.keys():
                allcommands[command.split(":")[0].replace(';','')] = command.split(":")[3].replace(';',''), nonecheck(command.split(":")[2])
        l = f.readline()

    print(json.dumps(allcommands))

filepointer = open(path, 'r')
filedata = filepointer.read().split('\n')
print(filedata)
match = False
end = True
filepointer.close()
for command, ctag in allcommands.items():
    print(command, ctag[0].replace(';', ''), ctag[1])
    for i in filedata:
        ctagt = ctag[0].replace(";", "")
        matchACK = '^M.*' + ctagt + '.*'
        res = re.compile(matchACK)
        end = _parse_line(i.strip())
        if res.search(i):
            os.system("touch " + tid + '/' + command + '-' + ctag[1] + ".txt")
            match = True
            continue
        elif end is not "response":
            match = False

        if match:
            with open(tid + '/' + command + '-' + ctag[1] + ".txt", 'a') as f:
                try:
                    line = i.strip().strip('"')
                    f.write(line)
                    f.write('\n')
                except:
                    print("Hey!!\n. There is an error while writing to file")
