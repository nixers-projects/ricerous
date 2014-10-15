
def getName():
    return "markdown"


def output(state, information):
    categories = information.listCategories()
    selections = state.selected
    toSave = ""

    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection]:
                    found += 1
                    if found == 1:
                        toSave += "\n#" + category + "\n\n"
                    toSave += "* " + selection + "\n"
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines:
                        toSave += "    " + line + "\n"
    return toSave
