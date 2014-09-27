from urllib import URLopener
from time import gmtime
import md5

"""
The role of this class is to handle the Update of the configurations
"""

# doesn't actually have latest json


class Updater:
    """
    takes a server location and an info file as parameters in the constructor
    it will use this server to fetch the new information
    there should be a /hash and /info.json dir on this server
    """
    def __init__(self, server, infoFile):
        self._server = server
        self._infoFile = infoFile
        self.br = URLopener()

    """
    hasNewInfo :: Boolean
    compare the local version tag with the one found on the server
    and returns true if the server version is newer
    """
    def hasNewInfo(self):
        jsonDate = open('version', 'r').read()
        servDate = self.br.open(self._server).read()
        return (jsonDate < servDate)

    """
    generateTimeStamp :: String
    returns a string that is used to timestamp old config backup files
    """
    def generateTimeStamp(self):
        return str(gmtime().tm_year) + "_" + str(gmtime().tm_mday) + "_" + \
            str(gmtime().tm_hour) + "_" + str(gmtime().tm_min)

    """
    fetchNewInfo :: Void
    it will download the info file from the server
    use the timestamp to back it up
    and overwrite it
    """
    def fetchNewInfo(self):
        response = self.br.open(self._server).read()
        oldInfo = open(self._infoFile, 'r').read()
        open(self._infoFile+"."+self.generateTimeStamp(), 'w').write(oldInfo)
        open(self._infoFile, 'w').write(response)
