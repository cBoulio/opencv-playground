import cv2
import numpy as np

cap = cv2.VideoCapture(0)
panel = np.zeros([100, 700], np.uint8)
cv2.namedWindow("panel")

def nothing(x):
    pass

cv2.createTrackbar("L - h","panel",0,179,nothing)
cv2.createTrackbar("U - h","panel",179,179,nothing)

cv2.createTrackbar("L - s","panel",0,255,nothing)
cv2.createTrackbar("U - s","panel",255,255,nothing)

cv2.createTrackbar("L - v","panel",0,255,nothing)
cv2.createTrackbar("U - v","panel",255,255,nothing)


while True:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - h", "panel")
    u_h = cv2.getTrackbarPos("U - h", "panel")
    l_s = cv2.getTrackbarPos("L - s", "panel")
    u_s = cv2.getTrackbarPos("U - s", "panel")
    l_v = cv2.getTrackbarPos("L - v", "panel")
    u_v = cv2.getTrackbarPos("U - v", "panel")

    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("panel", panel)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break
        cap.release()
        cv2.destroyAllWindows()