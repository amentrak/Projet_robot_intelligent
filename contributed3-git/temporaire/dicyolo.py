# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import os

dic = {}
trad = {'person': 'personne', 'bicycle': 'vélo', 'car': 'voiture', 'motorbike': 'moto', 'aeroplane': 'avion', 'bus': 'autobus', 'train': 'train', 'truck': 'camion', 'boat': 'bateau', 'traffic light': 'feu de circulation', 'fire hydrant': "bouche d'incendie", 'stop sign': 'panneau stop', 'parking meter': 'parcmètre', 'bench': 'banc', 'bird': 'oiseau', 'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'sheep': 'mouton', 'cow': 'vache', 'elephant': 'éléphant', 'bear': 'ours', 'zebra': 'zèbre', 'giraffe': 'girafe', 'backpack': 'sac à dos', 'umbrella': 'parapluie', 'handbag': 'sac à main', 'tie': 'attacher', 'suitcase': 'valise', 'frisbee': 'frisbee', 'skis': 'ski', 'snowboard': 'snowboard', 'sports ball': 'ballon de sport', 'kite': 'cerf-volant', 'baseball bat': 'batte de baseball', 'baseball glove': 'gant de baseball', 'skateboard': 'planche à roulette', 'surfboard': 'planche de surf', 'tennis racket': 'raquette de tennis', 'bottle': 'bouteille', 'wine glass': 'verre de vin', 'cup': 'coupe', 'fork': 'fourchette', 'knife': 'couteau', 'spoon': 'cuillère', 'bowl': 'bol', 'banana': 'banane', 'apple': 'pomme', 'sandwich': 'sandwich', 'orange': 'orange', 'broccoli': 'brocoli', 'carrot': 'carotte', 'hot dog': 'hot-dog', 'pizza': 'pizza', 'donut': 'donut', 'cake': 'gâteau', 'chair': 'chaise', 'sofa': 'sofa', 'pottedplant': 'plante en pot', 'bed': 'lit', 'diningtable': 'table à manger', 'toilet': 'toilette', 'tvmonitor': 'tvmonitor', 'laptop': 'portable', 'mouse': 'souris', 'remote': 'éloigné', 'keyboard': 'clavier', 'cell phone': 'téléphone portable', 'microwave': 'four micro onde', 'oven': 'four', 'toaster': 'grille-pain', 'sink': 'évier', 'refrigerator': 'réfrigérateur', 'book': 'livre', 'clock': 'horloge', 'vase': 'vase', 'scissors': 'ciseaux', 'teddy bear': 'ours en peluche', 'hair drier': 'sèche cheveux', 'toothbrush': 'brosse à dents'}
pluriel = {'person': 'personnes', 'bicycle': 'vélos', 'car': 'voitures', 'motorbike': 'motos', 'aeroplane': 'avions', 'bus': 'buss', 'train': 'trains', 'truck': 'camions', 'boat': 'bateaux', 'traffic light': 'feux de circulation', 'fire hydrant': "Bouches d'incendie", 'stop sign': "panneaux d'arrêt", 'parking meter': 'parcmètres', 'bench': 'bancs', 'bird': 'oiseaux', 'cat': 'chats', 'dog': 'chiens', 'horse': 'chevaux', 'sheep': 'moutons', 'cow': 'vaches', 'elephant': 'éléphants', 'bear': 'ours', 'zebra': 'zèbres', 'giraffe': 'girafes', 'backpack': 'sacs à dos', 'umbrella': 'parapluies', 'handbag': 'sacs à main', 'tie': 'cravates', 'suitcase': 'valises', 'frisbee': 'frisbees', 'skis': 'skis', 'snowboard': 'snowboards', 'sports ball': 'balles de sport', 'kite': 'cerfs-volants', 'baseball bat': 'battes de baseball', 'baseball glove': 'gants de baseball', 'skateboard': 'planches à roulettes', 'surfboard': 'planches de surf', 'tennis racket': 'raquettes de tennis', 'bottle': 'bouteilles', 'wine glass': 'verres à vin', 'cup': 'tasses', 'fork': 'fourchettes', 'knife': 'couteaux', 'spoon': 'cuillères', 'bowl': 'boules', 'banana': 'bananes', 'apple': 'pommes', 'sandwich': 'sandwichs', 'orange': 'oranges', 'broccoli': 'brocolis', 'carrot': 'carottes', 'hot dog': 'hot-dogs', 'pizza': 'pizzas', 'donut': 'beignets', 'cake': 'gâteaux', 'chair': 'chaises', 'sofa': 'canapés', 'pottedplant': 'plantes en pot', 'bed': 'lits', 'diningtable': 'tables à manger', 'toilet': 'toilettes', 'tvmonitor': 'moniteurs de télévision', 'laptop': 'ordinateurs portables', 'mouse': 'souris', 'remote': 'télécommandes', 'keyboard': 'claviers', 'cell phone': 'téléphones portables', 'microwave': 'micro-ondes', 'oven': 'fours', 'toaster': 'grille-pain', 'sink': 'puits', 'refrigerator': 'réfrigérateurs', 'book': 'livres', 'clock': 'horloges', 'vase': 'vases', 'scissors': 'ciseaux', 'teddy bear': 'nounours', 'hair drier': 'sèche-cheveux', 'toothbrush': 'brosses à dents'}


os.chdir('/home/maxime/darknet')
sortie = os.popen('./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg 2>/dev/null').read()
sortie = sortie.split('\n')
N = 0
for i in sortie[1:-1]:
    a = i.split(': ')
    objet = a[0]
    if objet in dic:
        dic[objet] += 1
    else :
        dic[objet] = 1
        N += 1
count = 0
for i in dic:
    if count == 0:
        if dic[i] == 1:
            print('Il y a {} {}'.format(dic[i],trad[i]),end = '')
        else :
            print('Il y a {} {}'.format(dic[i],pluriel[i]),end = '')
    elif count == N - 1:
         if dic[i] == 1:
            print(' et {} {}.'.format(dic[i],trad[i]))
         else :
            print(' et {} {}.'.format(dic[i],pluriel[i]))
    else :
        if dic[i] == 1:
            print(', {} {}'.format(dic[i],trad[i]), end = '')
        else :
            print(', {} {}'.format(dic[i],pluriel[i]), end = '')
    count += 1
            
