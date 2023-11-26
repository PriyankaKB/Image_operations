# import cv2 module
import cv2
import sys
  
# resd the image
input1 = sys.argv[1]
img = cv2.imread(input1)
  
# shape prints the tuple (height,weight,channels)
print(img.shape)
  
# img will be a numpy array of the above shape
print(img)
