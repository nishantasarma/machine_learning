import get_content

def lang_map():
	text = get_content.get_text()
	words = text.split()
	d = {}
	for id,word in enumerate(words,1):
		d[word] = id	

	return d
