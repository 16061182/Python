import numpy as np
import tkinter as tk
path = "C:/Users/98341/Desktop/#01101纵向障碍物-宽门-无奖励-1_v8/"
real_input_data = []

for i in range(1,27):
    with open(path+str(i)+".txt") as f:
        init = f.read()
        data = init.split('\n')
        # print(len(data))
        input_data = []
        # print(i)
        for j in range(len(data) - 1):
            x = np.float32(data[j].split()[0])
            y = np.float32(data[j].split()[1])
            input_data.append([x, y])
        # print(j)
        # in_data = np.array(input_data, dtype=np.float32)
        real_input_data.append(input_data)
        # print(in_data)
        # print(in_data.shape)

print(len(real_input_data))
print(type(real_input_data[0][1][0]))

max_steps = 384
for i in range(0,26):
    length = len(real_input_data[i])
    for j in range(0, max_steps - length):
        real_input_data[i].append(real_input_data[i][length-1])

steps = []
for i in range(0,26):
    steps.append(len(real_input_data[i]))
max_steps = max(steps)
# print(steps)
# print(real_input_data[25])

def cal(x1,y1,x2,y2):
    return np.sqrt((x1 - x2)*(x1 - x2)+(y1 - y2)*(y1 - y2))

# d = [1,100,2]
# d.append(1)
# d.sort()
# print(d)

# for i in range(26,0,-1):
#     print(i)

train_x_data = []
#取前383个
for i in range(383):
    all_line = []
    for j in range(26):
        x = real_input_data[j][i][0]
        y = real_input_data[j][i][1]
        distance = []
        index = []
        line = []#向量
        line.append(x)
        line.append(y)
        for k in range(26):
            xx = real_input_data[k][i][0]
            yy = real_input_data[k][i][1]
            distance.append(cal(x,y,xx,yy))#距离加入距离列表
            index.append(k)
        #排序
        for ii in range(25,0,-1):
            for jj in range(0,ii):
                if(distance[jj] > distance[jj+1]):
                    temp_d = distance[jj]
                    distance[jj] = distance[jj+1]
                    distance[jj+1] = temp_d
                    temp_i = index[jj]
                    index[jj] = index[jj+1]
                    index[jj+1] = temp_i
        for ii in range(1,5):#不包括距离为0的点（自身）
            line.append(real_input_data[index[ii]][i][0])
            line.append(real_input_data[index[ii]][i][1])
        all_line.append(line)
    train_x_data.append(all_line)

train_y_data = []
for i in range(383):
    all_line = []
    for j in range(26):
        line = []
        line.append(real_input_data[j][i+1][0])
        line.append(real_input_data[j][i+1][1])
        all_line.append(line)
    train_y_data.append(all_line)


# print(len(train_x_data[1][9]))
# print(len(train_y_data[1][9]))
# for i in range(383):
#     if(len(train_x_data[i])!=26):
#         print("error")
#         print(i)
#     for j in range(26):
#         if(len(train_x_data[i][j])!=10):
#             print("err")
#             print(i)
#             print(j)
#
# for i in range(383):
#     if(len(train_y_data[i])!=26):
#         print("y_error")
#         print(i)
#     for j in range(26):
#         if(len(train_y_data[i][j])!=2):
#             print("y_err")
#             print(i)
#             print(j)
# print(train_x_data)
x_data_train = np.array(train_x_data)
y_data_train = np.array(train_y_data)
np.save("x_data_train",x_data_train)
np.save("y_data_train",y_data_train)
print(x_data_train.shape)
print(y_data_train.shape)

# print(x_data_train.shape)
# print(y_data_train.shape)
def next(label):
    all_line = []
    for i in range(len(label)):
        line = []
        x = label[i][0]
        y = label[i][1]
        line.append(x)
        line.append(y)
        distance = []
        index = []
        for j in range(len(label)):
            xx = label[j][0]
            yy = label[j][1]
            distance.append(cal(x,y,xx,yy))#加入距离列表
            index.append(j)
        for ii in range(25,0,-1):
            for jj in range(0,ii):
                # print(jj)
                if (distance[jj] > distance[jj + 1]):
                    temp_d = distance[jj]
                    distance[jj] = distance[jj + 1]
                    distance[jj + 1] = temp_d
                    temp_i = index[jj]
                    index[jj] = index[jj + 1]
                    index[jj + 1] = temp_i
        for ii in range(1,5):
            line.append(label[index[ii]][0])
            line.append(label[index[ii]][1])
        all_line.append(line)
    all_line = np.array(all_line)
    return all_line

for i in range(383):
    print(x_data_train[i])
# Coot = tk.Tk()
# # 创建一个Canvas，设置其背景色为白色
# cv = tk.Canvas(Coot,bg = 'blue')
# # 创建一个矩形，坐标为(10,10,110,110)
# cv.create_rectangle(10,10,110,110)
# cv.pack()
# Coot.mainloop()

# win = tk.Tk()
# # win.title("数学建模作业二")
# # win.geometry("2000x1000")
# # win.resizable(width=False, height=False)
# Caut = tk.Canvas(win, bg = 'blue')
# Caut.create_oval(1000, 1000, 50, 50)
# Caut.pack()
# win.mainloop()

# print(cal(1,1,2,2))
