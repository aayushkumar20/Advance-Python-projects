import os
import cv2
import numpy as np
import mediapipe as mp
#import all the modules properly.
#verify the imported modules.
#Initialize the MediaPipe graph.
mp_selfie_segmentation=mp.solutions.selfie_segmentation
selfie_segmentation=mp_selfie_segmentation.SelfieSegmentation(mode1_selection=1)
#storing the image path and listing it throught the directory.
image_path='Images' #Change the path and directory as per your image
#in case you're using the webcamera then please write the path as '0'
images=os.listdir(image_path)
image_index=0
bg_image=cv2.imread(os.path.join(image_path,images[image_index]))
#Make sure that the image is in the same directory as the script.
#Initialize the background removal.
cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,frame=cap.read()
    frame=cv2.resize(frame,1)
    height,width,chanel=frame.shape
    RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=selfie_segmentation.process(RGB)
    mask=results.segmentation_mask
    condition=np.stack((results.segmentation_mask,)*3,axis=-1)>0.6
    bg_image=cv2.resize(bg_image,(width,height))
    output_image=np.where(condition,frame,bg_image)
    cv2.imshow('output',output_image)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('d'):
        if image_index!=len(images)-1:
            image_index+=1
        else:
            image_index=0
        bg_image=cv2.imread(image_path+'/'+images[image_index])
cap.release()
cv2.destroyAllWindows()