import cv2;
import numpy;
"""
img = cv2.imread("6361226.webp");
cv2.imshow("window",img);
cv2.waitKey(0);
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

cv2.imshow("window",gray);
cv2.waitKey(0);
print(img.shape);
print(img)
"""

img = cv2.imread("6361226.webp");
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cropped =img_gray[1:2,1:2];
#cv2.imshow("window",cropped)
#cv2.waitKey(0);
print(img.shape)
print(img)
img=img.reshape(200,14808);
cv2.imshow("windows",img);
cv2.waitKey(0);