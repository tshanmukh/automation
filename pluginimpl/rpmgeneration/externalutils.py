from pexpect import pxssh
import re


class externalutils():
    def __init__(self, username, ip, password):
        self.s = pxssh.pxssh()
        self.username = username
        self.ipaddress = ip
        self.password = password

        if not self.s.login(self.ipaddress, self.username, self.password):
            print("SSH session failed on login.")
            exit(1)
        self.files()

    def files(self):
        self.s.sendline("cd /var/www/html/repository/vsureplugin")
        self.s.prompt()  # match the prompt
        self.s.sendline("ls -1rth *.rpm")
        self.s.prompt()
        self.rpms = self.s.before.decode('utf-8').split('\r\n')[1:]
        self.s.sendline("ls -1rth *.csv")
        self.s.prompt()
        self.profileconfig = self.s.before.decode('utf-8').split('\r\n')[1:]
        self.s.sendline("ls -1rth vsure-plugininfo-util-3.0*")
        self.s.prompt()
        self.utils = self.s.before.decode('utf-8').split('\r\n')[1:]

    def calculatelatestpluginutil(self):
        # self.s.sendline("cd /var/www/html/repository/vsureplugin")
        # self.s.prompt() # match the prompt
        # self.s.sendline("ls -1rth vsure-plugininfo-util-3.0*")
        # self.s.prompt()
        # self.list = self.s.before.decode('utf-8').split('\r\n')[1:]
        self.temp = self.utils.copy()
        for i in range(len(self.temp)):
            if self.temp[i].startswith("vsure-plugininfo-util-3.0"):
                self.temp[i] = re.sub('vsure-plugininfo-util-3.0-', '', self.temp[i])
                self.temp[i] = int(re.sub('.x86_64.rpm', '', self.temp[i]))
            elif len(self.temp[i]) <= 2:
                del self.temp[i]
        self.latestpluginustil = max(self.temp)
        # self.s.logout()

    def getlatestversion(self):
        return str(self.latestpluginustil)


if __name__ == "__main__":
    util = externalutils(ip="172.29.0.6", username="root", password="passw0rd")
    util.calculatelatestpluginutil()
    print(util.getlatestversion())
    print(util.utils)
    print(util.rpms)
    print(util.profileconfig)
