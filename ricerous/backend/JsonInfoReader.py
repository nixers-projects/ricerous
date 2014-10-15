# -*- coding: utf-8 -*-

import sys
import json
try:
    from ricerous.backend import Updater
except Exception:
    from backend import Updater

"""
The role of the JsonInfoReader class is to handle the information located
in the infoFile (json) so that they can be easily accessible for the rest
of the program.
"""


class JsonInfoReader:
    def __init__(self, infoFile):
        """
        Constructor takes an infoFile (String) as parameter
        """
        self._infoFile = infoFile
        info_json = open(infoFile, 'r')
        self._allInfo = json.load(info_json)
        info_json.close()
        """
        WARNING: an Updater object is created in the constructor
        Might want to read that host from a file
        """
        server = "https://raw.githubusercontent.com/nixers-projects/ricerous/master/ricerous/"
        self._updater = Updater.Updater(server, self._infoFile)

    def refresh(self):
        """
        refresh :: Int
        reload the infoFile, at failure returns -1
        """
        try:
            self._allInfo = json.load(open(self._infoFile, 'r'))
            return 0
        except Exception:
            print("cannot re-read file")
            return -1

    def update(self):
        """
        update :: Int
        use the Updater object to try updating the info file if it has new info
        if it doesn't have new info it returns 2
        if it successfully updated the info it returns 0
        if it failed it returns -1
        """
        if self._updater.hasNewInfo():
            try:
                self._updater.fetchNewInfo()
                self.refresh()
                return 0
            except Exception:
                return -1
        return 2

    def listCategories(self):
        """
        listCategories :: [String]
        return a list of categories that have information (Headers)
        """
        categories = []
        for info in self._allInfo:
            categories.append(info)
        return categories

    def listInsideCategories(self, category):
        """
        listInsideCategories :: String -> [String]
        takes a category and returns the sub-categories found for that category
        """
        if category not in self._allInfo:
            return ""
        return self._allInfo[category]

    def getInfo(self, name):
        """
        getInfo :: String -> String
        return the info for a particular category
        """
        category = self.getCategory(name)
        if category not in self._allInfo:
            return ""
        if name not in self._allInfo[category]:
            return ""
        return self._allInfo[category][name]

    def getCategory(self, name):
        """
        getCategory :: String -> String
        takes a sub-category and returns the mother category
        """
        thecategory = ""
        for category in self._allInfo:
            for info in self._allInfo[category]:
                if name == info:
                    thecategory = category
                    break
            if thecategory != "":
                break
        return thecategory


"""
if __name__ == "__main__" :
    test = JsonInfoReader("json/info.json")
    test.listCategories()
    print "\n\n"
    test.listInsideCategories("raw")
    print "\n\n"
    print test.getInfo("Shell")
    print "\n\n"
    print test.getCategory("IM")
    print "\n\n"
"""
