import cv2
import numpy as np
import cvzone
import pickle

vid = cv2.VideoCapture("carpark.mp4")

width, height = 29, 14

def checkspaces(proimg):
    flag = 0
    for pos in positionlist:
        x, y = pos
        cropimg = proimg[y:y+height, x:x+width]
        count = cv2.countNonZero(cropimg)
        cv2.putText(img, str(count), (x, y+height-7), fontFace=0,
                    fontScale=0.2, color=(10, 100, 200), thickness=0)

        if (count < 38):
            color = (0, 255, 0)
            thickness = 2
            flag += 1
        else:
            color = (0, 0, 255)
            thickness = 1

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(img,f'{flag}/{len(positionlist)}',(50,330),scale=2,thickness=2,colorT=(10,10,10))


with open('CarParkPos', 'rb') as f:
    positionlist = pickle.load(f)

while (True):

    if (vid.get(cv2.CAP_PROP_POS_FRAMES) == vid.get(cv2.CAP_PROP_FRAME_COUNT)):
        vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
    suc, img = vid.read()

    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurimg = cv2.GaussianBlur(grayimg, (3, 3), 1)
    thresholdimg = cv2.adaptiveThreshold(
        blurimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    medianimg = cv2.medianBlur(thresholdimg, 5)

    checkspaces(medianimg)

    cv2.imshow("Video", img)
    if (cv2.waitKey(100) & 0xFF == ord('a')):
        break
