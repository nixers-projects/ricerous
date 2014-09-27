import JsonStateHandler

"""
The purpose of the State class is to keep track of the temporary changes
happening
"""


class State:
    """
    Constructor doesn't take any arguments
    """
    def __init__(self):
        self.selected = []
        self.comments = {}

    """
    load :: String -> Void
    a wrapper to load state from a json file
    """
    def load(self, loadLocation):
        self.selected = []
        self.comments = {}
        JsonStateHandler.load(loadLocation, self)

    """
    save :: String -> Void
    a wrapper to save state to a json file
    """
    def save(self, savelocation):
        JsonStateHandler.save(savelocation, self)

    """
    addComment :: String -> String -> Void
    takes the name of a section and a comment
    it set the comment of this section as the one specified (overwrite)
    """
    def addComment(self, section, comment):
        self.comments[section] = comment

    """
    unComment :: String -> Void
    takes the name of a section and remove the comment associated with it
    """
    def unComment(self, section):
        if section in self.comments:
            del(self.comments[section])

    """
    addSelect :: String -> Void
    takes the name of a section and set it as riced
    """
    def addSelect(self, section):
        if section not in self.selected:
            self.selected.append(section)

    """
    unSelect :: String -> Void
    takes the name of a section and unset it from the riced things
    """
    def unSelect(self, section):
        if section in self.selected:
            self.selected.remove(section)
