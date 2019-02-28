import csv
trainfile = "./CarEvaluateTrain.csv"
testfile = "./CarEvaluateTest.csv"
outcomefile = "./submission.csv"
sum = [0]*4#各种结果数量
traindata = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
def dealwithdata(file,row,colomn):
    a = 0
    with open(file,"r") as f:
        reader = csv.reader(f)
        matrix = [row for row in reader]
        for i in range (0,row):
            k = matrix[i][6]
            if(k == 'acc'):
                x = 0
                sum[0] += 1
            elif(k == 'unacc'):
                x = 1
                sum[1] += 1
            elif(k == 'good'):
                x = 2
                sum[2] += 1
            elif(k == 'vgood'):
                x = 3
                sum[3] += 1
            for j in range (0,colomn - 1):
                item = matrix[i][j]
                if(item == "low" or item == "2" or item == "small"):
                    traindata[x][j][0] += 1
                if (item == "med" or item == "3"):
                    traindata[x][j][1] += 1
                if (item == "high" or item == "4" or item == "big"):
                    traindata[x][j][2] += 1
                if(item == "vhigh" or item == "5more" or item == "more"):
                    traindata[x][j][3] += 1
        #print(sum)
        for i in range(0,4):
            for j in range(0,6):
                for k in range(0,4):
                    traindata[i][j][k] /= sum[i]

def predictdata(tfile,row,colomn,ofile):
    with open(tfile,"r") as tf:
        with open(ofile,"w",newline='') as of:
            reader = csv.reader(tf)
            matrix = [row for row in reader]
            print = ["acc","unacc","good","vgood"]
            for i in range (1,row):
                temp = [1,1,1,1]
                res = [0]*colomn
                for j in range (0,colomn):
                    item = matrix[i][j]
                    if (item == "low" or item == "2" or item == "small"):
                        num = 0
                    if (item == "med" or item == "3"):
                        num = 1
                    if (item == "high" or item == "4" or item == "big"):
                        num = 2
                    if (item == "vhigh" or item == "5more" or item == "more"):
                        num = 3
                    temp[0] *= traindata[0][j][num]
                    temp[1] *= traindata[1][j][num]
                    temp[2] *= traindata[2][j][num]
                    temp[3] *= traindata[3][j][num]
                s = print[temp.index(max(temp))]
                writer = csv.writer(of)
                writer.writerow([s])

if __name__ == '__main__':
    dealwithdata(trainfile,1211,7)
    predictdata(testfile,519,6,outcomefile)
    print(traindata)