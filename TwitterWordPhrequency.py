#!/usr/bin/env python3

import twitfunctions as twit
import datetime as dt
import pandas as pd
import json
import sys
import re
import os


if len(sys.argv) != 2:
    raise ValueError('Please enter a twitter handle to analyze')

# Grab target information from file OR from Twitter if new
target = sys.argv[1]
try:
    with open(f'{target}.json', 'r') as target_file:
        target_json = json.load(target_file)
    target_file.close()
    target_json = json.dumps(target_json, indent=4)
except IOError:
    target_dict = twit.getUserInfobyName(target)
    target_json = json.dumps(target_dict, indent=4)
    with open(f'{target}.json', 'w') as target_file:
        json.dump(target_dict, target_file)
    target_file.close()

target_name = target_dict['name']
target_id = target_dict['id']


# Grab timeline from file OR Twitter if new
count = 200
try: 
    with open(f'{target}_timeline.txt', 'r') as timeline_file:
        timeline_json = json.load(timeline_file)
    timeline_file.close()
    timeline_json = json.dumps(timeline_json, indent=4)
except IOError:
    target_timeline_dict = twit.getUserTimeline(target, count)
    timeline_json = json.dumps(target_timeline_dict, indent=4)
    with open(f'{target}_timeline.txt' 'w') as timeline_file:
        json.dump(target_timeline_dict, timeline_file)
    timeline_file.close()


word_dict = {}
rt_list = []
hashtags = []

for id in target_timeline_dict:
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
