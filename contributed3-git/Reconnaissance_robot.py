#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:40:41 2020

@author: zowi
"""
# lancer dans un environnement python 2 avec la librairie naoqi
import argparse
import sys
import time
import cv2

import face


def main(args):
    frame_interval = 3  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0
    Test =False
    video_capture = cv2.VideoCapture(0)
    face_recognition = face.Recognition() # pour appeler l'autre classe
    start_time = time.time()
    dicfaces ={}


    if args.debug:
        print("Debug enabled")
        face.debug = True






    while (video_capture.isOpened()):
        ret, frame = video_capture.read()

        if (frame_count % frame_interval) == 0:
            faces = face_recognition.identify(frame)

            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0

        for i in faces:

            if i.name in dicfaces:
                dicfaces[i.name] +=1
            else:
                dicfaces[i.name] = 1

        L_tri_nom = list(sorted(dicfaces, key=dicfaces.__getitem__,reverse =True))



        if len( L_tri_nom) != 0:

            if dicfaces[L_tri_nom[0]] >=5: # verifier que la personne a bien été reconnu un bon nombre de fois
                cv2.imwrite("BG.png",frame)
                return L_tri_nom[0]
                break

    video_capture.release()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)


if __name__ == '__main__':




    resultat = main(parse_arguments(sys.argv[1:]))
    #print(resultat)
    with open ('/home/zowi/Documents/Projet/facenet/contributed3/code_fichiertxt/behavior_1/test23.txt','w') as o:
        o.write("")
    time.sleep(1.5)
    with open ('/home/zowi/Documents/Projet/facenet/contributed3/code_fichiertxt/behavior_1/test23.txt','w') as o:
        o.write("zowi")
