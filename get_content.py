import os
import re

def get_text():
	
	lang_arr = [] 

	dir = '/home/nishanta/Desktop/machine_learning/'


	for file in os.listdir(dir):
		f = open(dir+file)	
		text = f.read()
		lang_arr.append(text.splitlines())		
	
	len0 = len(lang_arr[0])
	len1 = len(lang_arr[1])
	len2 = len(lang_arr[2])
	smallest = ' '

	if len0 <= len1 and len0 <= len2 :
		smallest = 'len0'
	elif len1 <= len0 and len1 <= len2 : 
		smallest = 'len1'
	else:						
		smallest = 'len2'	

	texts = ''

	if smallest == 'len0':

	
		for i,sentence in enumerate(lang_arr[0]):
	
					texts+= lang_arr[0][i]+" "+lang_arr[1][i]+" "+lang_arr[2][i]

	elif smallest == len1:

		for i,sentence in enumerate(lang_arr[1]):
	
					texts+= lang_arr[0][i]+" "+lang_arr[1][i]+" "+lang_arr[2][i]
	else:

		for i,sentence in enumerate(lang_arr[2]):
	
					texts+= lang_arr[0][i]+" "+lang_arr[1][i]+" "+lang_arr[2][i]



	texts = re.sub(' +',' ',texts)


	return texts


def lang_map():
	text = get_text()
	words = text.split()
	d = {}
	for id,word in enumerate(words,1):
		d[word] = id	

	return d





