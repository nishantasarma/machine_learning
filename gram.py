def add_0s(str,n):
	m = 0
	length = len(str)
	k = length+1
	r  = length % n
	if r is not 0:
		for i in range (1,n):
			z = length + i
			if z%n == 0:
				m = i
				break
		for i in range(0,m):
			str = str+'0'
	return str

def get_engram(str,n):
	gram_list = []
	length1 = len(str)
	no_of_engrams = length1/n
	str_engram = '' 
	for j in range(0,n):

		str_engram = str_engram + str[j]

	gram_list.append(str_engram)

	for i in range(0,no_of_engrams-1):
		str_engram = ''
		c = (i+1)*n
		for j in range(c,c+n):

				str_engram=str_engram + str[j]

		gram_list.append(str_engram)


	return gram_list

