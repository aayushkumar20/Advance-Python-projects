import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(img):
    gray_img=cv2.cvtColor(img,0)
    barcode=decode(gray_img)

    for obj in barcode:
        points=obj.polygon
        (x,y,w,h)=obj.rect
        pts=np.array(points,np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,255),3)
        barcodeData=obj.data.decode("utf-8")
        barcodeType=obj.type
        string="Data"+str(barcodeData)+" | Type "+str(barcodeType)
        cv2.putText(frame,string,(x,y-10),2,0.8,(0,255,0),2,cv2.LINE_AA)
        print("Barcode:"+barcodeData+" | Type : "+barcodeType)

cap=cv2.Videocapture(0)
while True:
    ret,frame=cap.read()
    decoder(frame)
    cv2.imshow("image",frame)
    if code==ord('q'):
        break
