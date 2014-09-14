
def getName():
    return "bbcode"

def output(state,information):
    categories = information.listCategories()
    selections = state.selected
    toSave     = ""
    firstOne   = True
    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection] :
                    found += 1
                    if found == 1:
                        if not firstOne:
                            toSave += "[/list]\n"
                        toSave += "\n[size=9]" + category + "[/size]\n[list]\n\n"
                        firstOne = False
                    toSave += "[*][size=5]"+ selection+"[/size]\n"
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines :
                        toSave += "    "+line+"\n"
    toSave += "[/list]"+"\n"
    return toSave

