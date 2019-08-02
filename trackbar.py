import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow('result')
def nothing(x):
    pass
cv2.createTrackbar('lowh','result',0,255,nothing)
cv2.createTrackbar('highh','result',0,255,nothing)
cv2.createTrackbar('lows','result',0,255,nothing)
cv2.createTrackbar('highs','result',0,255,nothing)
cv2.createTrackbar('lowv','result',0,255,nothing)
cv2.createTrackbar('highv','result',0,255,nothing)


while True:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)
    img= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('lowh','result')
    hh=cv2.getTrackbarPos('highh','result')
    ls=cv2.getTrackbarPos('lows','result')
    hs=cv2.getTrackbarPos('highs','result')
    lv=cv2.getTrackbarPos('lowv','result')
    hv=cv2.getTrackbarPos('highv','result')

    lower= np.array([lh,ls,lv])
    higher=np.array([hh,hs,hv])

    mask=cv2.inRange(img,lower,higher)

    ##blue=cv2.countNonZero(mask)
    ##print('the number is:'+str(blue))
    
    cv2.imshow('frame',frame);
    cv2.imshow('r',mask)

    k=cv2.waitKey(5) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
