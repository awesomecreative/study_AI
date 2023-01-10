import numpy as np
from sklearn.datasets import load_wine

#1. data
datasets = load_wine()
x = datasets.data
y = datasets.target

print(x.shape, y.shape) # (178,13) (178,)
print(y) # 다중분류임을 알 수 있음.
print(np.unique(y)) # [0 1 2]
print(np.unique(y, return_counts=True)) # [0 1 2] [59 71 48]

from tensorflow.keras.utils import to_categorical
y = to_categorical(y)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True, random_state=1)

#2. model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()
model.add(Dense(10, activation='relu', input_shape=(13,)))
model.add(Dense(70, activation='sigmoid'))
model.add(Dense(120, activation='relu'))
model.add(Dense(80, activation='linear'))
model.add(Dense(10, activation='linear'))
model.add(Dense(3, activation='softmax'))

#3. compile, fit
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
earlyStopping = EarlyStopping(monitor='val_loss', mode='min', patience=50, restore_best_weights=True, verbose=1)
model.fit(x_train, y_train, epochs=1000, batch_size=1, validation_split=0.2, verbose=1, callbacks=[earlyStopping])

#4. evaluate, predict
loss, accuracy = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy : ', accuracy)

y_predict = model.predict(x_test)
print(y_predict)

y_predict = np.argmax(y_predict, axis=1)
y_test = np.argmax(y_test, axis=1)
print('y_predict : ', y_predict)
print('y_test : ', y_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_predict)
print('acc : ', acc)

"""
y_predict :  [2 1 0 1 0 2 1 0 2 1 0 1 1 0 1 1 1 0 1 0 0 1 2 1 0 2 0 0 0 2 1 2 2 0 1 1]
y_test :  [2 1 0 1 0 2 1 0 2 1 0 0 1 0 1 1 2 0 1 0 0 1 2 1 0 2 0 0 0 2 1 2 2 0 1 1]
acc :  0.9444444444444444
"""

"""
Memo
np.unique(y) : y의 고유한 값들만 모아서 반환한다.
np.unique(y, return_counts=True) : y의 고유한 값들과 각각 몇 개 있는 지도 알려줌.
"""