
# coding: utf-8

# ## Import Packages

# In[13]:

#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import numpy as np
import cv2

lines = [] 
with open('data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
measurements = []

for line in lines:
    source_path_center = line[0]
    source_path_left = line[1]
    source_path_right = line[2]

    filename_center = source_path_center.split('/')[-1]
    filename_left = source_path_left.split('/')[-1]
    filename_right = source_path_right.split('/')[-1]

    currentpath_center = 'data/IMG/' + filename_center
    currentpath_left = 'data/IMG/' + filename_left
    currentpath_right = 'data/IMG/' + filename_right

    image_center = cv2.imread(currentpath_center)
    images.append(image_center)
    image_left = cv2.imread(currentpath_left)
    images.append(image_left)
    image_right = cv2.imread(currentpath_right)
    images.append(image_right)
    
    correction= 0.2
    measurement = float(line[3])
    measurements.append(measurement)
    measurements.append(measurement+correction)
    measurements.append(measurement-correction)

aug_images, aug_measurements = [], []
for image, measurement in zip(images, measurements):
    aug_images.append(image)
    aug_measurements.append(measurement)
    aug_images.append(cv2.flip(image,1))
    aug_measurements.append(measurement*-1.0)
	   
X_train = np.array(aug_images)
Y_train = np.array(aug_measurements)

print(len(X_train))
print(len(Y_train))

print(X_train.shape)
print(Y_train.shape)


# In[11]:

from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.layers import Lambda, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

model = Sequential()
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((70,25), (0,0))))
model.add(Convolution2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, Y_train, validation_split=0.2, shuffle=True, nb_epoch=10)
model.save('model.h5')

