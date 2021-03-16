#! /usr/bin/env python3
import os
import requests

scr = '/data/feedback/'
keys = ['title', 'name', 'date', 'feedback']

for files in os.listdir(src):
  dict = {'title':' ', 'name':' ', 'date':' ', 'feedback':' '}
  with open(src + files, 'r') as text:
    i = 0
    for x in text:
      dict[keys[i]] = x.rstrip('\n')
      i = i + 1
  print(dict)
  response = requests.post('http://<external IP>/feedback/', json=dict)
  print('Response', response.status_code)
  text.close()
