# -*- coding: utf-8 -*-

import sys
import json
import Updater

"""
The role of the JsonInfoReader class is to handle the information located
in the infoFile (json) so that they can be easily accessible for the rest
of the program.
"""


class JsonInfoReader:
    """
    Constructor takes an infoFile (String) as parameter
    """
    def __init__(self, infoFile):
        self._infoFile = infoFile
        info_json      = open(infoFile, 'r')
        self._allInfo  = json.load(info_json)
        info_json.close()
        # Might want to read that host from a file
        """
        WARNING: an Updater object is created in the constructor
        """
        self._updater = Updater.Updater("http://venam.nixers.net",
                                        self._infoFile)

    """
    refresh :: Int
    reload the infoFile, at failure returns -1
    """
    def refresh(self):
        try:
            self._allInfo = json.load(open(self._infoFile, 'r'))
            return 0
        except Exception:
            print("cannot re-read file")
            return -1

    """
    update :: Int
    use the Updater object to try updating the info file if it has new info
    if it doesn't have new info it returns 2
    if it successfully updated the info it returns 0
    if it failed it returns -1
    """
    def update(self):
        if self._updater.hasNewInfo():
            try:
                self._updater.fetchNewInfo()
                self.refresh()
                return 0
            except Exception:
                return -1
        return 2

    """
    listCategories :: [String]
    return a list of categories that have information (Headers)
    """
    def listCategories(self):
        categories = []
        for info in self._allInfo:
            categories.append(info)
        return categories

    """
    listInsideCategories :: String -> [String]
    takes a category and returns the sub-categories found for that category
    """
    def listInsideCategories(self, category):
        if category not in self._allInfo:
            return ""
        return self._allInfo[category]

    """
    getInfo :: String -> String
    return the info for a particular category
    """
    def getInfo(self, name):
        category = self.getCategory(name)
        if category not in self._allInfo:
            return ""
        if name not in self._allInfo[category]:
            return ""
        return self._allInfo[category][name]

    """
    getCategory :: String -> String
    takes a sub-category and returns the mother category
    """
    def getCategory(self, name):
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
    test = JsonInfoReader("info.json")
    test.listCategories()
    print "\n\n"
    test.listInsideCategories("raw")
    print "\n\n"
    print test.getInfo("Shell")
    print "\n\n"
    print test.getCategory("IM")
    print "\n\n"
"""
