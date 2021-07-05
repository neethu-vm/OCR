# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:26:53 2020

@author: chris
"""

import cv2
import numpy as np


img = cv2.imread('/home/neethu/Desktop/noiseimage.png')



# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)

#thresholding  to make black and white  
def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]





gray = get_grayscale(img)
noise = remove_noise(gray)
thresh = threshold(noise)




import matplotlib.pyplot as plt

plt.subplot(221); plt.title("gray"); plt.imshow(gray, cmap='gray');
plt.subplot(222); plt.title("noise"); plt.imshow(noise);



plt.show()

import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = thresh
print("binary ocr\n")
print(pytesseract.image_to_string(img))

img = noise
print("\n\nnoise removed ocr\n")
print(pytesseract.image_to_string(img))

img = gray
print("\n\ngreyscale removed ocr\n")
print(pytesseract.image_to_string(img))




