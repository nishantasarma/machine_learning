import dataset
from sklearn.model_selection import train_test_split
from sklearn import svm
import os

x = dataset.x_set()
y = dataset.y_set()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
clf = svm.SVC()
clf.fit(x_train, y_train)
res = clf.predict(x_test)
result = ''
test = ''
for data in res:
	result += str(data)+"\n"
 
for data in y_test:
	test += str(data)+"\n"

f2 = open('result', 'w')
f2.write(result)
f1 = open('test', 'w')
f1.write(test)
f3 = open('accuracy', 'w')
f3.write(acc)

