# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
photo = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480

#photo.set(3 , 640)
#photo.set(4 , 480)

# loading the mountain image
house = cv2.imread('HauntedHouse.jpg')

# resizing the mountain image as 640 X 480

#cv2.resize(house, (640,640))

while True:

    # read a frame from the attached camera
    status , frame = photo.read()

    # if we got the frame successfully
    

        # flip it

        #frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
    frame = cv2.resize(frame, (640,480))
    house = cv2.resize(house, (640,480))

        # creating thresholds
    lower_bound = np.array([104,153,70])
    upper_bound = np.array([30,30,0])

    mask = cv2.inRange(frame,lower_bound,upper_bound)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    f = np.where(f == 0,house,f)
        # thresholding image
    

        # final image
        
        # show it
    cv2.imshow('video' , frame)
    cv2.imshow("mask", f)

        # wait of 1ms before displaying another frame
    code = cv2.waitKey(1)
    if code  ==  32:
        break

# release the camera and close all opened windows
photo.release()
cv2.destroyAllWindows()
