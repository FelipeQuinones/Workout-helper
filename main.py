import cv2 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import video_visual as vv
import graph_visual as gp
import recorded_df as rdf

cap_ = vv.createCamera()
df_ = rdf.createDf()

L_B = np.array([165, 156, 163])
U_B = np.array([255, 255, 255])

"""plt.ion()
figure, ax = plt.subplots(figsize=(5, 5))
line1, = ax.plot(np.linspace(0,10,50), range(0,50))
plt.title("Bar movement", fontsize=10)
plt.ylabel("Pixel trajectory")"""

i = 0
y_coord1 = [0]
y_coord2 = [0]
while(cap_.isOpened()):
    ret, frame = cap_.read()

    if ret == True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, L_B, U_B)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            if cv2.contourArea(contour) < 1000000 and cv2.contourArea(contour) > 500:
                approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                df_ = rdf.addRow(df_, contour[0][0][0], contour[0][0][1])

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

        """y_coord1.append(contour[0][0][0])
        new_y = y_coord1
        line1.set_xdata(np.linspace(0,10,50))
        line1.set_ydata(new_y)
        ax.set_xlim(i,i+50)
        figure.canvas.draw()
        figure.canvas.flush_events()
        i += 1"""

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

    

cap_.release()
cv2.destroyAllWindows()
df_.to_csv(rdf.dfPath())