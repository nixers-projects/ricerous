def getName():
    return "html"


def output(state, information):
    categories = information.listCategories()
    selections = state.selected
    toSave = """
<html>
    <head>
    </head>
    <body>
\n
"""
    firstOne = True
    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection]:
                    found += 1
                    if found == 1:
                        if not firstOne:
                            toSave += "</ul>\n"
                        toSave += "<h2>" + category + "</h2>\n<ul>\n"
                        firstOne = False
                    toSave += "\n<li>\n<h3>" + selection + "</h3><br/>\n"
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines:
                        toSave += line + "<br/>\n"
                    toSave += "</li>\n"
    toSave += "</ul>\n"
    toSave += "</body>\n"
    toSave += "</html>\n"
    return toSave
