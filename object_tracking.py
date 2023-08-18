import cv2
import time
import math

p1 = 500
p2 = 300

xcoord = []
ycoord = []

video = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSRT_create()

returned, img = video.read()

bBox = cv2.selectROI('tracking...', img, False)

tracker.init(img, bBox)

print(bBox)


def drawBox(img, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])

    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (25, 0, 255), 3, 1)

    cv2.putText(img, 'tracking', (75, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


def trajectory(img, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])
    c1 = x + int(w/2) 
    c2 = y + int(h/2)
    cv2.circle(img, (int(p1), int(p2)), 2, (0, 0, 255), 3)
    cv2.circle(img, (c1, c2), 2, (0, 0, 255), 3)
    xcoord.append(c1)
    ycoord.append(c2)

    for i in range(len(xcoord)-1):
        cv2.circle(img,(xcoord[i], ycoord[i]), 2, (0, 0, 255), 3)


while True:
    check, img = video.read()

    success, bBox = tracker.update(img)

    if success:
        drawBox(img, bBox)
    else:
        cv2.putText(img, 'lost', (75, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    trajectory(img, bBox)

    cv2.imshow("result", img)

    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

video.release()
cv2.destroyALLwindows()
