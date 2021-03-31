#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
Healthy = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_healthy.xml')
bacterial_spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Bacterial_spot_.xml')
Early_blight = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Early_blight.xml')
Late_blight = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Late_blight.xml')
Leaf_mold = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Leaf_Mold.xml')
Septoria_leaf_spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Septoria_leaf_spot.xml')
Spider_mites = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Spider_mites.xml')
Target_Spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Target_Spot.xml')
Mosaic_virus = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Mosaic_virus.xml')
Curl_Virus = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Tomato_Yellow_Curl_Virus.xml')


# In[ ]:


import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

Healthy = cv2.CascadeClassifier('C:\\Users\\HP\\haarcascade_healthy.xml')
bacterial_spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Bacterial_spot_.xml')
Early_blight = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Early_blight.xml')
Late_blight = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Late_blight.xml')
Leaf_mold = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Leaf_Mold.xml')
Septoria_leaf_spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\haarcascade_Septoria_leaf_spot.xml')
Spider_mites = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Spider_mites.xml')
Target_Spot = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Target_Spot.xml')
Mosaic_virus = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Mosaic_virus.xml')
Curl_Virus = cv2.CascadeClassifier('C:\\Users\\HP\\project\\hasscascade_Tomato_Yellow_Curl_Virus.xml')
log.basicConfig(filename='webcam.log',level=log.INFO)
color = (255,0,255)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    healthy = Healthy.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )

    
    for (x, y, w, h) in healthy:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Healthy",(x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(healthy):
        anterior = len(healthy)
        log.info("Healthy: "+str(len(healthy))+" at "+str(dt.datetime.now()))

    
    cv2.imshow('Video', frame)
    
    disease1 = bacterial_spot.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
    for (ax, ay, aw, ah) in disease1:
        cv2.rectangle(frame, (ax, ay), (ax+aw, ay+ah), (255, 0, 0), 2)
        cv2.putText(frame, "Bacterial Spot",(ax,ay-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease1):
        anterior = len(disease1)
        log.info("Bacterial Spot: "+str(len(disease1))+" at "+str(dt.datetime.now()))

    
    cv2.imshow('Video', frame)
    
    
    disease2 = Early_blight.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
    
    for (bx, by, bw, bh) in disease2:
        cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (0, 0, 255), 2)
        cv2.putText(frame, "Early Blight",(bx,by-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease2):
        anterior = len(disease2)
        log.info("Early Bligt: "+str(len(disease2))+" at "+str(dt.datetime.now()))
    
    cv2.imshow('Video', frame)
    
    disease3 = Late_blight.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
    
    for (cx, cy, cw, ch) in disease1:
        cv2.rectangle(frame, (cx, cy), (cx+cw, cy+ch), (255, 255, 0), 2)
        cv2.putText(frame, "Late blight",(cx,cy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease3):
        anterior = len(disease3)
        log.info("Late blight: "+str(len(disease3))+" at "+str(dt.datetime.now()))
    
    
    cv2.imshow('Video', frame)

    
    disease4 = Leaf_mold.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
    
    
    for (dx, dy, dw, dh) in disease4:
        cv2.rectangle(frame, (dx, dy), (dx+dw, dy+dh), (0, 255, 255), 2)
        cv2.putText(frame, "Leaf Mold",(dx,dy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease4):
        anterior = len(disease4)
        log.info("Leaf Mold: "+str(len(disease4))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)
    
    disease5 = Septoria_leaf_spot.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
        
    for (ex, ey, ew, eh) in disease5:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 255, 255), 2)
        cv2.putText(frame, "Septoria leaf spot",(ex,ey-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease5):
        anterior = len(disease5)
        log.info("Septoria leaf spot: "+str(len(disease5))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)
    
    
    disease6 = Spider_mites.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
        
    for (fx, fy, fw, fh) in disease6:
        cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)
        cv2.putText(frame, "Spider Mites",(fx,fy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease6):
        anterior = len(disease6)
        log.info("Spider Mites: "+str(len(disease6))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)
    
    disease7 = Target_Spot.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
        
    for (gx, gy, gw, gh) in disease7:
        cv2.rectangle(frame, (gx, gy), (gx+gw, gy+gh), (100, 100, 0), 2)
        cv2.putText(frame, "Target Spot",(gx,gy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease7):
        anterior = len(disease7)
        log.info("Target Spot: "+str(len(disease7))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)
    
    
    disease8 = Mosaic_virus.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
    
        
    for (hx, hy, hw, hh) in disease8:
        cv2.rectangle(frame, (hx, hy), (hx+hw, hy+hh), (0, 100, 100), 2)
        cv2.putText(frame, "Mosaic Virus",(hx,hy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease8):
        anterior = len(disease8)
        log.info("Mosaic Virus: "+str(len(disease8))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)
    
    
    disease9 = Curl_Virus.detectMultiScale( gray, scaleFactor=1.1,  minNeighbors=5, minSize=(30, 30) )
    
        
    for (ix, iy, iw, ih) in disease9:
        cv2.rectangle(frame, (ix, iy), (ix+iw, iy+ih), (100, 100, 100), 2)
        cv2.putText(frame, "Curl Virus",(ix,iy-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    if anterior != len(disease9):
        anterior = len(disease9)
        log.info("Curl Virus: "+str(len(disease9))+" at "+str(dt.datetime.now()))
        
    
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()

