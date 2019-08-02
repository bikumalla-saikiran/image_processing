import cv2 
import numpy as np 
x=0
while(1):

# Read the main image 
 img_rgb = cv2.imread('stop.png')
  
# Convert it to grayscale 
 img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY) 
  
# Read the template 
 template = cv2.imread('stop1.png',0) 
  
# Store width and heigth of template in w and h 
 w, h = template.shape[::-1] 
  
 res = img_gray - template 
# Perform match operations. 
 # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
  
# Specify a threshold 
 threshold = 0.8
  
# Store the coordinates of matched area in a numpy array 
 loc = np.where( res >= threshold)  
  
# Draw a rectangle around the matched region. 
 for pt in zip(*loc[::-1]): 
    x = cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,204,153), 0) 
 print(x) 
# Show the final image with the matched area. 
 cv2.imshow('Detected',img_rgb) 
 cv2.imshow('template',template)
 cv2.imshow('res',res)
 k = cv2.waitKey(5) & 0xFF
 if k == 27: 
   break

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
