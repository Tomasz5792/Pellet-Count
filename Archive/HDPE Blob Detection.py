#Cant get this to work

import cv2
import numpy as np
#import matplotlib.pyplot as plt
#print("Your OpenCV version is: " + cv2.__version__)

#path
path = r'C:\Users\Tomasz\OneDrive\Programing\Projects\Pellet-Count\Pellets\HDPE\HDPE_126_(1).png'

image = cv2.imread(path,0)

#resize image
image = cv2.resize(image,(900,900))

#image_copy = image.copy()

#set up detector with default parameters
blob_detector = cv2.SimpleBlobDetector_create()

#detect blobs
keypoint_info = blob_detector.detect(image)

#highlight blobs
#blobs = cv2.drawKeypoints(image,keypoint_info,np.array([]),(0,0,255),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
blobs = cv2.drawKeypoints(image,keypoint_info,np.array([]))

#shows image
cv2.imshow("image",blobs)       # Displaying the image
cv2.waitKey(0)                  # waits for user to press any key       # (this is necessary to avoid Python kernel form crashing)
cv2.destroyAllWindows()         # closing all open windows
  




