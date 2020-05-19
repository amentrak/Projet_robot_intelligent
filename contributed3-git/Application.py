#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:52:40 2020

@author: zowi
"""
import argparse
import sys
import time

import cv2

import face

# fonction principal d'identification
def main(args):
    frame_interval = 3  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0
    Test =False
    video_capture = cv2.VideoCapture(0)
    face_recognition = face.Recognition() # on definit une variable qui est la classe reconnaissance
    start_time = time.time()
    dicfaces ={}


    if args.debug:
        print("Debug enabled")
        face.debug = True
    # ouverture de la caméra
    while (video_capture.isOpened()):
        ret, frame = video_capture.read() # on sauvegard chaque frame

        if (frame_count % frame_interval) == 0:
            faces = face_recognition.identify(frame) # grâce à la classe de reconnaissance on lui passe la frame pour identification, faces est le noms des personnes reconnu

            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0
                # système d'identification on stock dans un dictionnaire le nom des personnes reconnu et le nbr d'occurences
        for i in faces:

            if i.name in dicfaces:
                dicfaces[i.name] +=1
            else:
                dicfaces[i.name] = 1
                  # on trie le dictionnaire en fct du ndr d'occurences de chaque personne reconnu
        L_tri_nom = list(sorted(dicfaces, key=dicfaces.__getitem__,reverse =True))


        # si une personne est reconnu alors on renvoie le nom de la personne reconnu
        if len( L_tri_nom) != 0:

            if dicfaces[L_tri_nom[0]] >=3: # verifier que la personne a bien été reconnu un bon nombre de fois
                cv2.imwrite("BG.png",frame)
                return L_tri_nom[0]

                break


    cv2.imwrite("BG.png",frame)
    video_capture.release()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)


if __name__ == '__main__':


    main(parse_arguments(sys.argv[1:]))
