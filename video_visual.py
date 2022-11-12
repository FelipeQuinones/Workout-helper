import cv2
import numpy as np

def createCamera(x=640, y=360):
    cap = cv2.VideoCapture(0)
    cap.set(3, x)
    cap.set(4, y)
    return cap
