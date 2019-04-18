__author__ = 'shanmukh'
__status__ = 'Prototype'

from pexpect import pxssh
import general

class builduser():
    """Class which impliments methods in process to generate the RPMs"""
    def __init__(self, ip='172.31.6.112',username="builduser",password="builduser"):
        self.s = pxssh.pxssh()
        self.username = username
        self.ipaddress = ip
        self.password = password
        if not self.s.login(self.ipaddress, self.username, self.password):
            print("SSH session failed on login.")
            exit(1)

    def changetimestamp(self,profilename):
        """Changes timestamp to current time only to the profiles which require the RPM generation"""
        self.s.sendline("cd repository/centina/repository/profiles/")
        self.s.prompt()
        self.s.sendline("touch -t 1901010101 *")
        self.s.prompt()
        for pro in profilename:
            self.s.sendline("touch "+pro+".pro")
        self.s.close()

    def generateRPM(self,path="/home/builduser/repository/tools/plugin-automation_37_server_final_backup/",script="createPluginRepository.py"):
        """Runs the RPM generation script"""
        self.s.sendline("cd  "+path)
        self.s.prompt()
        self.s.sendline("python "+script)
        self.s.prompt()
        print(self.s.before.decode('utf-8'))
        self.s.close()

    def prepareutil(self):
        general.copy(source="rpm.exp", destinaion="builduser@172.31.6.112:/home/builduser/repository/tools/rpmbuild/SPEC/")
        self.s.sendline("cd /home/builduser/repository/tools/rpmbuild/SPEC/")
        self.s.prompt()
        self.s.sendline("chmod +x rpm.exp")
        self.s.prompt()
        print(self.s.before.decode('utf-8'))
        self.s.close()

    def removeexp(self):
        self.s.sendline("cd /home/builduser/repository/tools/rpmbuild/SPEC/")
        self.s.prompt()
        self.s.sendline("rm rpm.exp")
        self.s.prompt()



        # self.utils = self.s.before.decode('utf-8').split('\r\n')[1:]

if __name__ == "__main__":
    rpm = builduser(username="builduser",ip="172.31.6.112",password="builduser")
    temp = ['eltek', 'snmp-discoverytree','evertz-7000']
    rpm.changetimestamp(temp)
    rpm = builduser(username="builduser", ip="172.31.6.112", password="builduser")
    rpm.generateRPM()
