# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import os
import cv2
import sys
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.models import Model, load_model
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


class Ui_Form3(object):
    def setupUi(self, Form):
        # définition de l'interface
        Form.setObjectName("Form")
        Form.resize(533, 327)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 155, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 50, 431, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 224, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet("QFrame{background-color : #c7e0f0}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Quitter_Button = QtWidgets.QPushButton(self.frame)
        self.Quitter_Button.setGeometry(QtCore.QRect(150, 210, 121, 25))
        self.Quitter_Button.setObjectName("Quitter_Button")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 211, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Lancer_Partie = QtWidgets.QPushButton(self.frame)
        self.Lancer_Partie.setGeometry(QtCore.QRect(20, 10, 191, 25))
        self.Lancer_Partie.setObjectName("Lancer_Partie")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 161, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("darknet/data/cifar/new.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 171, 21))
        self.label_6.setObjectName("label_6")
        self.Regles = QtWidgets.QPushButton(self.frame)
        self.Regles.setGeometry(QtCore.QRect(20, 210, 121, 25))
        self.Regles.setObjectName("Regles")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(240, 40, 171, 17))
        self.label_7.setObjectName("label_7")
        self.Lancer_coup = QtWidgets.QPushButton(self.frame)
        self.Lancer_coup.setGeometry(QtCore.QRect(20, 40, 191, 25))
        self.Lancer_coup.setObjectName("Lancer_coup")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 191, 17))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 191, 17))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 191, 17))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 170, 191, 17))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 10, 91, 131))
        self.label_4.setStyleSheet("QLabel{ background-image: url(:/Pepper.png) }")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pepper.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # chargement du modèle de reconnaissance faciale
        model_path="/home/zowi/Documents/Projet/facenet/contributed3/modele_pierre/model2.h5"
        self.model = load_model(model_path)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Quitter_Button.clicked.connect(self.on_Quitter_Button_clicked)
        self.Lancer_coup.clicked.connect(self.on_Lancer_coup_clicked)
        self.Lancer_Partie.clicked.connect(self.on_Lancer_partie_clicked)
        self.Regles.clicked.connect(self.on_Regles_clicked)

        self.Partie =False
        # fonction pour lancer la box pour les règles
    def on_Regles_clicked(self):

        regles= QMessageBox()

        regles.setWindowTitle("Règles")
        regles.setText("Voici les règles du Pierre/Papier/Ciseaux :\n Bouton Lancer Partie -> Lance la partie \n Bouton Lancer Coup -> jouer un tour \n Le premier à trois a gagné \n")

        x=regles.exec_()
        # fonction pour lancer une partie
    def on_Lancer_partie_clicked(self):
        self.counta = 0
        self.countb = 0
        self.Partie = True
        self.Partie_Texte = 'Lancement de la partie'
        self.label_5.setText(self.Partie_Texte)
        self.label_10.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        # fonction appeler pour chaque coup
    def on_Lancer_coup_clicked(self):
        if self.Partie ==True: # il faut d'abord lancer une partie sinon message d'erreur
            video_capture = cv2.VideoCapture(0) # ouverture de la caméra
            if self.counta < 3 and self.countb < 3:
                a = random.randrange(3) # lancement du coup pour le robot
                if a == 0:
                    mouv1 = 'pierre'
                if a == 1:
                    mouv1 = 'papier'
                if a == 2:
                    mouv1 = 'ciseaux'

                ret, frame = video_capture.read() # capture d'image



                classes = ['Ciseau','Papier','Pierre'] # noms des classes à reconnaitres
                cv2.imwrite("coup.png",frame)
                # preprocessing de image pour apres la reconnaitre avec le modèle
                img = image.load_img("coup.png",target_size=(224,224))

                x = image.img_to_array(img)
                x = np.expand_dims(x,axis=0)
                x = preprocess_input(x)
                prediction = self.model.predict(x)[0] # la variable prediction est un vecteur avec trois valeur de prediction pour chaque classe
                result = [(classes[i], float(prediction[i]) * 100.0) for i in range(len(prediction))]
                result.sort(reverse=True, key=lambda x: x[1])
                (mouv2, taux) = result[0]

                self.label_3.setPixmap(QtGui.QPixmap("coup.png"))


                # comparaison des coups
                if mouv2 == 'Pierre':
                    b = 0
                if mouv2 == 'Papier':
                    b = 1
                if mouv2 == 'Ciseau':
                    b = 2
                if a == b + 1 or a == b - 2:
                    self.counta += 1
                    #avictoire
                elif b == a + 1 or b == a - 2:

                    self.countb += 1
                    #bvictoire
                else :
                    print("") # egaliter
                    # affichage des résultats
            self.label_8.setText("Score :")
            self.label_9.setText("Robot : "+str(self.counta)+" Vous : "+ str(self.countb))
            self.label_6.setText("Robot a joué: " + mouv1)
            self.label_7.setText("Vous avez joué: " + mouv2)
            if self.counta == 3:
                self.label_10.setText("Victoire du robot")
                self.Partie = False
            if self.countb == 3:
                self.label_10.setText("Vous avez gagné GG")
                self.Partie = False
            video_capture.release()
        else :
            self.label_5.setText("Lancer d'abord une Partie")

    def on_Quitter_Button_clicked(self):
        sys.exit()
        #code pour quitter



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Pierre Papier Ciseaux </span></p><p><br/></p></body></html>"))
        self.Quitter_Button.setText(_translate("Form", "Quitter"))
        self.Lancer_coup.setText(_translate("Form", "Lancer Un Coup"))
        self.Lancer_Partie.setText(_translate("Form", "Lancer Partie"))
        self.label_6.setText(_translate("Form", "Robot a joué : "))
        self.Regles.setText(_translate("Form", "Règles"))
        self.label_7.setText(_translate("Form", "Vous avez joué :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
