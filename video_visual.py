import cv2
import numpy as np

def createCamera(x=640, y=360):
    cap = cv2.VideoCapture(0)
    cap.set(3, x)
    cap.set(4, y)
    return cap

cap_ = createCamera()

while(cap_.isOpened()):
    ret, frame = cap_.read()
    frame_copy = frame.copy()
    if ret == True:

       cv2.line(frame_copy, (320, 0), (320, 360), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow("frame", frame_copy)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap_.release()
cv2.destroyAllWindows()