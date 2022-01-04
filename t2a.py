#!/usr/bin/env python
"""
Written by Vance Green
Please do not redistribute or use any code from this program in a non FOSS way without my concent.

This program is licenced under GPL 3.0 or later. Check the LICENCE file for the full licence.
"""
import sys
import os
import json
#Gets terminal size for text wrap calculations
width=os.get_terminal_size()[0]
def help():
    print("""
    Text To Ascii
    This program converts text inputted via -t into big, asciiart text. Below are all of the options
    -h --help - Displays this message
    -f --font - Specifies which font file to load from the same directory the program is in (default is big)
    -t --text - The text to display
    """)
    exit()
string=""
font="big"
#If there are not any options, display help and exit
if 1<len(sys.argv):
    #Series of if statements checking whether a certain argument is passed
   for i in range(len(sys.argv)):
        if sys.argv[i]=="-h" or sys.argv[i]=="--help":
            help()
        elif sys.argv[i]=="-f" or sys.argv[i]=="--font":
            font=sys.argv[i+1]
            i=i+1
        elif sys.argv[i]=="-t" or sys.argv[i]=="--text":
            optionTriggered=True
            string=sys.argv[i+1]
            i=i+1
else:
	help()

#Checks whether the string variable has any text
if string=="":
    print("You need to pass some text to display!")

#Attempt to open the font file. If reading the file fails, display an error message and exit
try:
    fontFile=open(font+".fnt",'r').read().replace("\@","")
except:
    print("INVALID FONT(font file either does not exist or is not readable)")
    exit()
fontLines=fontFile.split("\n")

i=0
jsonData=""
#Load the json data at the beginning of the file telling the program which character is on which line.
while not fontLines[i]=="BEGIN":
    try:
        jsonData+=fontLines[i]
        i+=1
    except:
        print("It would appear this font is invalid, please enter a valid font.")

#Parse json data into a readable list
fontRef=json.loads(jsonData)
font={}
values=list(fontRef.values())
keys=list(fontRef.keys())

#Load font into memory by iterating over every character and checking its place, then loading the next 6 lines into the list containing the font
for i in range(len(fontRef)):
    tmp2=values[i]
    tmp=[]
    for j in range(6):
        tmp.append(fontLines[tmp2+j-1])
    font[keys[i]]=tmp
dispcache,display=[[],[]]

#Load in the relivent characters in the order they will be used in, as well as processing word wrap
i=0
for j in range(len(string)):
    if i+len(font[string[j]][0])<=width:
        dispcache.append(string[j])
        i+=len(font[string[j]][0])
    else:
        display.append(dispcache)
        dispcache=[string[j]]
        i=len(font[string[j]][0])
#This almost certainly will never be triggered but is here in case it is
if dispcache!=[]:
	display.append(dispcache)

#Iterating over every line and displaying that line of each character(it repeats the process over every big line as well)
for k in display:
	for i in range(6):
		for j in k:
			print(font[j][i],end="")
		print()
	print()
