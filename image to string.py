# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

import cv2
import pytesseract

#Reading the image using CV
img = cv2.imread('/home/neethu/Desktop/testocr.png') 
start = time.time()
print("Text extracted using Tesseract\n")
#Extracting the text from image
text = pytesseract.image_to_string(img)
print(text)
end = time.time()
t = round(end-start,2)
print("\nTime Taken   ", t, " (s)")