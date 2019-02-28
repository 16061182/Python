import numpy as np
import csv
from keras.models import Sequential
from keras.layers import Dense, Dropout, Recurrent
train_data_x = []
train_data_y = []
test_data_x = []
test_data_y = []
b_p = {'low':0, 'med':1, 'high':2, 'vhigh':3}
m_c = {'low':0, 'med':1, 'high':2, 'vhigh':3}
n_d = {'2':2, '3':3, '4':4, '5more':5}
n_p = {'2':2, '3':3, '4':4, 'more':5}
l_b = {'small':0, 'med':1, 'big':2}
safety = {'low':0, 'med':1, 'high':2, 'vhigh':3}
decision = {'unacc':0, 'acc':1, 'good':2, 'vgood':3}
_decision = {0:'unacc', 1:'acc', 2:'good', 3:'vgood'}

def data_process():
    global train_data_x
    global train_data_y
    global test_data_x
    global test_data_y
    with open('CarEvaluateTrain.csv') as train_file:
        csv_reader = csv.reader(train_file)
        train_data = np.array([row for row in csv_reader])#二维列表，每一行是子列表
        row_num = 0
        for row in train_data:
            row_num = row_num + 1
            if row_num == 1:
                continue
            new_row = []
            new_row.append(b_p[row[0]])
            new_row.append(m_c[row[1]])
            new_row.append(n_d[row[2]])
            new_row.append(n_p[row[3]])
            new_row.append(l_b[row[4]])
            new_row.append(safety[row[5]])
            new_row_y = []
            new_row_y.append(decision[row[6]])
            train_data_x.append(new_row)
            train_data_y.append(new_row_y)
        train_data_x = np.array(train_data_x)
        train_data_y = np.array(train_data_y)
        print(train_data_x.shape)
        print(train_data_x)
        print(train_data_y.shape)
        print(train_data_y)
    with open('CarEvaluateTest.csv') as test_file:
        csv_reader = csv.reader(test_file)
        test_data = np.array([row for row in csv_reader])
        row_num = 0
        for row in test_data:
            row_num = row_num + 1
            if row_num == 1:
                continue
            new_row = []
            new_row.append(b_p[row[0]])
            new_row.append(m_c[row[1]])
            new_row.append(n_d[row[2]])
            new_row.append(n_p[row[3]])
            new_row.append(l_b[row[4]])
            new_row.append(safety[row[5]])
            test_data_x.append(new_row)
        test_data_x = np.array(test_data_x)
        print(test_data_x.shape)
        print(test_data_x)

if __name__ == '__main__':
    data_process()
    Model = Sequential()
    Model.add(Dense(50, input_shape=(6,), activation='relu'))
    Model.add(Dense(50, activation='relu'))
    Model.add(Dense(50, activation='relu'))
    Model.add(Dense(50, activation='relu'))
    Model.add(Dense(1))
    Model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
    Model.fit(train_data_x, train_data_y, epochs=500)
    for i in range(0,518):
        row = test_data_x[i].reshape(1,6,)
        test_data_y.append(Model.predict(row)[0])
    test_data_y = np.array(test_data_y)
    # print(test_data_y.shape)
    # print(test_data_y)
    with open('submission.csv','w',newline='') as output_file:
        csv_writer = csv.writer(output_file)
        for row in test_data_y:
            value = row[0]
            comp = []
            comp.append(abs(value-0))
            comp.append(abs(value-1))
            comp.append(abs(value-2))
            comp.append(abs(value-3))
            value = _decision[comp.index(min(comp))]
            csv_writer.writerow([value])
