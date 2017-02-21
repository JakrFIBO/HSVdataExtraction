import glob
import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt

#Histogram of Gradient Parameter Setup
winSize = (32,32)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 4
hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins, derivAperture, winSigma,
                        histogramNormType, L2HysThreshold, gammaCorrection, nlevels)

f = open('HSVdataEx.csv', 'w')
forwrite = str("")

HSV = ('H', 'S', 'V')
for i, col in enumerate(HSV):
    for k in range(0,256):
        wording = str(HSV[i]) + str(k)
        # print(wording)
        forwrite = forwrite + wording + ","
for i in range(0,324):
    wording = str('v') + str(i)
    forwrite = forwrite + wording + ","

forwrite = forwrite + "class"
forwrite += str("\n")

for filename in glob.iglob('boong*.jpg'):

    image_bgr = cv2.imread(filename, 1)
    height, width = image_bgr.shape[:2]
    # changing color space from BGR to HSV
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)


    # HSV Data Extraction
    for i, col in enumerate(HSV):
        histr = cv2.calcHist([image_hsv], [i], None, [256], [0, 256])
        j=0
        for k in histr :
            j = j + 1
            forwrite = forwrite + str(k[0]) + ","

    #Histogram of Gradient Data Extraction
    resized = cv2.resize(image_hsv, (32, 32))
    hist = hog.compute(resized)
    for k in range(0,len(hist)):
        forwrite = forwrite + str(hist[0][0]) + ","

    forwrite = forwrite + str("boong")
    forwrite = forwrite + str("\n")

for filename in glob.iglob('meatball*.jpg'):

    image_bgr = cv2.imread(filename, 1)
    height, width = image_bgr.shape[:2]
    # changing color space from BGR to HSV
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)


    # HSV Data Extraction
    for i, col in enumerate(HSV):
        histr = cv2.calcHist([image_hsv], [i], None, [256], [0, 256])
        j=0
        for k in histr :
            j = j + 1
            forwrite = forwrite + str(k[0]) + ","

    #Histogram of Gradient Data Extraction
    resized = cv2.resize(image_hsv, (32, 32))
    hist = hog.compute(resized)
    for k in range(0,len(hist)):
        forwrite = forwrite + str(hist[0][0]) + ","

    forwrite = forwrite + str("meatball")
    forwrite = forwrite + str("\n")

for filename in glob.iglob('mincepork*.jpg'):

    image_bgr = cv2.imread(filename, 1)
    height, width = image_bgr.shape[:2]
    # changing color space from BGR to HSV
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)


    # HSV Data Extraction
    for i, col in enumerate(HSV):
        histr = cv2.calcHist([image_hsv], [i], None, [256], [0, 256])
        j=0
        for k in histr :
            j = j + 1
            forwrite = forwrite + str(k[0]) + ","

    #Histogram of Gradient Data Extraction
    resized = cv2.resize(image_hsv, (32, 32))
    hist = hog.compute(resized)
    for k in range(0,len(hist)):
        forwrite = forwrite + str(hist[0][0]) + ","

    forwrite = forwrite + str("mincepork")
    forwrite = forwrite + str("\n")

for filename in glob.iglob('mama*.jpg'):

    image_bgr = cv2.imread(filename, 1)
    height, width = image_bgr.shape[:2]
    # changing color space from BGR to HSV
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)


    # HSV Data Extraction
    for i, col in enumerate(HSV):
        histr = cv2.calcHist([image_hsv], [i], None, [256], [0, 256])
        j=0
        for k in histr :
            j = j + 1
            forwrite = forwrite + str(k[0]) + ","

    #Histogram of Gradient Data Extraction
    resized = cv2.resize(image_hsv, (32, 32))
    hist = hog.compute(resized)
    for k in range(0,len(hist)):
        forwrite = forwrite + str(hist[0][0]) + ","

    forwrite = forwrite + str("mama")
    forwrite = forwrite + str("\n")

f.write(forwrite)
