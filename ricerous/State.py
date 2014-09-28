import ricerous.JsonStateHandler

"""
The purpose of the State class is to keep track of the temporary changes
happening
"""


class State:
    def __init__(self):
        """
        Constructor doesn't take any arguments
        """
        self.selected = []
        self.comments = {}

    def load(self, loadLocation):
        """
        load :: String -> Void
        a wrapper to load state from a json file
        """
        self.selected = []
        self.comments = {}
        ricerous.JsonStateHandler.load(loadLocation, self)

    def save(self, savelocation):
        """
        save :: String -> Void
        a wrapper to save state to a json file
        """
        ricerous.JsonStateHandler.save(savelocation, self)

    def addComment(self, section, comment):
        """
        addComment :: String -> String -> Void
        takes the name of a section and a comment
        it set the comment of this section as the one specified (overwrite)
        """
        self.comments[section] = comment

    def unComment(self, section):
        """
        unComment :: String -> Void
        takes the name of a section and remove the comment associated with it
        """
        if section in self.comments:
            del(self.comments[section])

    def addSelect(self, section):
        """
        addSelect :: String -> Void
        takes the name of a section and set it as riced
        """
        if section not in self.selected:
            self.selected.append(section)

    def unSelect(self, section):
        """
        unSelect :: String -> Void
        takes the name of a section and unset it from the riced things
        """
        if section in self.selected:
            self.selected.remove(section)
