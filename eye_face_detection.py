import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap =cv2.VideoCapture(0)

while True:
    res, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for(x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_Color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (m,n,o,p) in eyes:
            cv2.rectangle(roi_Color,(m,n),(m+o,n+p),(0,255,0),2)

    cv2.imshow('frame',frame)
    k= cv2.waitKey(30) & 0xFF
    if k == 27 :
        break

cap.release()
cv2.destroyAllWindows()