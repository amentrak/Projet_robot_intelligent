import random
import os
import cv2
import time 
counta = 0
countb = 0
video_capture = cv2.VideoCapture(0)
if counta < 3 and countb < 3:
    a = random.randrange(3)
    if a == 0:
        mouv1 = 'pierre'
    if a == 1:
        mouv1 = 'papier'
    if a == 2:
        mouv1 = 'ciseaux'
    ret, frame = video_capture.read()

    cv2.imwrite("/home/zowi/Documents/Projet/facenet/contributed3/darknet/data/cifar/new.png",frame)
    
    os.chdir('/home/zowi/Documents/Projet/facenet/contributed3/darknet')
    sortie = os.popen('./darknet classifier predict cfg/cifar.data cfg/cifar_small.cfg backup/cifar_small.backup data/cifar/new.png 2>/dev/null').read()
    taux = sortie[0:5]
   
    if taux =='100.0':
        mouv2 = sortie[9:15]
    else:
        mouv2 = sortie[8:14]
    
    if mouv2 == 'Pierre':
        b = 0
    if mouv2 == 'Papier':
        b = 1
    if mouv2 == 'Ciseau':
        b = 2
    if a == b + 1 or a == b - 2:
        print('a gagne')
        counta += 1
    elif b == a + 1 or b == a - 2:
        print('b gagne')
        countb += 1
    else : 
        print('égalité')
    
if counta == 3:
    print('victoire de a')
else:
    print('victoire de b')
video_capture.release()

