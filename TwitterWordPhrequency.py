#!/usr/bin/env python3

import twitfunctions as twit
import datetime as dt
import json
import sys

if len(sys.argv) != 2:
    raise ValueError('Please enter a twitter handle to analyze')

# Grab target information
target = twit.getUserInfobyName(sys.argv[1])
target_name = target['name']
target_id = target['id']
last_status = target['status']['text']

# Grab the latest sample of the target timeline
count = 150
target_timeline = twit.getUserTimeline(sys.argv[1], count)

word_dict = {}

for id in target_timeline:
    curr_string = id['text'].split()
    for word in curr_string:
        if word not in word_dict:
            word_dict[word] = 1
            print(f'{word}: {word_dict[word]}')
        else:
            cnt = word_dict.get(word)
            word_dict[word] += 1
            print(f'{word}: {word_dict[word]}')

#print(f'{target_name} {target_id} {last_status}')
#print(f'{target["status"]["id"]}')
