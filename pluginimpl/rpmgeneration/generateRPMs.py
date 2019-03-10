from rpmgeneration import builduserutils
from rpmgeneration import externalutils
from rpmgeneration import general
from rpmgeneration import specfile
from rpmgeneration import profileconfig
from rpmgeneration import mercurial

import os

print("Copying the profile-configs csv to local")
copy = general.copy
copy(source="root@172.29.0.6:/var/www/html/repository/vsureplugin/profile-configs.csv",
     destinaion=".")  # copying the external server profile-configs

# os.system("scp root@172.29.0.6:/var/www/html/repository/vsureplugin/profile-configs.csv .")

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
rep.checkbranch()
if rep.checkbranch() == "VSURE_DEVELOPMENT":
    rep.pullchanges()
else:
    print("changing the branch to VSURE_DEVELOPMENT")
    rep.changebranch()

build = builduserutils.builduser()

# changing the timestamp to generate only the required RPMs
build.changetimestamp(profilename)
print("Time stamp modified")
build = builduserutils.builduser()
print("Running RPM generation script")
build.generateRPM(path="/home/builduser/repository/tools/plugin-automation_37_server_final_backup/",
                  script="createPluginRepository.py")

copy(source="builduser@172.31.6.112:profile-configs.csv",
     destinaion="profile-configs-internal.csv")  # Copying the internal server profile-configs

print("\n\nRPM generation done.\nprofile-config.csv generated in local is copied as profile-config-internal.csv")
print("Please do the neccessary changes to profile-config.csv and enter done")

external = profileconfig.profileconfigcsv("profile-configs.csv")
data, dict = external.readfile()

internal = profileconfig.profileconfigcsv("profile-configs-internal.csv")
dataInternal, dict_Internal = internal.readfile()
external.writeprofileconfigs(dict_Internal, profilename)

if external.findduplicates():  # checks the duplicate entries
    print("Found Duplicate entries. correct it and rerun the code")
    exit(1)

print("Please check the profile-configs and enter done")

check = True
while check:
    response = input("Response: ")

    if response.lower() == "done":
        check = False
    elif response.lower() == "stop":
        exit(1)

util = externalutils.externalutils(username="root", ip="172.29.0.6", password="passw0rd")
util.calculatelatestpluginutil()

print("The highest version util present in the " + util.ipaddress + " is " + util.getlatestversion())

print("Working on Specifications file")
copy("builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/SPEC/netomnia-plugininfo-util.spec", ".")

spefifications = specfile.specfile()
spefifications.modify(Release=str(util.latestpluginustil + 1))

print("Modified the specifications file")
print("Copying the specifications file to builduser: ")

copy(source="netomnia-plugininfo-util.spec",
     destinaion="builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/SPEC/netomnia-plugininfo-util.spec")

os.system('gnome-terminal -e \'sh -c "ssh builduser@172.31.6.112 ./test.sh"\'')
