import cv2
import os
import time
from datetime import datetime

camera = cv2.VideoCapture(0)

directorioCapturas ="../fotosPersonal"


try:
  os.stat(directorioCapturas)
except:
  os.mkdir(directorioCapturas)
  


while True:
    return_value,image = camera.read()
    gray = image
    fuente = cv2.FONT_HERSHEY_COMPLEX_SMALL
    	
    cv2.imshow('image',gray)
    
    pressed_key = cv2.waitKey(1)	
    if pressed_key& 0xFF == ord('s'):
	cv2.putText(gray, text='HOLA', org=(20,100), fontFace=fuente, fontScale=2, color=(0,255,0), thickness=1, lineType=cv2.LINE_8)
	cv2.imshow('image',gray)
        cv2.imwrite('test.jpg',image)
	cv2.waitKey(500)       
    if pressed_key& 0xFF == ord('q'):
	break
camera.release()
cv2.destroyAllWindows()
