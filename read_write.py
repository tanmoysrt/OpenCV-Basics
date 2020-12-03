import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('2.jpg',cv2.IMREAD_COLOR)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows


# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.plot([80,100],[50,100],[30,100],[10,10],'r',linewidth=5)
# plt.show()

cv2.imwrite('test.jpg',img)