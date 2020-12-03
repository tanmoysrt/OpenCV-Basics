import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red=np.array([130,80,80])
    uper_red=np.array([255,255,255])

    mask = cv2.inRange(hsv,lower_red,uper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)


    kernel = np.ones((5,5),np.uint8)/225
    erosion= cv2.erode(mask,kernel,iterations=1)
    dilation = cv2.dilate(mask, kernel,iterations=1)
    
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    # kernel = np.ones((15,15),np.float32)/225
    # smoothed= cv2.filter2D(res,-1,kernel)

    # blur = cv2.GaussianBlur(res,(15,15),0)
    # median = cv2.medianBlur(res,15)
    # bilateral=cv2.bilateralFilter(res,15,75,75)

    # cv2.imshow('hsv',hsv)
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    # cv2.imshow('smoothed',smoothed)
    # cv2.imshow('blur',blur)
    # cv2.imshow("median",median)
    # cv2.imshow("bilateral",bilateral)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()
cap.release()
