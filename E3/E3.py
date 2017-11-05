import cv2
import numpy as np

img=cv2.imread('C:/Users/Blink/Desktop/baboon.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original',gray)
cv2.imwrite('original.jpg',gray)

box = cv2.blur(gray,(3,3))
cv2.imshow('blur',box)
cv2.imwrite('blur.jpg',box)

gauss = cv2.GaussianBlur(gray,(3,3),1.5)
cv2.imshow('GaussianBlur',gauss)
cv2.imwrite('GaussianBlur.jpg',gauss)

med = cv2.medianBlur(gray,3)
cv2.imshow('medianBlur',med)
cv2.imwrite('medianBlur.jpg',med)

