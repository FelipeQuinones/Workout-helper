import cv2
import numpy as np

def createCamera(x=640, y=360):
    cap = cv2.VideoCapture(0)
    cap.set(3, x)
    cap.set(4, y)
    return cap
cap_ = createCamera()

while(cap_.isOpened()):
    ret, frame1 = cap_.read()
    ret, frame2 = cap_.read()

    if ret == True:
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        inverse = cv2.bitwise_not(gray)
        _, th1 = cv2.threshold(inverse, 200, 230, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            if cv2.contourArea(contour) < 1000 and cv2.contourArea(contour) > 800:
                approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
                cv2.drawContours(frame1, [approx], 0, (0, 0, 0), 5)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5

                if len(approx) == 4:
                    x1 ,y1, w, h = cv2.boundingRect(approx)
                    aspectRatio = float(w)/h
                    print(contour[0])
                    if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                        cv2.putText(frame1, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

                else:
                    cv2.putText(frame1, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                    print(contour[0][0][0])

        cv2.imshow("th1", th1)
        cv2.imshow("frame", frame1)
        cv2.imshow("gray", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap_.release()
cv2.destroyAllWindows()