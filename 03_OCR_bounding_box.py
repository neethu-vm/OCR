# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:39:43 2020

@author: chris
"""

import cv2
import pytesseract

img = cv2.imread('/home/neethu/Desktop/noiseimage.png')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b[0])
    ix=int(b[1])
    iy=h-int(b[2])
    x = int(b[3])
    y = h-int(b[4])
    img = cv2.rectangle(img, (ix, iy), (x,y), (255, 0, 0), 1)

# cv2.imshow('img', img)
# cv2.waitKey(0)

import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes")
plt.show()
cv2.imwrite("/home/neethu/Desktop/noiseimage_boxing.png",img)

