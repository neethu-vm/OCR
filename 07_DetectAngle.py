# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:36:30 2020

@author: chris
"""
import pytesseract
import cv2
import re

img = cv2.imread('/home/neethu/machine learning datas/Deep learning/OCR/90degree.png')
osd = pytesseract.image_to_osd(img)
osd = osd.split("\n")
osd_dict = dict()
for x in osd:
    try:
        osd_dict[x.split(":")[0]] = x.split(":")[1]
    except:
        pass
print(osd_dict)