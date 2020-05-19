# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'four.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mail import mail
import os
import cv2
import sys


class Ui_Form4(object):
    def setupUi(self, Form):
        # definition de interface
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
        self.Quitter_Button.setGeometry(QtCore.QRect(300, 220, 121, 25))
        self.Quitter_Button.setObjectName("Quitter_Button")
        self.Lancer = QtWidgets.QPushButton(self.frame)
        self.Lancer.setGeometry(QtCore.QRect(20, 10, 161, 25))
        self.Lancer.setObjectName("Lancer")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 231, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("attente.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 131, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 131, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(270, 50, 141, 151))
        self.label_5.setObjectName("label_5")
        self.Email = QtWidgets.QPushButton(self.frame)
        self.Email.setGeometry(QtCore.QRect(10, 220, 141, 25))
        self.Email.setObjectName("Email")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 10, 91, 131))
        self.label_4.setStyleSheet("QLabel{ background-image: url(:/Pepper.png) }")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pepper.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Quitter_Button.clicked.connect(self.on_Quitter_Button_clicked)
        self.Lancer.clicked.connect(self.on_Lancer_clicked)
        self.Email.clicked.connect(self.on_email_clickek)
        # lancer la reconnaissance objet
    def on_Lancer_clicked(self):
        import os
        text =""
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        # essai pour utiliser pour des fichiers settings pour les chemins d'accès
        """
        try:
            settings = readSetting()
            if type(settings) is not dict:
                raise SystemExit('Settings file is missing or incomplete')
        except Exception as e:
            print(e)
            """

        cv2.imwrite("/home/zowi/Documents/Projet/facenet/contributed3/darknet/data/new.jpg",frame)



        video_capture.release()

        dic = {}
        # defintion des classes de yolo en francais
        trad = {'person': 'personne', 'bicycle': 'vélo', 'car': 'voiture', 'motorbike': 'moto', 'aeroplane': 'avion', 'bus': 'autobus', 'train': 'train', 'truck': 'camion', 'boat': 'bateau', 'traffic light': 'feu de circulation', 'fire hydrant': "bouche d'incendie", 'stop sign': 'panneau stop', 'parking meter': 'parcmètre', 'bench': 'banc', 'bird': 'oiseau', 'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'sheep': 'mouton', 'cow': 'vache', 'elephant': 'éléphant', 'bear': 'ours', 'zebra': 'zèbre', 'giraffe': 'girafe', 'backpack': 'sac à dos', 'umbrella': 'parapluie', 'handbag': 'sac à main', 'tie': 'attacher', 'suitcase': 'valise', 'frisbee': 'frisbee', 'skis': 'ski', 'snowboard': 'snowboard', 'sports ball': 'ballon de sport', 'kite': 'cerf-volant', 'baseball bat': 'batte de baseball', 'baseball glove': 'gant de baseball', 'skateboard': 'planche à roulette', 'surfboard': 'planche de surf', 'tennis racket': 'raquette de tennis', 'bottle': 'bouteille', 'wine glass': 'verre de vin', 'cup': 'coupe', 'fork': 'fourchette', 'knife': 'couteau', 'spoon': 'cuillère', 'bowl': 'bol', 'banana': 'banane', 'apple': 'pomme', 'sandwich': 'sandwich', 'orange': 'orange', 'broccoli': 'brocoli', 'carrot': 'carotte', 'hot dog': 'hot-dog', 'pizza': 'pizza', 'donut': 'donut', 'cake': 'gâteau', 'chair': 'chaise', 'sofa': 'sofa', 'pottedplant': 'plante en pot', 'bed': 'lit', 'diningtable': 'table à manger', 'toilet': 'toilette', 'tvmonitor': 'tvmonitor', 'laptop': 'portable', 'mouse': 'souris', 'remote': 'éloigné', 'keyboard': 'clavier', 'cell phone': 'téléphone portable', 'microwave': 'four micro onde', 'oven': 'four', 'toaster': 'grille-pain', 'sink': 'évier', 'refrigerator': 'réfrigérateur', 'book': 'livre', 'clock': 'horloge', 'vase': 'vase', 'scissors': 'ciseaux', 'teddy bear': 'ours en peluche', 'hair drier': 'sèche cheveux', 'toothbrush': 'brosse à dents'}
        pluriel = {'person': 'personnes', 'bicycle': 'vélos', 'car': 'voitures', 'motorbike': 'motos', 'aeroplane': 'avions', 'bus': 'buss', 'train': 'trains', 'truck': 'camions', 'boat': 'bateaux', 'traffic light': 'feux de circulation', 'fire hydrant': "Bouches d'incendie", 'stop sign': "panneaux d'arrêt", 'parking meter': 'parcmètres', 'bench': 'bancs', 'bird': 'oiseaux', 'cat': 'chats', 'dog': 'chiens', 'horse': 'chevaux', 'sheep': 'moutons', 'cow': 'vaches', 'elephant': 'éléphants', 'bear': 'ours', 'zebra': 'zèbres', 'giraffe': 'girafes', 'backpack': 'sacs à dos', 'umbrella': 'parapluies', 'handbag': 'sacs à main', 'tie': 'cravates', 'suitcase': 'valises', 'frisbee': 'frisbees', 'skis': 'skis', 'snowboard': 'snowboards', 'sports ball': 'balles de sport', 'kite': 'cerfs-volants', 'baseball bat': 'battes de baseball', 'baseball glove': 'gants de baseball', 'skateboard': 'planches à roulettes', 'surfboard': 'planches de surf', 'tennis racket': 'raquettes de tennis', 'bottle': 'bouteilles', 'wine glass': 'verres à vin', 'cup': 'tasses', 'fork': 'fourchettes', 'knife': 'couteaux', 'spoon': 'cuillères', 'bowl': 'boules', 'banana': 'bananes', 'apple': 'pommes', 'sandwich': 'sandwichs', 'orange': 'oranges', 'broccoli': 'brocolis', 'carrot': 'carottes', 'hot dog': 'hot-dogs', 'pizza': 'pizzas', 'donut': 'beignets', 'cake': 'gâteaux', 'chair': 'chaises', 'sofa': 'canapés', 'pottedplant': 'plantes en pot', 'bed': 'lits', 'diningtable': 'tables à manger', 'toilet': 'toilettes', 'tvmonitor': 'moniteurs de télévision', 'laptop': 'ordinateurs portables', 'mouse': 'souris', 'remote': 'télécommandes', 'keyboard': 'claviers', 'cell phone': 'téléphones portables', 'microwave': 'micro-ondes', 'oven': 'fours', 'toaster': 'grille-pain', 'sink': 'puits', 'refrigerator': 'réfrigérateurs', 'book': 'livres', 'clock': 'horloges', 'vase': 'vases', 'scissors': 'ciseaux', 'teddy bear': 'nounours', 'hair drier': 'sèche-cheveux', 'toothbrush': 'brosses à dents'}
        os.chdir("/home/zowi/Documents/Projet/facenet/contributed3/darknet")
        sortie = os.popen('./darknet detect cfg/yolov3.cfg yolov3.weights data/new.jpg 2>/dev/null').read()
        sortie = sortie.split('\n')
        N=0
        for i in sortie[1:-1]:
            a = i.split(': ')
            objet = a[0]
            if objet in dic:
                dic[objet] += 1
            else :
                dic[objet] = 1
                N += 1
        count = 0
        # affichage des résultats
        for i in dic:
            if count == 0:
                if dic[i] == 1:
                    tmp ="Il y a {} {}".format(dic[i],trad[i])
                else :
                    tmp='Il y a {} {}'.format(dic[i],pluriel[i])
            elif count == N - 1:
                 if dic[i] == 1:
                    tmp="et {} {}.".format(dic[i],trad[i])
                 else :
                    tmp="et {} {}.".format(dic[i],pluriel[i])
            else :
                if dic[i] == 1:
                    tmp=" {} {}".format(dic[i],trad[i])
                else :
                    tmp =" {} {}".format(dic[i],pluriel[i])
            text=text+"\n "+tmp
            count += 1




        self.label_5.setText(text)
        self.label_3.setPixmap(QtGui.QPixmap("/home/zowi/Documents/Projet/facenet/contributed3/darknet/predictions.jpg"))


    def on_Quitter_Button_clicked(self):
        sys.exit()
        #code pour quitter

        # bouton pour lancer envoi email, la fonction mail() vient du code de mail 
    def on_email_clickek(self):
        self.Form = QtWidgets.QWidget()
        self.ui = mail()
        self.ui.setupUi(self.Form)
        self.Form.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Comptage d\'objet </span></p><p><br/></p></body></html>"))
        self.Quitter_Button.setText(_translate("Form", "Quitter"))
        self.Lancer.setText(_translate("Form", "Lancer le comptage "))
        self.label_2.setText(_translate("Form", "Element reconnu :"))
        self.pushButton.setText(_translate("Form", "Fonctionnement"))
        self.label_5.setText(_translate("Form", ""))
        self.Email.setText(_translate("Form", "Email souvenir"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form4()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
