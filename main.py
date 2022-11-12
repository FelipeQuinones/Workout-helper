import cv2
import video_visual as vv
import graph_visual as gp
import recorded_df as rdf

cap_ = vv.createCamera()

while(cap_.isOpened()):
    ret, frame = cap_.read()

    if ret == True:
       cv2.line(frame, (320, 0), (320, 360), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow("frame", frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        break

cap_.release()
cv2.destroyAllWindows()