import cv2
import os
import numpy as np

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


def Deep(path):

	IMG_SIZE = 50
	learn_rate = 1e-3

	MODEL_NAME = 'dogsvscats-{}-{}.model'.format(learn_rate, 'tconv-basic')

	convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')

	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 5)

	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 5)

	convnet = conv_2d(convnet, 128, 5, activation='relu')
	convnet = max_pool_2d(convnet, 5)

	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 5)

	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 5)

	convnet = fully_connected(convnet, 1024, activation='relu')
	convnet = dropout(convnet, 0.8)

	convnet = fully_connected(convnet, 2, activation='softmax')
	convnet = regression(convnet, optimizer='adam', learning_rate=learn_rate, loss='categorical_crossentropy', name='targets')

	model = tflearn.DNN(convnet, tensorboard_dir='log')
	
	if os.path.exists('{}.meta'.format(MODEL_NAME)):
		model.load(MODEL_NAME)
		# # print('model loded!')
		# return "super"

	# if path.exists(path):
	# path = 'media/Images/8.jpg'

	# img = cv2.imread(path[1:], cv2.IMREAD_GRAYSCALE)
	# img = cv2.imread(path[1:])
	img = cv2.cvtColor(path, cv2.COLOR_BGR2GRAY)
	# print(np.array(img))
	img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
	img_data = np.array(img)
	data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
	model_out = model.predict([data])[0]
	if np.argmax(model_out) == 1: 
		STR_LABEL='dog'
		return "dog"
	else:
		STR_LABEL='cat'
		return "cat"
		# print(STR_LABEL)
	
