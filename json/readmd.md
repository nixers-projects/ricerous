# JSON
This directory contains the JSON formatted data used by Ricerous. Here's a quick run down over which does.

## conf.json
The personal config file.

## info.json & info_to_json.py & pad_info
The python script generates the  ```info.json``` file from the markdown ```pad_info``` file during development.

## version
This is a version tag which checks for new versions of the info.json file. The tag has the following format

    YYYYMMDDXX

    Y: year
    M: month
    D: day
    X: extra

For example, the first update to the list on the 27th of September 2014 would have the tag ```2014092700```, the second update would have the tag ```2014092701``` and so on.