__author__ = 'shanmukh'
__status__ = 'Prototype'

import os
from pexpect import pxssh


class mercurialutil():
    def __init__(self, repopath="/home/builduser/repository/centina", ip="172.31.6.112", username="builduser",
                 password="builduser"):
        self.repoPath = repopath
        self.ip = ip
        self.username = username
        self.password = password
        self.s = pxssh.pxssh()
        if not self.s.login(self.ip, self.username, self.password):
            print("SSH session failed on login.")
            exit(1)
        # self.repo = hglib.open(self.repoPath) # Todo implement local usecases with hglib

    def checkbranch(self):
        self.s.sendline("cd " + self.repoPath)
        self.s.prompt()
        self.s.sendline("hg branch")
        self.s.prompt()
        self.branch = self.s.before.decode('utf-8').split('\r\n')[1]
        return self.branch

    def changebranch(self, newBranch="VSURE_DEVELOPMENT"):
        self.s.sendline("cd " + self.repoPath)
        self.s.prompt()
        self.s.sendline("hg up -C " + newBranch)
        self.s.prompt()
        print(self.s.before.decode('utf-8'))

    def pullchanges(self):
        self.s.sendline("hg pull")
        self.s.prompt()
        self.s.sendline("hg up")
        self.s.prompt()

if __name__ == '__main__':
    rep = mercurialutil()
    print(rep.checkbranch())


