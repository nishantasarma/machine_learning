import os
import re
import get_content 
import gram
import engram_list
def x_set():
	map = get_content.lang_map()
	text = get_content.get_text()
	words= text.split(" ")
	x = []
	ngram = engram_list.ngram_dic()
	word_arr = [] 

	for i,word in enumerate(words):
		word_arr.append(word)

	length = len(word_arr)-1


	for j, word in enumerate(word_arr):
		stri = ' '	
		stri = word_arr[j]
		stri = gram.add_0s(stri,3)
		ngrams = gram.get_engram(stri,3)
		if j==0:		
			x.append([0])
			next = word_arr[j+1]
			next = map[next]	
			x[j].append(next)
			for engram in ngram:
				if engram in ngrams:
					x[j].append(1)
				else:
					x[j].append(0)	

		elif j==length:
			prev = word_arr[j-1]
			prev = map[prev]	
			x.append([prev])
			x[j].append(length+2)
			for engram in ngram:
				if engram in ngrams:
					x[j].append(1)
				else:
					x[j].append(0)	

		else:
			next = word_arr[j+1]
			next = map[next]
			prev = word_arr[j-1]
			prev = map[prev]
	
			x.append([prev])
			x[j].append(next)
	
			for engram in ngram:
				if engram in ngrams:
					x[j].append(1)
				else:
					x[j].append(0)	

	return x

def y_set():

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
	lang0 = {}
	lang1 = {}
	lang2 = {}
	for word in text0:
		lang0[word] = 1
	for word in text1:
		lang1[word] = 1
	for word in text2:
		lang2[word] = 1
	
	text = get_content.get_text()
	words= text.split(" ")


	for i,word in enumerate(words):

		if word in lang0:
			y.append(0)
			
		elif word in lang1:
			y.append(1)
		
		else:
			y.append(2)

	return y



