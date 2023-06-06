import cv2
import os
import datetime
import time
import numpy as np
# Se debe tener: pip install opencv-contrib-python

#def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='Camara'):
def save_frame_camera_key(device_num, flipcam, dir_path, basename, x1=500, y1=10, w1=700, h1=400, x2=500, y2=450, ext='jpg', delay=1):
       
    cap = cv2.VideoCapture(device_num)
    window_cam='Camara (C: Caputar - Q: Salir)'
    window_img='Imagen Capturada'

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    tiempo = str(time_stamp).replace('.','')
    entro = False

    #Posicion Intefaces de Captura y Visualizacion Foto
    cv2.namedWindow(window_cam, cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(window_cam, w1, h1)
    cv2.moveWindow(window_cam, x1, y1)
    cv2.namedWindow(window_img, cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(window_img, w1, h1)
    cv2.moveWindow(window_img, x2, y2)
    
    x1 = 300
    y1 = 10
    x2 = x1 + 700
    y2 = y1 + 700

    while True:
        time.sleep(0)
        ret,frame = cap.read()
        if flipcam == 1:
            frame = cv2.flip(frame, 1 )
    
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)   
        cv2.imshow(window_cam,frame)

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            #cv2.imwrite('{}_{}.{}'.format(base_path, tiempo, ext), frame, size=(256, 256, 3))
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 125, 255, cv2.THRESH_BINARY)
            ret,thresh = cv2.threshold(grayImage,70,255,0)
            #cv2.imshow('Black white image', blackAndWhiteImage)
            
            cv2.imwrite('{}_{}.{}'.format(base_path, tiempo, ext), thresh) #frame)
            
            img = cv2.imread('{}_{}.{}'.format(base_path, tiempo, ext), cv2.IMREAD_ANYCOLOR)
            refPoint = [(x1, y1), (x2, y2)]
            dim = (256,256)
            img2 = cv2.resize(img[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]], dim, interpolation = cv2.INTER_AREA)
            
            cv2.imwrite('{}_{}.{}'.format(base_path, tiempo, ext), img2)
            imgf = cv2.imread('{}_{}.{}'.format(base_path, tiempo, ext), cv2.IMREAD_ANYCOLOR) 
            cv2.imshow(window_img, imgf)

            entro = True
        elif key == ord('q'):
            break
    
    cap.release()        
    cv2.destroyWindow(window_cam)
    cv2.destroyWindow(window_img)
    #cv2.destroyWindow('trackbar')
    if entro:
        return 'screen_' + tiempo + '.' + ext
    else:
        return 'nofile'
