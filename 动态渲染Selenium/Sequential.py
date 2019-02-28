from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
from Loader import *


def build_and_predict(train_x, train_y, test_x, test_y):
    Model = Sequential()
    Model.add(Dense(100, input_dim=5, activation='relu'))
    #Model.add(Dropout(0.5))
    for i in range(2):
        Model.add(Dense(100, activation='relu'))
        #Model.add(Dropout(0.5))
    Model.add(Dense(1))
    Model.compile(loss = 'mse', optimizer='adam', metrics=['accuracy'])
    Model.fit(train_x, train_y, batch_size=20, epochs = 100)
    # result = Model.evaluate(train_x, train_y)
    # print('\n训练集上的正确率为 ', result[1])
    # result = Model.evaluate(test_x, test_y)
    # print('\n测试集上的正确率为 ', result[1])
    result = Model.predict(test_x)
    print(result.shape)
    for i in range(847):
        print(test_y[i], result[i][0])
    return result

if __name__ == '__main__':
    train_x, train_y, test_x, test_y = data_load(init_data_file)
    build_and_predict(train_x, train_y, test_x, test_y)