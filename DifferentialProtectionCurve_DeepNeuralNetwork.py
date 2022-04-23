!pip3 install ann_visualizer
!pip3 install keras-visualizer

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import tensorflow as tf

from keras.regularizers import l2
from keras.models import Sequential
from keras.layers import Dense


from sklearn.metrics import accuracy_score

from ann_visualizer.visualize import ann_viz
from keras_visualizer import visualizer

from google.colab import files
uploaded = files.upload()

# Importing the datasets
datasets = pd.read_csv('diff.csv', sep=',')
X = datasets.iloc[:, [0,1]].values
Y = datasets.iloc[:, 2].values
datasets.head()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_Train)

X_train1 = scaler.transform(X_Train)
X_train1 = X_train1.astype(np.float32)

X_test1 = scaler.transform(X_Test)
X_test1 = X_test1.astype(np.float32)

model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu', kernel_regularizer=l2(0.2)))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary() 

history = model.fit(X_train1, Y_Train, validation_data = (X_test1, Y_Test), epochs=500, verbose=2)

ann_viz(model, title="Differential_Protection_Curve_DeepNeuralNetwork");
visual = visualizer(model, format='png', view=True)

all_predict = model.predict(X_test1)
n = 0
for r in all_predict:
  if all_predict[n][0] < 0.5:
    all_predict[n][0] = 0
  else:
    all_predict[n][0] = 1
  n = n+1
# print(all_predict)
# print(Y_Test)
print("accuracy deep neural network: ", accuracy_score(Y_Test, all_predict))

# summarize history for accuracy
figure(figsize=(15, 10), dpi=80)
fig1 = plt.gcf()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

fig1.savefig("model_accuracy.png", dpi=200)
files.download("model_accuracy.png")

figure(figsize=(15, 10), dpi=80)
fig1 = plt.gcf()

plt.plot(history.history['loss']) 
plt.plot(history.history['val_loss']) 
plt.title('Model loss') 
plt.ylabel('Loss') 
plt.xlabel('Epoch') 
plt.legend(['Train', 'Test'], loc='upper left') 
plt.show()
plt.draw()

fig1.savefig("nn_resolve_overfitting.png", dpi=200)
files.download("nn_resolve_overfitting.png")

all_predict = model.predict(X_test1)
print(Y_Test)
all_predict

# x_sample = scaler.transform([[1.130 , 4.479   ]])
x_sample = scaler.transform([[2.55, 3]])
# x_sample = scaler.transform([[1.748, 15]])
# x_sample = scaler.transform([[6.950, 10]])
# x_sample = scaler.transform([[7.26, 3]])
x_sample = x_sample.astype(np.float32)

predict = model.predict(x_sample)
print(predict)

model.save( 'models/model.h5' )

tflite_model = tf.keras.models.load_model('models/model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(tflite_model)
tflite_save = converter.convert()
open("tfliteModel.tflite", "wb").write(tflite_save)
