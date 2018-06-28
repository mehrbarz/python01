#!/usr/bin/env python3

import os
import sys
import json

os.system("sh test-cloud-vision.sh")

f= open('response.json')
data = json.load(f)
f.close()

for(k,v) in data.items():
    print("key: " + k)
    print("value: " +str(v))

"""
def getBox(k , v):
    if 'Box' in k:
        value = str(v)
        return value
"""

