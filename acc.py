import re

f1 = open('result')
f2 = open('test')
txt_arr1 = []

txt1 = f1.read()
txt1 = re.sub("\n"," ",txt1).strip()

txt_arr1 = txt1.split(" ") 

txt2 =f2.read()
txt_arr2 = []


txt2 = re.sub("\n"," ",txt2).strip()

txt_arr2 = txt2.split(" ") 

length = len(txt_arr1)
print len(txt_arr2)
count = 0
for i in range(0, length):

	if txt_arr1[i] == txt_arr2[i]:

		count+=1
		
acc = 0

acc = (count*100)/length

print acc
