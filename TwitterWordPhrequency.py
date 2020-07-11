#!/usr/bin/env python3

import twitfunctions as twit
import datetime as dt
import pandas as pd
import json
import sys
import re
import nltk
import os
from os import path


if len(sys.argv) != 2:
    raise ValueError('Please enter a twitter handle to analyze')

count = 200

# Grab target information
target = sys.argv[1]
try:
    with open(f'{target}.json', 'r') as timeline_file:
        timeline_json = json.load(timeline_file)
    timeline_file.close()
    timeline_json = json.dumps(timeline_json, indent=4)
except IOError:
    # Grab the latest sample of the target timeline
    target_dict = twit.getUserInfobyName(target)
    target_name = target_dict['name']
    target_id = target_dict['id']
    target_timeline = twit.getUserTimeline(target, count)

word_dict = {}
rt_list = []
hashtags = []

for id in target_timeline:
    if id['text'].startswith('RT'):
        rt_list.append(id['text'])
        pass
    
    curr_string = id['text'].split()
    for word in curr_string:
        if word.startswith('#'):
            hashtags.append(word)
        if word not in word_dict:
            word_dict[word] = 1
            print(f'{word}: {word_dict[word]}')
        else:
            cnt = word_dict.get(word)
            word_dict[word] += 1
            print(f'{word}: {word_dict[word]}')

for rt in rt_list:
    print(rt)
print(hashtags)

# print(f'{target_name} {target_id} {last_status}')
# print(f'{target["status"]["id"]}')
