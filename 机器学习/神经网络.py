import math
import random
import csv
import numpy as np
trainfile = './CarEvaluateTrain.csv'
testfile = './CarEvaluateTest.csv'
printfile = './msubmission.csv'
traindata = []
testdata = []
input_n = 0
hidden_n = 0
output_n = 0
input_cells = []
hidden_cells = []
output_cells = []
input_weights = []
output_weights = []
input_correction = []
output_correction = []


# def trtype(s):#评价转换为数字
#     types = {'acc':0,'unacc':1,'good':2,'vgood':3}
#     return types[s]

def initdata(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
        return data

def convertdata(i,data):
    outcome = []
    buying_price = {'low':0.25,'med':0.5,'high':0.75,'vhigh':1}
    maintenance_cost = {'low':0.25,'med':0.5,'high':0.75,'vhigh':1}
    number_doors = {'2':0.25,'3':0.5,'4':0.75,'5more':1}
    number_persons = {'2':1/3,'4':2/3,'more':1}
    lug_boot = {'small':1/3,'med':2/3,'big':1}
    safety = {'low':1/3,'med':2/3,'high':1}
    outcome.append(buying_price[data[i][0]])
    outcome.append(maintenance_cost[data[i][1]])
    outcome.append(number_doors[data[i][2]])
    outcome.append(number_persons[data[i][3]])
    outcome.append(lug_boot[data[i][4]])
    outcome.append(safety[data[i][5]])
    # print(outcome)
    return outcome

def convertoutcome(i,data):
    dict = {'acc':[0.25],'unacc':[0.5],'good':[0.75],'vgood':[1]}
    inx = dict[data[i][6]]
    #print(inx)
    return inx

def make_matrix(m, n, fill=0.0):#矩阵生成函数
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat

def rand(a, b):#随机数函数
    return (b - a) * random.random() + a

def sigmoid(x):#激活函数
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(x):#激活函数求导
    return x * (1 - x)
# def train():

def setup():
    global traindata
    global testdata
    global input_n
    global hidden_n
    global output_n
    global input_cells
    global hidden_cells
    global output_cells
    global input_weights
    global output_weights
    global input_correction
    global output_correction

    #初始化输入、隐层、输出元数
    input_n = 6+1
    hidden_n = 6
    output_n = 1
    #初始化神经元
    input_cells = [1.0] * input_n
    hidden_cells = [1.0] * hidden_n
    output_cells = [1.0] * output_n
    #初始化权重矩阵
    input_weights = make_matrix(input_n,hidden_n)
    output_weights = make_matrix(hidden_n,output_n)
    #初始化权重
    for i in range(input_n):
        for h in range(hidden_n):
            input_weights[i][h] = rand(-0.2,0.2)
    for h in range(hidden_n):
        for o in range(output_n):
            output_weights[h][o] = rand(-2.0,2.0)
    #初始化偏置
    input_correction = make_matrix(input_n,hidden_n)
    output_correction = make_matrix(hidden_n,output_n)

def predict(inputs):
    global traindata
    global testdata
    global input_n
    global hidden_n
    global output_n
    global input_cells
    global hidden_cells
    global output_cells
    global input_weights
    global output_weights
    global input_correction
    global output_correction
    #激活输入层
    for i in range(input_n - 1):#第7个输入节点的值始终为1.0
        input_cells[i] = inputs[i]
    #激活隐藏层
    for j in range(hidden_n):
        total = 0.0
        for i in range(input_n):
            total += input_cells[i] * input_weights[i][j]
        hidden_cells[j] = sigmoid(total)
    #激活输出层
    for k in range(output_n):
        total = 0.0
        for j in range(hidden_n):
            total += hidden_cells[j] * output_weights[j][k]
        output_cells[k] = sigmoid(total)
    return output_cells[:]

def back_propagate(case,label,learn):
    global traindata
    global testdata
    global input_n
    global hidden_n
    global output_n
    global input_cells
    global hidden_cells
    global output_cells
    global input_weights
    global output_weights
    global input_correction
    global output_correction
    #先预测
    predict(case)
    #求输出误差
    output_deltas = [0.0] * output_n
    l1 = 0#正则化项
    for i in range(hidden_n):
        for j in range(output_n):
            l1 +=math.abs(output_weights[i][j])

    for i in range(output_n):
        error = label[i] - output_cells[i] + l1
        output_deltas[i] = sigmoid_derivative(output_cells[i]) * error
    #求隐层误差
    hidden_deltas = [0.0] * hidden_n
    l1 = 0#正则化项
    for i in range(input_n):
        for j in range(hidden_n):
            l1 += math.abs(input_weights[i][j])

    for h in range(hidden_n):
        error = l1
        for i in range (output_n):
            error += output_deltas[i] * output_weights[h][i]
        hidden_deltas[h] = sigmoid_derivative(hidden_cells[h]) * error
    #更新输出权重
    for h in range(hidden_n):
        for o in range(output_n):
            change = output_deltas[o] * hidden_cells[h]#相对输入*相对输出的误差*学习率
            output_weights[h][o] += learn * change
    #更新输入权重
    for i in range(input_n):
        for h in range(hidden_n):
            change = hidden_deltas[h] * input_cells[i]
            input_weights[i][h] += learn * change

def train(limit = 100,learn = 0.05):
    global traindata
    global testdata
    global input_n
    global hidden_n
    global output_n
    global input_cells
    global hidden_cells
    global output_cells
    global input_weights
    global output_weights
    global input_correction
    global output_correction
    for j in range(limit):
        #print(j)
        for i in range(1,1211):
            case = convertdata(i,traindata)
            label = convertoutcome(i,traindata)
            back_propagate(case,label,learn)

def fit(file):
    w = ['acc','unacc','good','vgood']
    with open(file,"w",newline="") as f:
        writer = csv.writer(f)
        for i in range(1,519):
            case = convertdata(i,testdata)
            outcome = predict(case)#得到一个0~1之间的数
            array = [0,0,0,0]
            array[0] = abs(outcome[0] - 0.25)
            array[1] = abs(outcome[0] - 0.5)
            array[2] = abs(outcome[0] - 0.75)
            array[3] = abs(outcome[0] - 1)
            print(outcome[0])
            tmp = 1000000
            ans = 10
            for i in range(4):
                if(array[i] < tmp):
                    tmp = array[i]
                    ans = i
            writer.writerow([w[ans]])





if __name__ == '__main__':
    traindata = initdata(trainfile)
    testdata = initdata(testfile)
    setup()
    train(100,0.05)
    fit(printfile)