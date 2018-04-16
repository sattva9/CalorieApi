from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

from scipy import misc
import json

import tensorflow as tf

def small_convnet():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Conv2D(32, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Conv2D(64, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten()) 
	model.add(Dense(64))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(25))
	model.add(Activation('softmax'))

	model.compile(loss='categorical_crossentropy',
				optimizer='adam',
				metrics=['acc'])

	return model

def Deep(img):

	graph = tf.Graph()
	with graph.as_default():
		session = tf.Session()
		with session.as_default():
			convnet = small_convnet()
			convnet.load_weights('weights.h5')
			
			x = misc.imresize(img, (150, 150, 3))
			x = x.reshape((1,) + x.shape)
			
			p = convnet.predict_classes(x, verbose=1)
			with open('data.json', 'r') as fp:
				data = json.load(fp)
			return(data[str(p[0])])



	
