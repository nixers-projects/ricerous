import json

my_file = open("pad_info",'r').readlines()

section    = -1
category   = -1
sections   = []
categories = []
dico       = {}
tmp_dico   = {}
output     = ""
first_time = True

for line in my_file:
    if line.startswith("!!!"):
        sections.append(line.replace("!!!","").rstrip())

#print len(sections)

for line in my_file:
    if line.startswith("##"):
        categories.append(line.replace("##","").rstrip())

#print len(categories)

for i in range(len(my_file)):
    if my_file[i].startswith("!!!"):
        #we fill the previous section
        if section != -1:
            dico[sections[section]] = tmp_dico
        section   += 1
        tmp_dico   = {}
        first_time = True

        #print "---NEW SECTION---"
        #print sections[section]
        #print "-----------------"

    elif my_file[i].startswith("##"):
        #we fill the previous category
        if category != -1 and not first_time:
            tmp_dico[categories[category]] = output
            #print categories[category]
        category += 1
        first_time = False
        output    = ""
    else:
        output += my_file[i].replace('"','\"')
        if i+1 != len(my_file) and my_file[i+1].startswith("!!!"):
            tmp_dico[categories[category]] = output
            #print categories[category]
            output    = ""
        elif i+1 == len(my_file):
            tmp_dico[categories[category]] = output
            #print categories[category]
            dico[sections[section]] = tmp_dico



print json.JSONEncoder().encode(dico)
    

