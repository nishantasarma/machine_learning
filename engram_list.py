import operator
import gram
import get_content
import os
def ngram_dic():
	
	texts = get_content.get_text()   
	
	words = texts.split(" ")
	str = ' '
	for word in words:
		str=str+word
		str = gram.add_0s(str,3)
	gram_list=gram.get_engram(str,3)
	d = {}
	for word in gram_list:
		d[word] = 0

	for word in gram_list:		
		d[word] = d[word]+1

	l = sorted(d.values(),reverse=True) #key=operator.itemgetter(1)

	arr = []
	dic= {}

	for i in range (0,1000):		
		arr.append(l[i])

	
	

	for value in arr:	
		for key in d.keys():
			if d[key] == value:
				dic[key] = value

	return dic


