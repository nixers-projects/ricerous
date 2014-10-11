#!/usr/bin/env python

"""
This script generates the JSON information file which is used by Ricerous.
If you wish to make any changes to the information displayed, please follow
these steps:

  1. Make desired changes to `info.md`
  2. Run this script (`python md_to_json.py`)

This script will then update your changes to `info.json`, correct its file
formatting using Vim, and then increment the version number meaning that
people can get your additions from the update manager.
"""

import json
from os import system
from datetime import datetime

my_file = open("info.md", 'r').readlines()

section = -1
category = -1
sections = []
categories = []
dico = {}
tmp_dico = {}
output = ""
first_time = True

for line in my_file:
    if line.startswith("!!!"):
        sections.append(line.replace("!!!", "").rstrip())

# print len(sections)

for line in my_file:
    if line.startswith("##"):
        categories.append(line.replace("##", "").rstrip())

# print len(categories)

for i in range(len(my_file)):
    if my_file[i].startswith("!!!"):
        # we fill the previous section
        if section != -1:
            dico[sections[section]] = tmp_dico
        section += 1
        tmp_dico = {}
        first_time = True

        # print "---NEW SECTION---"
        # print sections[section]
        # print "-----------------"

    elif my_file[i].startswith("##"):
        # we fill the previous category
        if category != -1 and not first_time:
            tmp_dico[categories[category]] = output
            # print categories[category]
        category += 1
        first_time = False
        output = ""
    else:
        output += my_file[i].replace('"', '\"')
        if i+1 != len(my_file) and my_file[i+1].startswith("!!!"):
            tmp_dico[categories[category]] = output
            # print categories[category]
            output = ""
        elif i+1 == len(my_file):
            tmp_dico[categories[category]] = output
            # print categories[category]
            dico[sections[section]] = tmp_dico


jsonFile = json.JSONEncoder().encode(dico)
infoFile = open('info.json', 'w').write(jsonFile)

version = open('version', 'r').read()
verDate = int(''.join(list(version)[0:8]))

nowDate = datetime.isoformat(datetime.now())
nowDate = int(nowDate.split("T")[0].replace("-", ""))

if verDate == nowDate:
    new_version = open('version', 'w').write(str(int(version) + 1))
else:
    new_version = open('version', 'w').write(str(nowDate) + "00")

# Corrects formatting using Vim
system('vim -c ":% !python -m json.tool" -c ":wq" info.json')
