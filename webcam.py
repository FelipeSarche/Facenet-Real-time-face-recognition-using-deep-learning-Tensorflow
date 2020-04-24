import cv2
import os
import time
import datetime

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
    try:	
    	cv2.imshow('image',gray)
    except:
	print("No se encuentra ninguna camara")
	break    
    pressed_key = cv2.waitKey(1)	
    if pressed_key& 0xFF == ord('s'):
        now = datetime.datetime.now()
	tiempoactual = now.strftime("%Y-%m-%d %H:%M:%S")
	diaactual = now.strftime("%Y-%m-%d")
	print(diaactual)
	try:
  		os.stat(directorioCapturas + "/" + diaactual)
	except:
  		os.mkdir(directorioCapturas + "/" + diaactual)
	cv2.imwrite(directorioCapturas+"/" + diaactual + "/" + tiempoactual +".jpg",image)
	cv2.putText(gray, text= tiempoactual, org=(20,100), fontFace=fuente, fontScale=2, color=(0,255,0), thickness=3, lineType=cv2.LINE_8)
	cv2.imshow('image',gray)
	cv2.waitKey(500)       
    if pressed_key& 0xFF == ord('q'):
	break
camera.release()
cv2.destroyAllWindows()
