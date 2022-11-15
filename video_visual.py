import cv2
import numpy as np

def createCamera(x=640, y=360):
    cap = cv2.VideoCapture(0)
    cap.set(3, x)
    cap.set(4, y)
    return cap
cap_ = createCamera()

L_B = np.array([165, 156, 163])
U_B = np.array([255, 255, 255])

"""L_B = np.array([130, 123, 76])
U_B = np.array([255, 255, 255])"""

while(cap_.isOpened()):
    ret, frame = cap_.read()

    if ret == True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, L_B, U_B)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            if cv2.contourArea(contour) < 10000000:
                approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5

                if len(approx) == 4:
                    x1 ,y1, w, h = cv2.boundingRect(approx)
                    aspectRatio = float(w)/h
                    print(contour)
                    if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                        cv2.putText(frame, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

                else:
                    cv2.putText(frame, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                    print(contour)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap_.release()
cv2.destroyAllWindows()