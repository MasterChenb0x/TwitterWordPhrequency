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

target = sys.argv[1]

# Grab target information from file OR from Twitter if new
try:
    with open(f'{target}.json', 'r') as target_file:
        target_dict = json.load(target_file)
    target_file.close()
    target_json = json.dumps(target_dict, indent=4)
except EnvironmentError:
    target_dict = twit.getUserInfobyName(target)
    target_json = json.dumps(target_dict, indent=4)
    with open(f'{target}.json', 'w') as target_file:
        json.dump(target_dict, target_file)
    target_file.close()


# Grab timeline from file OR Twitter if new
count = 200
try: 
    with open(f'{target}_timeline.json', 'r') as timeline_file:
        target_timeline_dict = json.load(timeline_file)
    timeline_file.close()
    timeline_json = json.dumps(target_timeline_dict, indent=4)
except EnvironmentError:
    target_timeline_dict = twit.getUserTimeline(target, count)
    timeline_json = json.dumps(target_timeline_dict, indent=4)
    with open(f'{target}_timeline.json', 'w') as timeline_file:
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
            word_dict[word] += 1
            print(f'{word}: {word_dict[word]}')

sort_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
for i in sort_words:
    print(i[0], i[1])


for rt in rt_list:
    print(rt)
print(hashtags)

