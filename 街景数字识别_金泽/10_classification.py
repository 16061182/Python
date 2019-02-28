import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
'''
x_train = np.load("./x_train_24.npy")
y_train = np.load("./y_train.npy")
x_test = np.load("./x_test_24.npy")
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
'''
train_images = np.load("./x_train_24.npy")
train_labels = np.load("./y_train.npy")
test_images = np.load("./x_test_24.npy")

def narmalize_data(ima):
    a_max = np.max(ima)
    a_min = np.min(ima)
    for j in range(ima.shape[0]):
        ima[j] = (ima[j] - a_min) / (a_max - a_min)
    return ima


def initialize_with_zeros(n_x, n_h, n_y):
    np.random.seed(2)
    # W1=np.random.randn(n_h,n_x)*0.00000001    # W1=np.random.randn(n_h,n_x)
    W1 = np.random.uniform(-np.sqrt(6) / np.sqrt(n_x + n_h), np.sqrt(6) / np.sqrt(n_h + n_x), size=(n_h, n_x))
    # W1=np.reshape(32,784)
    b1 = np.zeros((n_h, 1))
    # W2=np.random.randn(n_y,n_h)*0.00000001  # W2=np.random.randn(n_y,n_h)
    W2 = np.random.uniform(-np.sqrt(6) / np.sqrt(n_y + n_h), np.sqrt(6) / np.sqrt(n_y + n_h), size=(n_y, n_h))
    b2 = np.zeros((n_y, 1))

    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}

    return parameters


def forward_propagation(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    # print W1,X,b1
    Z1 = np.dot(W1, X) + b1
    # A1=sigmoid(Z1)
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    # assert(A2.shape == (1, X.shape[1]))
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    return A2, cache


def costloss(A2, Y, parameters):
    # m=Y.shape[0]
    t = 0.00000000001
    logprobs = np.multiply(np.log(A2 + t), Y) + np.multiply(np.log(1 - A2 + t), (1 - Y))
    # print("jixiaozhi: ",10*np.exp(-10))
    # logprobs = np.multiply(A2-Y,A2-Y)
    cost = np.sum(logprobs, axis=0, keepdims=True) / A2.shape[0]
    # cost=np.squeeze(cost)
    # assert(isinstance(cost, float))
    # cost=cost.astype(float)
    # cost=Variable(cost)
    return cost


def back_propagation(parameters, cache, X, Y):
    # m=X.shape[0]
    # print('m',m)
    W1 = parameters["W1"]
    W2 = parameters["W2"]
    A1 = cache["A1"]
    A2 = cache["A2"]
    Z1 = cache["Z1"]

    dZ2 = A2 - Y
    # print("dz2: ",dZ2)
    # print("A1: ",A1.T)
    dW2 = np.dot(dZ2, A1.T)
    db2 = np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = np.dot(W2.T, dZ2) * (1 - np.power(A1, 2))
    # dZ1=np.dot(W2.T,dZ2)*sigmoid(Z1)*(1-sigmoid(Z1))
    dW1 = np.dot(dZ1, X.T)
    db1 = np.sum(dZ1, axis=1, keepdims=True)
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}

    # print("Dw2:",dW2)
    # print("Db2:",db2)
    return grads


def update_para(parameters, grads, learning_rate):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    dW1 = grads["dW1"]
    db1 = grads["db1"]
    dW2 = grads["dW2"]
    db2 = grads["db2"]
    # print("learning_rate:",learning_rate)
    # sumdW1=np.sum(dW1,axis=1,keepdims=True)
    # print("shape of dw1:",dW1.shape)
    # print("sumdW1: ",sumdW1)
    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    # print("W1",W1)
    # print("W2",W2)
    # print("chakan...")
    # print("canshugengxin....")
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters

def sigmoid(x):
    s=1/(1+np.exp(-x))
    return s
def image2vector(image):
    v=np.reshape(image,[784,1])
    return v
def softmax(x):
    v=np.argmax(x)
    return v


if __name__ == '__main__':
    #train_images = load_train_images()
    #train_labels = load_train_labels()
    #test_images = load_test_images()
    #test_labels = load_test_labels()

    ii = 0
    n_x = 32 * 32
    n_h = 32
    n_y = 10
    parameters = initialize_with_zeros(n_x, n_h, n_y)
    for i in range(50000):
        img_train = train_images[i]
        label_train1 = train_labels[i]
        label_train = np.zeros((10, 1))
        ttt = 0.001
        if i > 1000:
            ttt = ttt * 0.999
        label_train[int(train_labels[i])] = 1
        imgvector1 = image2vector(img_train)
        imgvector = narmalize_data(imgvector1)
        A2, cache = forward_propagation(imgvector, parameters)
        pre_label = softmax(A2)
        costl = costloss(A2, label_train, parameters)
        grads = back_propagation(parameters, cache, imgvector, label_train)
        parameters = update_para(parameters, grads, learning_rate=ttt)
        grads["dW1"] = 0
        grads["dW2"] = 0
        grads["db1"] = 0
        grads["db2"] = 0
        print("cost after iteration %i:" % (i))
        print(costl)
    for i in range(10000):
        img_train = test_images[i]
        vector_image = narmalize_data(image2vector(img_train))
        label_trainx = test_labels[i]
        aa2, xxx = forward_propagation(vector_image, parameters)
        predict_value = softmax(aa2)
        if predict_value == int(label_trainx):
            ii = ii + 1
        # print("the real value is: ",label_trainx)
        # print("the value of our prediction is: ",predict_value)
    print(ii)

'''
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(24, 24, 1)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

# model.add(Conv2D(32, (3, 3), activation='relu'))
# model.add(Conv2D(32, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.5))


# model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(24, 24, 1)))
# model.add(Conv2D(32, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.5))

# model.add(Conv2D(64, (3, 3), activation='relu'))
# # model.add(Conv2D(64, (3, 3), activation='relu'))
# # model.add(MaxPooling2D(pool_size=(2, 2)))
# # model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=500)
model.save("./MyModel")
# model = load_model("./MyModel")
# score = model.evaluate(x_train_test, y_train_test, batch_size=32, verbose=1)
# print(score)
predict = model.predict(x_test)
predict = np.array(predict)
print(predict.shape)
answer = []
for ret in predict:
    answer.append(np.where(ret == np.max(ret))[0])

answer = pd.DataFrame(answer)
answer.to_csv('./submission.csv', encoding='utf-8')
'''