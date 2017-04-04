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


#%% Find Titles
page = []
seite = []
liste = []
fuss = []

listnumbers = []
top = re.findall("div style.*top:([0-9]+)px.", myfile5)
left = re.findall("div style.*left:([0-9]+)px.", myfile5)
titles = []
for i,n in enumerate(data_correct):
    
    if n.startswith('Page'):
        page.append(n)
        data_correct[i] = ''
    if n.startswith('Seite'):
        seite.append(n)
        data_correct[i] = '' 
    if n.startswith('Gebur'):
        liste.append(n)
        data_correct[i] = ''  
    m = re.findall("^(\d\))", n)
    if m:
        fuss.append(n)
        data_correct[i] = ''  
        
    if re.search("(^([A-Z]{3,}( [0-9]+)*(.*%)*)(.*[A-Z]+)*)",n): 
        if re.search("([A-Z]{3,}.*) (([A-Z]+))",n):
            p = re.search("([A-Z]{3,}.*) (([A-Z]+))",n)
            titles.append(p.group(1))
            titles.append(p.group(2))
            data_correct[i] = '' 
        else:
            titles.append(n)       
            #data_correct.remove(n)           
#%%
(''') 
page = []
seite = []
liste = []
fuss = []
for i,n in enumerate(data_correct): 
    if n.startswith('Page'):
        page.append(n)
        data_correct[i] = []  
    if n.startswith('Seite'):
        seite.append(n)
        data_correct[i] = []  
    if n.startswith('Gebur'):
        liste.append(n)
        data_correct[i] = []  
    m = re.findall("^(\d\))", n)
    if m:
        fuss.append(n)
        data_correct[i] = []  
(''')        
for n in titles:
    while n in data_correct: data_correct.remove(n)   

#%% Compare titles with needed titles
bigdic = {}
titles_needed = ['(GEBURTEN [0-9]+)','NAME','STRASSE','ORT']
s = " ".join(titles)
for n in titles_needed:
    if re.search(n,s):
        p = re.findall(n,s)
        for m in p:
            bigdic[m] = 0
                  
#%%
liste1= 'https://de.wikipedia.org/wiki/Liste_der_St%C3%A4dte_in_Deutschland' 
with urllib.request.urlopen(liste1) as response:
    html_staedte = response.read()
    html_staedte = html_staedte.decode("utf-8") 
staedte = re.findall('title="(.*)"',html_staedte)
#%%
#print(any(x in a for x in b))
#any([True for e in (1, 2) if e in a])

#orte = re.findall('<br>([A-Z][a-z]+)\n<br>', myfile5)


orte = []
strassen = []
krankenhaus = []
for i,n in enumerate(data_correct):
    if re.findall('.*% (.*)',n):
        krankenhaus.append(re.findall('.*% (.*)',n))
        data_correct[i] = '' 
#%%                   
for i,n in enumerate(data_correct):                    
    if re.findall('(.*. [0-9]*)',n) and not re.findall('.*% (.*)',n):
        strassen.append(re.findall('(.*. [0-9]*)',n))
        #data_correct[i] = '' 
    
    #if n in staedte:
     #   orte.append(n)
    t = n.split()
    orte.append([e for e in t if e in staedte])
    #data_correct.remove(n)
    #orte.append(re.findall('^([A-Z][a-z]+)',n))
#%%    
def checkforsequence(data):  
    for n in data:
        if data_correct[i].isdigit() and data_correct[i+1].isdigit() and data_correct[i+2].isdigit():
            dif =  abs(data_correct[i] - data_correct[i+1])
            listnumbers.append(n) 

#%%
                
listnumbers = []
for i,n in enumerate(data_correct):
    if data_correct[i].isdigit():
        listnumbers.append(n)

#%%

diffs = []
for n in range(len(listnumbers)):
    diffs.append(abs(n-int(listnumbers[n])))
    
most_common,num_most_common = Counter(diffs).most_common(1)[0]

#%% Finde Strassen mit Haus Nr
(''')
name = ["A1B1", "djdd", "B2C4", "C2H2", "jdoi","1A4V"]
namenew = []
# Match names.
for element in name:
     m = re.findall("(^[A-Z]\d[A-Z]\d)", element)
     if m:
        print(m)
        namenew.append(element)
     else:
         print('no match')
