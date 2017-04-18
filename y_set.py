
import os
import re
import get_content 
y = []
lang_arr = [] 

dir = '/home/nishanta/Desktop/machine_learning/'


for file in os.listdir(dir):
	f = open(dir+file)	
	text = f.read()
	lang_arr.append(text.splitlines())		

len0 = len(lang_arr[0])
len1 = len(lang_arr[1])
len2 = len(lang_arr[2])

text0 = ''
text1 = ''
text2 = ''

for sentence in lang_arr[0]:
	text0+=sentence+" "
for sentence in lang_arr[1]:
	text1+=sentence+" "
for sentence in lang_arr[2]:
	text2+=sentence+" "



text0 = re.sub(' +',' ',text0).strip().split(" ")
text1 = re.sub(' +',' ',text1).strip().split(" ")
text2 = re.sub(' +',' ',text2).strip().split(" ")

lang_arr[0] = text0
lang_arr[1] = text1
lang_arr[2] = text2

	
text = get_content.get_text()
words= text.split(" ")


for i,word in enumerate(words):

	if word in lang_arr[0]:
		y.append([1])
		y[i].append(0)
		y[i].append(0)
	elif word in lang_arr[1]:
		y.append([0])
		y[i].append(1)
		y[i].append(0)
	else:
		y.append([0])
		y[i].append(0)
		y[i].append(1)

print y



