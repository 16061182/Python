#h-index, 按引用次数降序排列，满足 前n个引用次数不少于n 的n的最大值
#g-index, 按引用次数降序排列，满足 前n个引用的累计次数不少于n^2 的n的最大值

import numpy as np
init_data_file = './h-index down.txt'


def data_load(file):
    with open(file, 'r', encoding='UTF-8') as f:
        # reader = f.read()
        # print(reader,type(reader))
        data = []
        line = f.readline()
        while(line):
            data.append(line)
            print(line)
            line = f.readline()
        print(len(data))
        names = []
        values = []
        train_x = []
        train_y = []
        train_x_2 = []
        train_y_2 = []
        for i in range(998):
            value = data[2*i+1].split()
            _value = []
            for str in value:
                _value.append(int(str))
            if(len(_value) != 7):
                print('error',i)
            # 直观上_value[6]Activity对h-index影响不大
            _x = np.array(_value[0:2] + _value[3:6])
            _y = _value[2]
            if((_value[3] != 0) & (data[2 * i][0:-1] not in names)):
                # g-index为0应视为异常数据,num = 11
                # 去掉名字已经存在的数据,num = 23
                names.append(data[2 * i][0:-1])
                values.append(_value)
                train_x.append(_x)
                train_y.append(_y)
                # 精炼数据，取h-index不少于5
                if(_y >= 5):
                    train_x_2.append(_x)
                    train_y_2.append(_y)
        train_x = np.array(train_x)
        train_y = np.array(train_y)
        train_x_2 = np.array(train_x_2)
        train_y_2 = np.array(train_y_2)
        # print(train_x.shape)
        # print(train_y.shape)
        # print(train_x_2.shape)
        # print(train_y_2.shape)
        return train_x_2, train_y_2, train_x_2, train_y_2
        '''
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        root = 2
        #伪随机抽样20%的数据169个作为test集
        for i in range(847):
            if((i-2)%5 != 0):
                x_train.append(train_x_2[i])
                y_train.append(train_y_2[i])
                continue
            x_test.append(train_x_2[i])
            y_test.append(train_y_2[i])
        x_train = np.array(x_train); y_train = np.array(y_train)
        x_test = np.array(x_test); y_test = np.array(y_test)
        print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
        return x_train, y_train, x_test, y_test
        '''


if __name__ == '__main__':
    data_load(init_data_file)