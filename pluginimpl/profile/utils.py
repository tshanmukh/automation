import os
import pickle

def getrepopath():
    repopath = None
    if os.path.isfile("../.repopath.pickle"):
        infile = open("../.repopath.pickle", 'rb')
        new_dict = pickle.load(infile)
        infile.close()
        repopath = new_dict.get("repository")
        print("Repository path saved is {}".format(repopath))
    else:
        repopath = input("Enter the path to the repository: ")
        variable = {"repository": repopath}
        f = open(".repopath.pickle", 'wb')
        pickle.dump(variable, f)
        f.close()

    return repopath