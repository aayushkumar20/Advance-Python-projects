from lib2to3.pgen2.tokenize import _Coord
import cv2
import numpy as np
import time

cap = cv2.VideoCapture('/home/Desktop/test.mp4') #video file with path
car_cascade = cv2.CascadeClassifier('/home/Desktop/haarcascade_car.xml') #xml file with path
# I am using a video file instead of a camera feed because I don't have a camera
# If you have a camera feed, then change the cap = cv2.VideoCapture(0) to cap = cv2.VideoCapture('/dev/video0')
# I am using a macBook, please change the path to the xml file accordingly

# coordinates between two horizontal lines
# In meters
dist = 3

while True:
    ret, img  = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.8, 2)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.line(img, (coord[0][0]), coord[0][1]),(coord[1][0], coord[1][1]),(0,0,255),2) #drawing the line
    cv2.line(img, (coord[0][0]), coord[0][1]),(coord[2][0], coord[2][1]),(0,0,255),2) #drawing the line
    cv2.line(img, (coord[2][0]), coord[2][1]),(coord[3][0], coord[3][1]),(0,0,255),2) #drawing the line
    cv2.line(img, (coord[1][0]), coord[1][1]),(coord[3][0], coord[3][1]),(0,0,255),2) #drawing the line
    for (x,y,w,h) in cars:
        if(x>=coord[0][0] and x<=coord[0][1]):
            cv2.line(img, (coord[0][0]), coord[0][1]),(coord[1][0], coord[1][1]),(0,0,255),2) #drawing the line
            tim1 = time.time() #time at which the car crossed the line.
            print('Time at which car crossed the line: ', tim1)

            if (x>=coord[2][0] and y==coord[2][1]):
                cv2.line(img, (coord[2][0]), coord[2][1]),(coord[3][0], coord[3][1]),(0,0,255),2) #drawing the line
                tim2 = time.time() #time at which the car crossed the line.
                print("speed of the car: ", (tim2-tim1)/dist)
    
    cv2.imshow('img',img) #displaying the image

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()