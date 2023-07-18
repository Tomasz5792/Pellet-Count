import cv2
import numpy as np
import matplotlib.pyplot as plt

#print("Your OpenCV version is: " + cv2.__version__)

#path
path = r'C:\Users\Tomasz\OneDrive\Programing\Projects\Pellet-Count\Pellets\HDPE\HDPE_126_(1).png'

image = cv2.imread(path)

#resize image
image = cv2.resize(image,(900,900))

#grayscales image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#canny image
image = cv2.Canny(image, 30, 150, 3)

#dilate image
image = cv2.dilate(image, (1,1), iterations = 2)


(cnt, heirachy) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Pellets in image: ", len(cnt))


#shows image
window_name = "image"           # Window name in which image is displayed
cv2.imshow(window_name,image)   # Displaying the image
cv2.waitKey(0)                  # waits for user to press any key       # (this is necessary to avoid Python kernel form crashing)
cv2.destroyAllWindows()         # closing all open windows
  




