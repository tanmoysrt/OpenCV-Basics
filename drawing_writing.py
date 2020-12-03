import numpy as np
import cv2

img=cv2.imread('2.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(15,15),(100,100),(255,255,255),4)

cv2.rectangle(img,(15,15),(100,100),(255,0,0),4)

cv2.circle(img,(150,150),50,(0,0,255),4)
cv2.circle(img,(150,150),45,(0,255,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(255,255,0),5)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Hello World",(50,115),font,1,(255,255,255),2,cv2.LINE_4)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
