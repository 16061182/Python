import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout,Recurrent
import time
from keras.optimizers import SGD
from read import *
import tkinter as tk
x_train = np.load('./x_data_train.npy')
y_train = np.load('./y_data_train.npy')

win = tk.Tk()
win.title("训练结果演示，红色为训练出来的结果，黄色为原始数据结果")
win.geometry("1400x1050")
win.resizable(width=False, height=False)
C = tk.Canvas(win,width = 1400,height = 1050)
C.pack()


Model = Sequential()
Model.add(Dense(100,input_shape = (26,10),activation = 'relu'))
Model.add(Dense(100,activation = 'relu'))
Model.add(Dense(100,activation = 'relu'))
Model.add(Dense(2))
#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
Model.compile(optimizer = 'adam',loss = 'mse',metrics=['accuracy'])
Model.fit(x_train,y_train,epochs = 500)
temp1 = np.array([x_train[0]])
t1 = np.array(x_train[0])
print(temp1.shape)
print(t1.shape)

# temp2 = np.array[y_train[0]]

#next(lebel) 输入26*2返回26*10（array）
for i in range(380):
    C.delete("all")
    for j in range (26):
        C.create_oval(temp1[0][j][0]*100-10-200, temp1[0][j][1]*100-10-200, temp1[0][j][0]*100+10-200, temp1[0][j][1]*100+10-200, fill = "red")
        C.create_oval(y_data_train[i][j][0]*100-10-200, y_data_train[i][j][1]*100-10-200, y_data_train[i][j][0]*100+10-200, y_data_train[i][j][1]*100+10-200, fill = "yellow")
        C.pack()
    C.update()
    temp2 = Model.predict(temp1)
    print(temp2)
    temp2 = temp2.reshape(26,2)
    temp1 = next(temp2)
    temp1 = np.array([temp1])
    time.sleep(0.1)
win.mainloop()


