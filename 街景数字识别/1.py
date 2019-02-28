from PIL import Image
import numpy as np
import pandas as pd

def bat_rotate(file_name,file_num,angle):
    temp = []
    for i in range(0,file_num):
        file_add = file_name + str(i) + ".jpg"
        I = Image.open(file_add)
        L = I.convert('L')
        # print("466")
        L = L.rotate(angle)
        data = np.array(L)
        # print(data.shape)
        temp.append(data)
    perhona = np.array(temp)
    return perhona


def read_inform(file_name,file_num):
    temp = []
    for i in range(0,file_num):
        for j in range(0,4):
            file_add = file_name + str(i) + "_" + str(j) + ".jpg"
            I = Image.open(file_add)
            #I = I.convert('L')
            data = np.array(I)
            print(data.shape)
            temp.append(data)
    return temp

if __name__ == '__main__':
    train_0 = "C:/Users/98341/Desktop/data/train/"
    # train_0 = "C:/Users/98341/Desktop/data/train_0/"
    # train_45 = "C:/Users/98341/Desktop/data/train_45/"
    # train_90 = "C:/Users/98341/Desktop/data/train_90/"
    # train_135 = "C:/Users/98341/Desktop/data/train_135/"
    # train_180 = "C:/Users/98341/Desktop/data/train_180/"
    # train_225 = "C:/Users/98341/Desktop/data/train_225/"
    # train_270 = "C:/Users/98341/Desktop/data/train_270/"
    # train_315 = "C:/Users/98341/Desktop/data/train_315/"

    # temp_0 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,0)
    # print(temp_0.shape)
    temp_45 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,45)
    print(temp_45.shape)
    temp_90 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,90)
    print(temp_90.shape)
    temp_135 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,135)
    print(temp_135.shape)
    temp_180 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,180)
    print(temp_180.shape)
    temp_225 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,225)
    print(temp_225.shape)
    temp_270 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,270)
    print(temp_270.shape)
    temp_315 = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,315)
    print(temp_315.shape)

    
    # np.save("./x_train_0.npy",temp_0)
    np.save("./x_test_45.npy", temp_45)
    np.save("./x_test_90.npy", temp_90)
    np.save("./x_test_135.npy", temp_135)
    np.save("./x_test_180.npy", temp_180)
    np.save("./x_test_225.npy", temp_225)
    np.save("./x_test_270.npy", temp_270)
    np.save("./x_test_315.npy", temp_315)


    # temp_test = bat_rotate("C:/Users/98341/Desktop/data/test/",1800,0)
    # np.save("./x_test_0.npy",temp_test)
    # bat_rotate(s,4200,)
    '''
    for j in range(0,4):
        L = L.rotate(j * 90)
        L.save(dest + str(i) +"_" + str(j) + ".jpg")
    '''