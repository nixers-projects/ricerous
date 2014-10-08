# -*- coding: utf-8 -*-

import os
import shutil

"""
The purpose of this file is to manage the location of the info.json
"""


DEFAULT_CONFIG_LOCATION = "json/info.json"
PER_USER_LOCATION = os.environ["HOME"]+"/.config/ricerous"

if not os.path.exists(PER_USER_LOCATION):
    os.mkdir(PER_USER_LOCATION)
    shutil.copyfile(DEFAULT_CONFIG_LOCATION,PER_USER_LOCATION+"/info.json")


