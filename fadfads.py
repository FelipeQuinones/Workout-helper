import cv2
import numpy as np
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))
x = int(1280/2)
while(cap.isOpened()):
    ret, frame = cap.read()
    frame_copy = frame.copy()
    if ret == True:

       cv2.line(frame_copy, (x, 0), (x, 720), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow("frame", frame_copy)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()