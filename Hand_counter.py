import cv2
import time
import os
import HandTrackingModule as htm

dispW  =640
dispH= 480

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
# cap.set(cv2.CAP_PROP_FPS, 30)
#cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))



Ptime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4,8,12,16,20]

while True:
    sucees , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw= False)
    print(lmList)
    
    if len(lmList) != 0:
        fingers =[]
        for id in range(0,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)
            
    
    
    cTime = time.time()
    fps =1/(cTime-Ptime)
    Ptime = cTime 

    cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),3)

    cv2.imshow("image",img)
    cv2.moveWindow('Image',0,0)
    

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()   