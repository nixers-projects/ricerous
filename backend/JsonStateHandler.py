import json

"""
The Role of this file is to save the state to json or read the state from json
the state is a State object (State.py)
"""

"""
save :: String -> State -> Void
save the state in json format to a location specified
"""
def save(saveLocation,state):
    #save the comments and selected to a json file
    saveOutput  = "{\n"
    saveOutput += '"comments":\n'
    saveOutput += json.JSONEncoder().encode(state.comments)+"\n"
    saveOutput += ',"selections":\n'
    saveOutput += json.JSONEncoder().encode(state.selected)+"\n"
    saveOutput += "}\n"
    open(saveLocation,'w').write(saveOutput)

"""
load :: String -> State (by reference) -> Void
load the state from a json file into a State object
WARNING: this function will change the state
"""
def load(loadLocation, state):
    f              = open(loadLocation,'r')
    loaded         = json.load(f)
    f.close()
    state.comments = loaded['comments']
    state.selected = loaded['selections']

