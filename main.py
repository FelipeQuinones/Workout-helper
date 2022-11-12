import cv2 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import video_visual as vv
import graph_visual as gp
import recorded_df as rdf

cap_ = vv.createCamera()
df_ = rdf.createDf()

plt.ion()
figure, ax = plt.subplots(figsize=(5, 5))
line1, = ax.plot(np.linspace(0,10,50), range(0,50))
plt.title("Bar movement", fontsize=10)
plt.ylabel("Pixel trajectory")

i = 0

while(cap_.isOpened()):
    ret, frame = cap_.read()
    i += 1
    if ret == True:
        cv2.line(frame, (320, 0), (320, 360), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
        cv2.imshow("frame", frame)

        rdf.addRow(df_, "peso1", "peso2")

        min_val = i
        max_val = 50+i
        new_y = range(min_val,max_val)
        line1.set_xdata(np.linspace(0,10,50))
        line1.set_ydata(new_y)
        ax.set_xlim(min_val,max_val)
        figure.canvas.draw()
        figure.canvas.flush_events()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap_.release()
cv2.destroyAllWindows()
df_.to_csv(rdf.dfPath())