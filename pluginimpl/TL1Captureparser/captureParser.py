import re
from TL1Captureparser.fileNames import fileNames

nodeName="RTRV.*FARG650032-1O.*;"

regex={
    "command":re.compile(nodeName),
    "response":re.compile(r'^(")'),
    "nextcommand":re.compile(r'^_______________________________$'),
    "filechange":re.compile(r'^--$')
}

def _parse_line(line):
    """Searches the line for all the regexes defined in the dictionary regex"""
    for key,rx in regex.items():
        match=rx.search(line)
        if match:
            return key
    return None
def _list_filename(name):
    name=[]
    return name
i=0
file=False
with open("ciena-6500-otm.txt",'r') as f:
    line=f.readline().strip()
    prevline = line
    filename=None
    while line:
        key=_parse_line(line.strip())
        if key=='command':
            command=line.strip()
            uwCommand=True
        elif key == 'response':
            if not uwCommand:
                with open('results/'+filename, 'a') as result:
                    result.write(line.lstrip())
        elif key == "nextcommand":
            file=True
            filename = command.split(":")[0] +"-" +command.split(":")[2] + ".txt"
            uwCommand = False
            print(filename)
        elif key == "filechange":
            uwCommand=False
            print("code is here")


        prevline=line
        line=f.readline()


