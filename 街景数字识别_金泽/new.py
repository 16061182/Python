import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD


x_train = np.load("./x_train_315.npy")
y_train = np.load("./y_train.npy")
x_test = np.load("./x_test_0.npy")

x_train = x_train.reshape(4200,32,32,1)
# y_train = y_train.reshape(16800,1)
x_test = x_test.reshape(1800,32,32,1)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 1)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=500)
model.save("./MyModel")

predict = model.predict(x_test)
predict = np.array(predict)
print(predict.shape)
answer = []
for ret in predict:
    answer.append(np.where(ret == np.max(ret))[0])

answer = pd.DataFrame(answer)
answer.to_csv('./submission.csv', encoding='utf-8')