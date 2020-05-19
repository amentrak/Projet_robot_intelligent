#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:13:27 2020

@author: zowi
"""

import argparse
import sys
import time

import cv2

import face
from first import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def add_overlays(frame, faces, frame_rate):
    name =None 
    if faces is not None:
        for face in faces:
            face_bb = face.bounding_box.astype(int)
            cv2.rectangle(frame,
                          (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
                          (0, 255, 0), 2)
            if face.name is not None:
                name=face.name

                cv2.putText(frame, face.name + str(round(face.taux,2)), (face_bb[0], face_bb[3]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            thickness=2, lineType=2)

    cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                thickness=2, lineType=2)
    return name 

def main(args):
    frame_interval = 3  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0

    video_capture = cv2.VideoCapture(0)
    face_recognition = face.Recognition() # pour appeler l'autre classe
    start_time = time.time()

    if args.debug:
        print("Debug enabled")
        face.debug = True
    test =0 
    cont = 0
    test1=1
    setfaces =set()
    while True:
        # Capture frame-by-frame
        if test==0:
            print("..............................................................................................")
            print("..........                    FACE AUTHENTIFICATION                     ......................")
            print("..........         Please look at the camera to be identified           ......................")
            print("..............................................................................................")
            print("                                                                                              ")
            test =1
        ret, frame = video_capture.read()

        if (frame_count % frame_interval) == 0:
            faces = face_recognition.identify(frame)

            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0

        new_faces = add_overlays(frame, faces, frame_rate)
        if new_faces != "Inconnu":
            setfaces.add(new_faces)
        
        frame_count += 1
        cv2.imshow('Video', frame)
        
        cv2.waitKey(200)
        
        if new_faces in setfaces:
            cont +=1
                  
        if new_faces is not None and new_faces != "Inconnu" and cont >=5:                  # To be improved by selecting specific faces                      
            if test1 == 0:
                MainWindow = QtWidgets.QMainWindow()
                ui = Ui_MainWindow()
                ui.setupUi(MainWindow)
                MainWindow.show()
                test1 =1
            
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
