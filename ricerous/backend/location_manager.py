# -*- coding: utf-8 -*-

import os
import shutil
from pkg_resources import resource_filename

"""
The purpose of this file is to manage the location of the info.json
"""

DEFAULT_CONFIG_LOCATION = resource_filename("ricerous", "json/info.json")
DEFAULT_VERSION_LOCATION = resource_filename("ricerous", "json/version")

PER_USER_LOCATION = os.environ["HOME"]+"/.config/ricerous"
VERSION = PER_USER_LOCATION + "/version"
INFO = PER_USER_LOCATION + "/info.json"

if not os.path.exists(PER_USER_LOCATION):
    os.mkdir(PER_USER_LOCATION)
    shutil.copyfile(DEFAULT_CONFIG_LOCATION, INFO)
    print "copying " + DEFAULT_CONFIG_LOCATION + " to "+ VERSION
    shutil.copyfile(DEFAULT_VERSION_LOCATION ,VERSION)
