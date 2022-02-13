import cv2
import random
import numpy as np

print('hi')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

img_counter =0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break
    elif c%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter+=1

cap.release()
cv2.destroyAllWindows()

'''
- get picture and extract the binary of the picture: a.k.a conver the picture into bits (I mostly want it automated)
in a separate program:
    - use bits and insert it into a psuedorandom generator
    - genrate randomness!




'''








































