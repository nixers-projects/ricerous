# JSON
This directory contains the JSON formatted data used by Ricerous. Here's a quick run down over which does.

## conf.json
The personal config file.

## info.json & associated
This file contains all the ricing date read by the program. It has several file associated with it to ensure that it can be updated smoothly.

### pad_info
This markdown document is the base for all the info. If you wish to make changes to the displayed information, make them in this file.

### info_to_json.py
After making changes, run this script. This will update the JSON file and correct it's formatting using Vim. See the file header for futher usage information.

### version
This is the version date-tag for the JSON file, used by the program to determin if a newer version is available for download. It is incremented automatically by the python script.
