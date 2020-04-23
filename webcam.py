import cv2
camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = image
    fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(gray, text='HOLA', org=(20,100), fontFace=fuente, fontScale=1, color=(0,255,0), thickness=4, lineType=cv2.LINE_8)	
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()
