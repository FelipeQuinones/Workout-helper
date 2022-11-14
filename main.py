import cv2 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import video_visual as vv
import graph_visual as gp
import recorded_df as rdf

cap_ = vv.createCamera()
df_ = rdf.createDf()

"""plt.ion()
figure, ax = plt.subplots(figsize=(5, 5))
line1, = ax.plot(np.linspace(0,10,50), range(0,50))
plt.title("Bar movement", fontsize=10)
plt.ylabel("Pixel trajectory")"""

i = 0
y_coord1 = [0]
y_coord2 = [0]
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
                    if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                        cv2.putText(frame1, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

                else:
                    cv2.putText(frame1, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        cv2.imshow("th1", th1)
        cv2.imshow("frame", frame1)
        cv2.imshow("gray", gray)

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

    df_ = rdf.addRow(df_, contour[0][0][0], contour[0][0][1])

cap_.release()
cv2.destroyAllWindows()
df_.to_csv(rdf.dfPath())