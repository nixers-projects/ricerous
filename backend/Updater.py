from urllib import URLopener

"""
The role of this class is to handle the Update of the configurations
"""


class Updater:
    """
    takes a server location and an info file as parameters in the constructor
    it will use this server to fetch the new information
    there should be a /hash and /info.json dir on this server
    """
    def __init__(self, server, infoFile):
        self._infoFile = infoFile
        self._serverJSON = server + self._infoFile
        self._serverDate = server + "json/version"
        self.br = URLopener()

    """
    hasNewInfo :: Boolean
    compare the local version tag with the one found on the server
    and returns true if the server version is newer
    """
    def hasNewInfo(self):
        jsonDate = open('json/version', 'r').read().strip()
        servDate = self.br.open(self._serverDate).read().strip()
        return (int(jsonDate) < int(servDate))

    """
    generateTimeStamp :: String
    returns a string that is used to timestamp old config backup files
    """
    def generateTimeStamp(self):
        return open('json/version', 'r').read().strip()

    """
    fetchNewInfo :: Void
    it will download the info file from the server
    use the timestamp to back it up
    and overwrite it
    """
    def fetchNewInfo(self):
        # Fetching server's info.json
        response = self.br.open(self._serverJSON).read()
        oldInfo = open(self._infoFile, 'r').read()
        open(self._infoFile + "." + self.generateTimeStamp(), 'w').write(oldInfo)
        open(self._infoFile, 'w').write(response)
        # Fetching server's version
        servDate = int(self.br.open(self._serverDate).read().strip())
        open("json/version", 'w').write(str(servDate))
