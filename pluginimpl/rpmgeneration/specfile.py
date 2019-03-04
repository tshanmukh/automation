class specfile():
    def __init__(self,file="netomnia-plugininfo-util.spec"):
        self.lines = []
        self.newlines = []
        self.file =file
        f= open(self.file,'r')
        line = f.readlines()
        self.lines = [x.strip() for x in line]
        f.close()

    def data(self):
        return self.lines

    def modify(self,Release,version="3.0"):
        for i in self.lines:
            if i.startswith("Version: "):
                self.newlines.append("Version: "+version)
            elif i.startswith("Release: "):
                self.newlines.append("Release: "+Release)
            else:
                self.newlines.append(i)
        f = open(self.file,'w')
        for i in self.newlines:
            f.write(i+"\n")
        f.close()

if __name__ == "__main__":
    spec = specfile()
    lines = spec.data()
    print(type(lines),lines)
    spec.modify(Release="92")
