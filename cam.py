import cv2
import numpy as np
import matplotlib.pyplot as plt

cam=cv2.VideoCapture(0)
forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',forcc,20.0 ,(640,480))
while True:
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('Camera 1 Gray',gray)
    cv2.imshow('Camera 1 Real',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
out.release()
cam.release()
cv2.destroyAllWindows()