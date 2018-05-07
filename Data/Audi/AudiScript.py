#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:29:04 2018

@author: dsakosky
"""

# Get file contents
fd = open('Audi.txt')
contents = fd.readlines()
fd.close()

new_contents = []

# Get rid of empty lines
for line in contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_contents.append(line)

###########

import re

city_state = []
# Get rid of empty lines
for line in new_contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if re.match('\d\.+', line) is None: 
        continue
    # We got something, save it
    else:
        city_state.append(line)
########
        
######## Write to csv
with open('outfile.csv', 'w') as f:
    for line in city_state:
        f.write(line)

##### Convert to dataframe and add headers
import pandas as pd
data = pd.read_csv('outfile.csv', header=None)
data.columns = ['city', 'state']


##### Get rid of original numbering...
data['city'] = data['city'].str.replace(r'\d\.','')
data.to_csv('AudiLocations.csv')


#########
#import csv
#
#mycsv = csv.writer(open('OutPut.csv', 'w')) # The code I used had "wb", changing this
## to just w fixed the error
##https://stackoverflow.com/questions/33054527/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-when-writing-t
#mycsv = mycsv.writerow(['city', 'state']) #This puts the headers on the csv file