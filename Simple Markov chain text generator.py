#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:50:50 2018

@author: david
"""
import random
f = open("Tennyson",'r')    #Sample file, any parsable text file should work, including this .py
interval = 4                #Play with this variable for interesting results
maxsentencelength = 1000    #Maximum output length in number of characters
markovdict = {}             
text = f.read()

#Make the dictionary
for i in range(interval,len(text)):
    cursec = text[i-interval:i]                 #Generate the next character for each section of length 'interval'
    if cursec not in markovdict:                
        markovdict[cursec] = [text[i]]          #Add it to the dictionary
    else:
        markovdict[cursec].append(text[i])      #The same character might be added multiple times, weighing it to be chosen more often during generation

#Generate a sentence from the dictionary
sentence = random.choice(list(markovdict.keys()))               #Start with a random section
while(True):
    lastpiece = sentence[len(sentence)-interval:len(sentence)]  #Select section of length interval from text
    if(lastpiece not in markovdict.keys()):                     #Generation might reach the end of the source text
        break
    newword = random.choice(markovdict[lastpiece])              #Choose randomly from possible successor characters
    sentence+=newword
    if len(sentence)>maxsentencelength:                         #Stop generating when sentence gets too long
        break

print(sentence)
