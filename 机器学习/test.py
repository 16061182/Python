#https://blog.csdn.net/u011089523/article/details/52372962 python读取csv的某行
import csv
row = []
line1 = [1,2,3]
line2 = [1,2,3]
row.append(line1)
row.append(line2)
print(row)
print(row[1][2])
with open("./CarEvaluateTrain.csv","r") as f:#仅在这个语句块中f文件处于打开状态
    reader = csv.reader(f)
    print(reader)
    colomn = [a for a in reader]
a = 100
a/=1214
line1 = [0] * 4
line2 = []
traindata = []
for j in range(0, 6):
    line2.append(line1)
for j in range(0, 4):
    traindata.append(line2)
line1[0] = 2
# print(line2)
# print(traindata)
traindata = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
# print(traindata)
traindata[0][0][0] = 1
print(traindata)

print(a)