__author__ = 'shanmukh'
__status__ = 'Prototype'

import os
import subprocess

print("started the terminal")


# proc = subprocess.Popen('gnome-terminal -e \'sh -c "ssh builduser@172.31.6.112 ./test.sh"\'', shell=True,stdout=subprocess.PIPE)
proc = subprocess.Popen('gnome-terminal -e "ssh builduser@172.31.6.112 ./test.sh"', shell=True,stdout=subprocess.PIPE)

proc.wait()

print(proc.stdout.read())
# os.system('gnome-terminal -e \'sh -c "ssh builduser@172.31.6.112 ./test.sh"\'')

# pid = os.getpid()


print("printing this after the terminal is closed")