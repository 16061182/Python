import csv
from sklearn import svm

filename='E:\\机器学习\\大作业\\train\\CarEvaluateTrain.csv'
data_train=[]
rate=[]
'''
读取文件得函数
'''
def read(filename,row,col):
	with open(filename,"r") as f:
		data=[]
		reader=csv.reader(f)
		column=[row for row in reader]
		for i in range(0,row):
			mid=[]
			rate.append([0.,0.,0.,0.])
			for jj in range(0,col):
				j=column[jj][i];
				if(j=="low" or j=="2" or j=="small" or j=="unacc"):
					mid.append(0)
					rate[i][0]+=1
				if(j=="med"  or j=="3" or j=="acc"):
					mid.append(1)
					rate[i][1]+=1
				if(j=="high" or j=="4" or j=="big" or j=="high" or j=="good"):
					mid.append(2)
					rate[i][2]+=1
				if(j=="5more" or j=="more" or j=="vhigh" or j=="vgood"):
					mid.append(3)
					rate[i][3]+=1
			#print(len(mid))
			data.append(mid)
	return data
if __name__=='__main__':
	data_train=read(filename,7,1211)
	num=[]
	accept=[0.,0.,0.,0.]
	#print(rate)
	for j in range(0,1210):
		accept[data_train[6][j]]+=1
	for j in range(0,4):
		accept[j]/=1214
	print(accept)
	for i in range(0,6):
		mid1=[[1.,1.,1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]
		for j in range(0,1210):
			#print(data_train[i][j])
			mid1[data_train[i][j]][data_train[6][j]]+=1
		#print(mid1[0][0]+mid1[0][1]+mid1[0][2]+mid1[0][3])
		num.append(mid1)
	for i in range(0,6):
		for j in range(0,4):
			for k in range(0,4):
				num[i][j][k]/=1214
				num[i][j][k]/=accept[k]

	test_data=read("E:\\机器学习\\大作业\\train\\CarEvaluateTest.csv",6,519)
	out=["unacc","acc","good","vgood"]
	x=[]
	result=open('submission.csv','w', newline='')
	for i in range(0,1210):
		m=[]
		for j in range(0,6):
			m.append(data_train[j][i])
		x.append(m)
	y=data_train[6]
	clr=svm.SVC()
	clr.fit(x,y)
	writer=csv.writer(result)
	'''for i in range(0,518):
		m=[]
		for j in range(0,4):
			s=1
			for k in range(0,6):
				s*=num[k][test_data[k][i]][j]
			m.append(s)
		oo=m.index(max(m))
		writer.writerow([out[oo]])'''
	for i in range(0,518):
		m=[]
		for j in range(0,6):
			m.append(test_data[j][i])
		oo=clr.predict([m])
		writer.writerow([out[oo[0]]])




