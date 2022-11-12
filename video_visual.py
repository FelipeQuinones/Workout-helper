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

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, th1 = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow("frame", th1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap_.release()
cv2.destroyAllWindows()