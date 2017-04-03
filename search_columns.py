#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:25:57 2017

@author: julio
"""
import urllib.request
from lxml import html
#import requests
import re
from itertools import groupby
from operator import itemgetter
import numpy
from collections import Counter
#from parse import *
#from urllib.parse import urlparse
#from urllib.parse import search

import os
cwd = os.getcwd()
file = 'file://'+cwd+'/myfile5.html'


myfile5 = urllib.request.urlopen(file).read()
myfile5 = myfile5.decode("utf-8") 

tree = html.fromstring(myfile5)
data = tree.xpath('(.|.//*[not(name()="script")][not(name()="style")])/text()')

data_correct=data[0:-1]
for i,n in enumerate(data_correct):
    if '\n' not in n:    
        data_correct[i] = data_correct[i] + ' ' + data_correct[i+1]
        #data_correct.append(n + data[data.index(n)+1])
        del data_correct[i+1]
while '\n' in data_correct: data_correct.remove('\n')   

for i,n in enumerate(data_correct):
    data_correct[i] = data_correct[i].strip()


#%% Find attributes
listnumbers = []
top = re.findall("div style.*top:([0-9]+)px.", myfile5)
left = re.findall("div style.*left:([0-9]+)px.", myfile5)
titles = []
for i,n in enumerate(data_correct): 
    if re.search("(^([A-Z]{3,}( [0-9]+)*(.*%)*)(.*[A-Z]+)*)",n): 
        if re.search("([A-Z]{3,}.*) (([A-Z]+))",n):
            p = re.search("([A-Z]{3,}.*) (([A-Z]+))",n)
            titles.append(p.group(1))
            titles.append(p.group(2))
        else:
            titles.append(n)       
        
    
#%%
bigdic = {}
titles_needed = ['RANG','(GEBURTEN [0-9]+)','NAME','STRASSE','ORT']
s = " ".join(titles)
for n in titles_needed:
    if re.search(n,s):
        p = re.findall(n,s)
        for m in p:
            bigdic[m] = 0

orte = []
for n in data_correct:
    orte.append(re.findall('^([A-Z][a-z]+)',n))
     
def checkforsequence(data):  
    for n in data:
        if data_correct[i].isdigit() and data_correct[i+1].isdigit() and data_correct[i+2].isdigit():
            dif =  abs(data_correct[i] - data_correct[i+1])
            listnumbers.append(n) 
                
listnumbers = []
for n in data_correct:
    listnumbers.append(data_correct[n].isdigit())

diffs = []
for n in range(len(listnumbers)):
    diffs.append(abs(n-int(listnumbers[n])))
    
most_common,num_most_common = Counter(diffs).most_common(1)[0]