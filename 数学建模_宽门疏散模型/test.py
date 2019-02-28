import numpy as np
data = np.random.random((1000,100)) #size = (1000,100) variable size's type is typle
test = np.random.randint(2,size = (1000,1)) #size = (1000,1)
test1 = test.reshape(1000) #size = (1000,)
temp1_list = [1,2,3,3,4]
temp1_array = np.array(temp1_list) #size = (5,)
temp2_list = []
temp2_list.append([1])
temp2_list.append([2])
temp2_list.append([3])
temp2_list.append([3])
temp2_list.append([4])
temp2_array = np.array(temp2_list) #size = (5,1)
print(temp2_array)
print(temp2_array.shape)

np.save('data',data)
data_jr = np.load('data.npy') #size = (1000,100)