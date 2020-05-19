import argparse
import sys
import time
from PIL import Image
import face
import os 
import cv2
import time
from keras.preprocessing import image
from keras.applications.inception_v3 import  preprocess_input
from keras.models import load_model
import numpy as np
# from yolo import YOLO
#  .............................................................................................. #
#  ............................. CHARGEMENT DES MODELES ET LABELS   ............................. # 
#  .............................................................................................. #
#model_path_fire="xxxxx.h5"                  # Model Fire
#model_path_personal="xxxxx.h5"              # Model Personal
#model_path_suspect="xxxxx.h5"               # Model Suspect
#model_path_mvt="xxxxx.h5"                   # Model Movement

#classes_path = "classes.txt"                # Labels du modele de classification 
#image_path="images_test/4.bmp"              # Image de test   
#top_n=1
#model = load_model(model_path_fire)        # Chargement du modele de classification "Fire" 

#test_anchors = 'yolo_anchors.txt'                                    # Modele de localisation de cles 
#test_classes = 'key_classes.txt'                                     # Labels du modele de localiation
#new_model = YOLO(test_classes,test_anchors,'yolo_key.h5')           # Cargement du modele de localisation

# ................... Chargement des noms de classes pour la classification ..................... #
#classes_cat_dog = []
#with open(classes_path, 'r') as f:
#    classes_cat_dog = list(map(lambda x: x.strip(), f.readlines()))
#font = cv2.FONT_HERSHEY_COMPLEX 

# ...................... Fonction daffichage des nom de visages sur les box ..................... #
def add_overlays(frame, faces, frame_rate):
    name=None
    if faces is not None:
        for face in faces:
            face_bb = face.bounding_box.astype(int)
            cv2.rectangle(frame,
                          (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
                          (0, 255, 0), 2)
            if face.name is not None:
                name=face.name
                       
                cv2.putText(frame, face.name, (face_bb[0], face_bb[3]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            thickness=2, lineType=2)

    cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                thickness=2, lineType=2)
    return name
# ............................................................................................... #

def main(args):
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0
    face_recognition = face.Recognition()
    start_time = time.time()

    if args.debug:
        print("Debug enabled")
        face.debug = True
    test = 0
    while True:
        new_faces=None
        faces=None
        frame=None        
        if test==0:
            print("..............................................................................................")
            print("..........                    FACE AUTHENTIFICATION                     ......................")
            print("..........         Please look at the camera to be identified           ......................")
            print("..............................................................................................")
            print("                                                                                              ")
        #print("..........          To start the system, press any keyboard button !    ......................")
        #cv2.waitKey(0)
		
        # Capture frame-by-frame
        if test==0:
            video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
        # ................... Face recognition ..................... #
        faces = face_recognition.identify(frame)

        # Check our current fps
        end_time = time.time()
        if (end_time - start_time) > fps_display_interval:
            frame_rate = int(frame_count / (end_time - start_time))
            start_time = time.time()
            frame_count = 0

        new_faces=add_overlays(frame, faces, frame_rate)
        
        frame_count += 1
        #cv2.destroyAllWindows()
        cv2.imshow('Visage', frame)
        cv2.waitKey(200)
		
        if new_faces is not None and new_faces != "Inconnu":                  # To be improved by selecting specific faces                      
            print(".. Hello "+str(new_faces)+", you are well identified, you can select your Edge AI module..")
            print("1: ****************                  Fire/Smoke detection                 ****************")
            print("2: ****************                Suspect object detection               ****************")
            print("3: ****************                   Ations recognition                  ****************")
            print("4: ****************                         EXIT                          ****************")
            #value = input("***********                   Select an option:                                 \n")
            value = input("Choisir une option:\n") 
		
            """if(int(value)==1):
                video_capture.release()
                cv2.destroyAllWindows()
                test=0
                cap = cv2.VideoCapture(0)
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
                    if ret == True:
	                # To be completed by the prediction within your model
			# ...
                        cv2.putText(frame, 'Fire detection', (50, 100), font, 2, (255,0,0), 6, cv2.LINE_AA)
                        cv2.imshow('Fire Model',frame)
                        if cv2.waitKey(25) & 0xFF == ord('q'):          # Press Q on keyboard to  exit
                            break
                    else: 
                        break
                cap.release()
                cv2.destroyAllWindows()
            
            elif (int(value)==2):
                video_capture.release()
                cv2.destroyAllWindows()
                test=0
                cap = cv2.VideoCapture(0)
                while(True):
                    # Capture frame-by-frame
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
                    # To be completed by the prediction within your model
                    # ...
                    cv2.putText(frame, 'Suspect detection', (10, 100), font, 2, (255,0,0), 6, cv2.LINE_AA)
                    cv2.imshow('Suspect Model',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif (int(value)==3):
                video_capture.release()
                cv2.destroyAllWindows()
                test=0
                cap = cv2.VideoCapture(0)
                while(True):
                    # Capture frame-by-frame
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
                    # To be completed by the prediction within your model
                    # ...
                    cv2.putText(frame, 'Action recognition', (10, 100), font, 2, (255,0,0), 6, cv2.LINE_AA)
                    cv2.imshow('Movement Model',frame)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif (int(value)==4):
                video_capture.release()
                test=0
                sys.exit(0)
            else :
                continue """
        if new_faces == "Inconnu":
            print ("cheh")
        else :
            test=1  
    
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
