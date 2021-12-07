import cv2
cap=cv2.VideoCapture(0)
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    sucess,img=cap.read()
    faces=faceCascade.detectMultiScale(img,1.3,5)
    for (x,y,w,h) in faces:
        ROI=img[y:y+h,x:x+w]
        blur=cv2.GaussianBlur(ROI,(100,100),0)
        img[y:y+h,x:x+w]=blur
    if faces ==():
        cv2.putText(img,"No Face Found!",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    cv2.imshow("Face Blur",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()