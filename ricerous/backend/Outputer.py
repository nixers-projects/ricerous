import importlib
import pkgutil
import inspect

"""
The purpose of the Outputer class it to provide a dynamic way of outputing
the State object (State.py)
It loads all the available plugins from a plugin directory
"""


PLUGIN_PATHS = ["plugins"]


class Outputer:
    def __init__(self, plugin_paths):
        """
        Constructor takes the plugin path
        """
        self.plugin_paths = [plugin_paths]

    def lister(self):
        """
        lister :: [String]
        returns the list of available plugins
        """
        path = self.plugin_paths
        availables = []
        for loader, modname, is_pkg in pkgutil.walk_packages(path):
            module = loader.find_module(modname).load_module(modname)
            good = 0
            for name, value in inspect.getmembers(module):
                if name.startswith('__'):
                    continue
                if name == "getName":
                    good += 1
                if name == "output":
                    good += 1
            # Has the 2 functions getName and output, so it's a good plugin
            if good == 2:
                availables.append(modname)
        return availables

    def getAvailable(self):
        """
        getAvailable :: [String]
        a wrapper to return the list of available plugins
        """
        # availables = self.lister()

        # for available in availables:
        #     m = importlib.import_module('plugins.'+available)
        #     m.getName()
        return self.lister()

    def output(self, module, state, info, location):
        """
        output :: String -> State -> JsonInfoReader -> String -> Void
        takes the name of the output module (can be listed using getAvailable())
        , a State object, a JsonInfoReader object, the location where you want
        to save the output.
        it will call the `output` method on the dynamically loaded module from the
        plugin directory
        """
        toImp = self.plugin_paths[0].replace("/", ".")
        if not toImp.endswith("."):
            toImp = toImp + "."
        if "eggs" in toImp.lower() :
            toImp = "ricerous.plugins."
        m = importlib.import_module(toImp + module)
        toSave = m.output(state, info)
        open(location, 'w').write(toSave)

"""
if __name__ == "__main__":
    output = Outputer()
    output.getAvailable()
"""
