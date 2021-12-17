import sys
import os
width=os.get_terminal_size()[0]

if 1<len(sys.argv):
	 string=sys.argv[1]
else:
	print("NO ARGUMENTS PASSED")
	exit()
cachedChars=[]
charCache={}
for i in string:
	if not i in cachedChars:
		try:
			cachedChars.append(i)
			charCache[i]=open(f'assets/{i}.txt', 'r').read().split("\n")
		except:
			print("Sorry, but a filesysem error occurred(most likely that character isnt in /toilet2/assets, so if you want you can just make asciiart of it and put it in there as {character}.txt)")
			print(f'\nNONEXISTANT FILE ERROR: FILE {i}.txt DOES NOT EXIST IN /toilet2/assets')
			exit(1)
dispcache,display=[[],[]]
i=0
for j in range(len(string)):
	if i+len(charCache[string[j]][0])<width:
		dispcache.append(string[j])
		i+=len(charCache[string[j]][0])
	else:
		display.append(dispcache)
		dispcache=[]
		i=0
if dispcache!=[]:
	display.append(dispcache)
for k in display:
	for i in range(6):
		for j in k:
			print(charCache[j][i],end="")
		print()
	print()