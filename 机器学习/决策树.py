from typing import List

from sklearn.tree import DecisionTreeClassifier
import csv
traindata = []
testdata = []
_traindata = []
_testdata = []
buying_price = {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4}
maintenance_cost = {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4}
number_doors = {'2': 1, '3': 2, '4': 3, '5more': 4}
number_persons = {'2': 1, '4': 2, 'more': 3}
lug_boot = {'small': 1, 'med': 2, 'big': 3}
safety = {'low': 1, 'med': 2, 'high': 3}
trainfile = "./CarEvaluateTrain.csv"
testfile = "./CarEvaluateTest.csv"
subfile = "./submission.csv"
def trans(data,i) :
    array = []
    array.append(buying_price[data[i][0]])
    array.append(maintenance_cost[data[i][1]])
    array.append(number_doors[data[i][2]])
    array.append(number_persons[data[i][3]])
    array.append(lug_boot[data[i][4]])
    array.append(safety[data[i][5]])
    return array

def readdata():
    with open (trainfile,"r") as f:
        reader = csv.reader(f)
        rdata = [row for row in reader]
        print(rdata)
        for i in range(1,1211):
            traindata.append(trans(rdata,i))
            testdata.append(rdata[i][6])
        print(traindata)
        print(testdata)
        with open (testfile,"r") as _f:
            _reader = csv.reader(_f)
            _rdata = [row for row in _reader]
            for i in range (1,519):
                _traindata.append(trans(_rdata,i))
            print(_traindata)
            print(len(_traindata))

if __name__ == '__main__':
    readdata()
    make = DecisionTreeClassifier()
    make.fit(traindata,testdata)
    _testdata = make.predict(_traindata)
    print(_testdata)
    with open(subfile,"w",newline="") as f:
        writer = csv.writer(f)
        for i in range(len(_testdata)):
            writer.writerow([_testdata[i]])
    # array = trans(1)
    # print(array)


