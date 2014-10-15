import sys
if sys.version < '3':
    from urllib import URLopener
else:
    from urllib import request

try:
    from ricerous.backend import location_manager
except Exception:
    from backend import location_manager

"""
The role of this class is to handle the Update of the configurations
"""


class Updater:
    def __init__(self, server, infoFile):
        """
        takes a server location and an info file as parameters in the constructor
        it will use this server to fetch the new information
        there should be a json/version and json/info.json dir on this server
        """
        self._infoFile = infoFile
        self._serverJSON = server + self._infoFile
        self._serverDate = server + "json/version"
        if sys.version < '3':
            self.br = URLopener()
        else:
            self.br = request

    def hasNewInfo(self):
        """
        hasNewInfo :: Boolean
        compare the local version tag with the one found on the server
        and returns true if the server version is newer
        """
        jsonDate = open(location_manager.VERSION , 'r').read().strip()
        if sys.version < '3':
            servDate = self.br.open(self._serverDate).read().strip()
        else:
            servDate = self.br.urlopen(self._serverDate).read().strip()
        return (int(jsonDate) < int(servDate))

    def generateTimeStamp(self):
        """
        generateTimeStamp :: String
        returns a string that is used to timestamp old config backup files
        """
        return open(location_manager.VERSION, 'r').read().strip()

    def fetchNewInfo(self):
        """
        fetchNewInfo :: Void
        it will download the info file from the server
        use the timestamp to back it up
        and overwrite it
        """
        # Fetching server's info.json
        if sys.version < '3':
            response = self.br.open(self._serverJSON).read()
        else:
            response = self.br.urlopen(self._serverJSON).read().decode("utf-8")
        oldInfo = open(self._infoFile, 'r').read()
        open(self._infoFile + "." + self.generateTimeStamp(), 'w').write(oldInfo)
        open(self._infoFile, 'w').write(response)
        # Fetching server's version
        if sys.version < '3':
            servDate = int(self.br.open(self._serverDate).read().strip())
        else:
            servDate = int(self.br.urlopen(self._serverDate).read().strip())
        open(location_manager.VERSION, 'w').write(str(servDate))
