import csv
import sklearn
from dataloader import *
data_train=read(filename,7,1211)
test_data=read("./CarEvaluateTest.csv",6,519)
out=["unacc","acc","good","vgood"]
x=[]
result=open('bsubmission.csv','w', newline='')
for i in range(0,1210):
	m=[]
	for j in range(0,6):
		m.append(data_train[j][i])
	x.append(m)
y=data_train[6]
clr=svm.SVC()
clr.fit(x,y)
writer=csv.writer(result)
for i in range(0,518):
	m=[]
	for j in range(0,6):
		m.append(test_data[j][i])
	oo=clr.predict([m])
	writer.writerow([out[oo[0]]])
	print(out[oo[0]])
