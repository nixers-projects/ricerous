
def getName():
    return "latex"

def output(state,information):
    categories = information.listCategories()
    selections = state.selected
    toSave     = """\\documentclass{article}
\\title{Ricing Information}
\\date{\\today}
\\author{Your Name}
\\begin{document}
\\maketitle
"""
    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection] :
                    found += 1
                    if found == 1:
                        toSave += "\n\\section{" + category + "}\n\n"
                    toSave += "\\subsection{"+ selection+"}\n"
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines :
                        toSave += line+"\n"

    return toSave+"\n\\end{document}"
