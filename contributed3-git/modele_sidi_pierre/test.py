#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:25:04 2020

@author: zowi
"""

import tensorflow as tf
from IPython.display import Image, HTML, display
#from matplotlib import pyplot as plt
from keras.preprocessing import image
from keras.models import Model, load_model
import numpy as np
import os
import cv2 
import os
import csv
from keras.models import load_model
from tensorflow import keras
from keras import backend as K
from keras.backend.tensorflow_backend import set_session
from keras.preprocessing.image import ImageDataGenerator
from keras.losses import categorical_crossentropy
from keras.layers import Dense, GlobalAveragePooling2D, Activation, Flatten
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.applications.xception import Xception, preprocess_input, decode_predictions #299*299
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions #224*224
from keras.applications.inception_v3 import InceptionV3, preprocess_input,decode_predictions# input shape= 299x299
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input,decode_predictions# input shape= 299x299
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.applications.densenet import DenseNet121, preprocess_input, decode_predictions# input shape= 224x224 
from keras.applications.densenet import DenseNet169, preprocess_input
from keras.applications.densenet import DenseNet201, preprocess_input
from keras.applications.nasnet import NASNetLarge, preprocess_input
from keras.applications.nasnet import NASNetMobile, preprocess_input
from keras.optimizers import Adam, SGD
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint, EarlyStopping
import math
import argparse
#import matplotlib
import imghdr
import pickle as pkl
import datetime
#from cycler import cycler
from PIL import Image, ImageEnhance
#import matplotlib.pyplot as plt
from keras import utils as np_utils


def generate_from_paths_and_labels(input_paths, labels, batch_size, input_size=(299,299)):

    num_samples = len(input_paths)
    while 1:
        perm = np.random.permutation(num_samples)
        input_paths = input_paths[perm]
        labels = labels[perm]
        for i in range(0, num_samples, batch_size):
            inputs = list(map(
                lambda x: image.load_img(x, target_size=input_size),
                input_paths[i:i+batch_size]
            ))
            inputs = np.array(list(map(
                lambda x: image.img_to_array(x),
                inputs
            )))
            inputs = preprocess_input(inputs)
            yield (inputs, labels[i:i+batch_size])
            
model_path="/home/zowi/Documents/Projet/facenet/contributed3/modele_sidi_pierre/model2.h5"
classes_path = "classes.txt"
dataset_test="Corentin"    
image_path ="/home/zowi/Documents/Projet/facenet/contributed3/modele_sidi_pierre/corentin//14_Ciseau.png"     
top_n=3
model = load_model(model_path)
img = image.load_img(image_path,target_size=(224,224))

x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)
prediction = model.predict(x)
print(prediction)

#model = tf.keras.models.load_model(model_path)
