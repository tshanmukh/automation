import os

def copy(source,destinaion):
    if ' ' not in (source,destinaion):
        os.system("scp "+str(source)+" "+str(destinaion))