import numpy as np
import argparse
import os
import time
import imutils
import cv2
import pyttsx3
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=False,help="path to input image")
ap.add_argument("o","--output",required=True,help="path to output directory")
ap.add_argument("y","--yolo",required=True,help="path to yolo directory")
ap.add_argument("-c","--confidence",type=float,default=0.5,help="minimum probability to filter weak detections")
ap.add_argument("-t","--threshold",type=float,default=0.3,help="threshold when applyong non-maxima suppression")
args=vars(ap.parse_args())
engine=pyttsx3.init()
labelsPath=os.path.sep.join([args["yolo"],"cocohelmet.names"])
LABELS=open(labelsPath).read().strip().split("\n")
np.random.seed(42)
COLORS=np.random.randint(0,255,size=(len(LABELS),3),dtype="uint8")

weightsPath=os.path.sep.join([args["yolo"],"yolo-obj_2400.weights"])
configPath=os.path.sep.join([args["yolo"],"yolo-obj_2400.cfg"])

print("[INFO] loading...")
net=cv2.dnn.readNetFromDarknet(configPath,weightsPath)
ln=net.getLayerNames()
ln=[ln[i[0]-1] for i in net.getUnconnectedOutLayers()]
vs=cv2.VideoCapture(0)
writer=None
(W,H)=(None,None)
try:
    prop=cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
    else cv2.CAP_PROP_FRAME_COUNT
    total=int(vs.get(prop))
except:
    print("could not determine # of frames in video")
    print("no approx. completion time can be provided")
    total= -1
while True:
    _,frame=vs.read()
    print("[INFO] In frame")
    if W is None or H is None:
        (H,W)=frame.shape[:2]
    blob=cv2.dnn.blobFromImage(frame,1/255.0,(416,416),swapRB=True,crop=False)
    net.setInput(blob)
    start=time.time()
    layerOutputs=net.forward(ln)
    end=time.time()
    boxes=[]
    confidences=[]
    classIDs=[]
    for output in layerOutputs:
        for detection in output:
            scores=detection[5:]
            classID=np.argmax(scores)
            confidence=scores[classID]
            if confidence>args["confidence"]:
                box=detection[0:4]*np.array([W,H,W,H])
                (centerX,centerY,width,height)=box.astype("int")
                x=int(centerX-(width/2))
                y=int(centerY-(height/2))
                boxes.append([x,y,int(width),int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    idxs=cv2.dnn.NMSBoxes(boxes,confidences,args["confidence"],args["threshold"])
    if len(idxs)>0:
        for i in idxs.flatten():
            (x,y)= (boxes[i][0],boxes[i][1])
            (w,h)= (boxes[i][2],boxes[i][3])
            color= [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            text="{}: {:.4f}".format(LABELS[classIDs[i]],confidences[i])
            cv2.putText(frame,text,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)
            textname=LABELS[classIDs[i]]
            print("found",textname)
            a=str(textname)
            engine.say("found"+a)
        engine.runAndWait()
    if writer is None:
        fourcc=cv2.VideoWriter_fourcc(*"MJPG")
        writer=cv2.VideoWriter(args["output"],fourcc,1,(frame.shape[1],frame.shape[0]),True)
        if total>0:
            elap=(end-start)
            print("[INFO] single frame took {:.4f} seconds".format(elap))
            print("[INFO] estimated total time to finish: {:.4f}".format(elap*total))
    writer.write(frame)
print("Cleaning cache...")
writer.release()
vs.release()