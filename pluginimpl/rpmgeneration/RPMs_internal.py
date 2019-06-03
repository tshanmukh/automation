__author__ = 'shanmukh'
__status__ = 'Prototype'

import os
import sh
# from pexpect import pxssh
import subprocess

import builduserutils
import externalutils, general, mercurial, profileconfig, specfile


print("Copying the profile-configs csv to local")
copy = general.copy
copy(source="repouser@172.31.6.112:/var/www/html/repository/vsureplugin/profile-configs.csv", destinaion=".")  # copying the external server profile-configs


print("Enter filenames seperated by space")
names = input("Generate RPMS: ").split(' ')
profilename = []
for i in names:
    print(i)
    if len(i) >= 1:
        profilename.append(i)

print("Generating the RPM for the following plugin id's \n ", *profilename)

# Sanity checks on branch
rep = mercurial.mercurialutil()
# rep.checkbranch()
if rep.checkbranch() == "VSURE_1.8_MAINTENANCE":
    print("The branch is {}. Pulling the latest changes".format(rep.checkbranch()))
    rep.pullchanges()
else:
    print("changing the branch to VSURE_1.8_MAINTENANCE as the branch is {}".format(rep.checkbranch()))
    rep.changebranch()
# Check the branch in tools
reptools = mercurial.mercurialutil(repopath="/home/builduser/repository/tools", ip="172.31.6.112", username="builduser",
                 password="builduser")

if reptools.checkbranch() == "VSURE_1.8_MAINTENANCE":
    print("The branch is {}. Pulling the latest changes".format(rep.checkbranch()))
    reptools.pullchanges()
else:
    print("changing the branch to VSURE_1.8_MAINTENANCE as the branch is {}".format(rep.checkbranch()))
    reptools.changebranch()

build = builduserutils.builduser()

# changing the timestamp to generate only the required RPMs
build.changetimestamp(profilename)
print("Time stamp modified")
build = builduserutils.builduser()
print("Running RPM generation script")
build.generateRPM(path="/home/builduser/repository/tools/plugin-automation_37_server_final_backup/", script="createPluginRepository.py")

# subprocess.run(['ssh','builduser@172.31.6.112','python','/home/builduser/repository/tools/plugin-automation_37_server_final_backup/createPluginRepository.py'])

copy(source="builduser@172.31.6.112:/home/builduser/profile-configs.csv", destinaion="profile-configs-internal.csv")  # Copying the internal server profile-configs

print("\n\nRPM generation done.\nprofile-config.csv generated in local is copied as profile-config-internal.csv")
# print("Please do the neccessary changes to profile-config.csv and enter done")

print("Update the entry for snmp-discoverytree if needed in the file profile-configs-internal.csv and enter done")
check = True
while check:
    response = input("Response: ")

    if response.lower() == "done":
        check = False
    elif response.lower() == "stop":
        exit(1)


external = profileconfig.profileconfigcsv("profile-configs.csv")
data, dict = external.readfile()

internal = profileconfig.profileconfigcsv("profile-configs-internal.csv")
dataInternal, dict_Internal = internal.readfile()
external.writeprofileconfigs(dict_Internal, profilename)

if external.findduplicates():  # checks the duplicate entries
    print("Found Duplicate entries. correct it and rerun the code \n {}".format(*external.duplicate))
    # exit(1)


print("copying the profile-configs.csv to external and repouser")

# copy(source="profileConfigs.csv",destinaion="root@172.29.0.6:/var/www/html/repository/vsureplugin/profile-configs.csv")
copy(source="profileConfigs.csv",destinaion="repouser@172.31.6.112:/var/www/html/repository/vsureplugin/profile-configs.csv")


# obtaining the latest version RPMS to local and copying them to external
if os.path.isdir("RPMS"):
    os.system("rm RPMS/*")
else:
    sh.mkdir("RPMS")
print(external.updations)
for i,j in external.updations.items():
    copy(source="builduser@172.31.6.112:/home/builduser/1_Day_RPMS-vSure/netomnia-"+i+"-"+j+"-0.x86_64.rpm" , destinaion="./RPMS")

print("Please check the profileConfigs and \nCheck the RPMS and enter done:\n")

check = True
while check:
    response = input("Response: ")

    if response.lower() == "done":
        check = False
    elif response.lower() == "stop":
        exit(1)

util = externalutils.externalutils(username="repouser", ip="172.31.6.112", password="repopwd")
util.calculatelatestpluginutil()

print("The highest version util present in the " + util.ipaddress + " is " + util.getlatestversion())

print("Working on Specifications file")
# copy("builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/SPEC/netomnia-plugininfo-util.spec", ".")

spefifications = specfile.specfile()
spefifications.modify(Release=str(util.latestpluginustil + 1))

print("Modified the specifications file")
print("Copying the specifications file to builduser: ")

copy(source="netomnia-plugininfo-util.spec", destinaion="builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/SPEC/netomnia-plugininfo-util.spec")

# print(os.system('gnome-terminal -e \'sh -c "ssh builduser@172.31.6.112 ./test.sh;touch completedtheutil"\''))

subprocess.run(['ssh','builduser@172.31.6.112','./test.sh'])

# copying all the RPMS in the RPMS folder to external
copy(source="builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/vsure-plugininfo-util-3.0-"+str(int(util.getlatestversion())+1)+".x86_64.rpm" , destinaion="./RPMS")
print("Copying the RPMS to internal\n")

# os.system('gnome-terminal -e \'sh -c "scp ./RPMS/* root@172.29.0.6:/var/www/html/repository/vsureplugin/"\'')
os.system('gnome-terminal -e \'sh -c "scp ./RPMS/* repouser@172.31.6.112:/var/www/html/repository/vsureplugin/"\'')
# subprocess.run('scp /home/sthummala/myworkspace/automation/pluginimpl/rpmgeneration/RPMS/* root@172.29.0.6:/var/www/html/repository/vsureplugin/')
# subprocess.run(['scp','/home/sthummala/myworkspace/automation/pluginimpl/rpmgeneration/RPMS/*','repouser@172.31.6.112:/var/www/html/repository/vsureplugin/'])


print("copied the RPMS required to repositories")
