#Image Segmentation with Watershed Algorithm
#https://docs.opencv.org/3.4/d3/db4/tutorial_py_watershed.html

#try https://pyimagesearch.com/2015/11/02/watershed-opencv/  may help to get it to work

import cv2
import numpy as np
import matplotlib.pyplot as plt
#print("Your OpenCV version is: " + cv2.__version__)        #Makes sure OpenCV is working

#path
path = r'C:\Users\Tomasz\OneDrive\Programing\Projects\Pellet-Count\Pellets\HDPE\HDPE_126_(1).png'

#loads image
image = cv2.imread(path)

#resize image
image = cv2.resize(image,(900,900))

#grayscales image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#thresh image
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


#Cant get the markers to work?
###

###

#shows image
window_name = "image"                   # Window name in which image is displayed
cv2.imshow("thresh",thresh)             # Displaying the image
cv2.waitKey(0)                       
cv2.imshow("sure bg",sure_bg)   
cv2.waitKey(0)                       
cv2.imshow("sure fg",sure_fg)     
cv2.waitKey(0)                 
cv2.imshow("unknown",unknown)     
cv2.waitKey(0)   
cv2.imshow("markers",markers)     
cv2.waitKey(0)                  
cv2.destroyAllWindows()                 # closing all open windows
  




