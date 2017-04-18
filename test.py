import os
import get_content 
import gram
import engram_list

map = get_content.lang_map()
text = get_content.get_text()
words= text.split(" ")
x = []
ngram = engram_list.ngram_dic()
word_arr = [] 

for i,word in enumerate(words):
	word_arr.append(word)

print word_arr
