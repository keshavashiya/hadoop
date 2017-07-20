#!/usr/bin/env python
import sys

current_word = None
current_count = 0

dic={}

for line in sys.stdin:

    line = line.strip()

    word,count = line.split('==')
    if word in dic.keys():
       dic[word]=int(dic[word])+1
    else:
       dic[word]=count

print dic
      
      
      
