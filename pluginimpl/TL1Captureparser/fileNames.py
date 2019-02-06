class fileNames(object):

    def __init__(self,filename):
        """

        :param filename: some name
        """
        self.nameofthefile=filename
        self.response = []

    def create(self):
        self.response = []
        return fileNames

    def add(self,someresponse):
        self.response.append(someresponse)

    def __str__(self):
        print(self.response)
