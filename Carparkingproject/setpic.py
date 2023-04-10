import cv2
import pickle

width, height = 29,14

try:
    with open('CarParkPos', 'rb') as f:
        positionlist = pickle.load(f)
except:
    positionlist = []


def mouseclick(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        positionlist.append((x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(positionlist):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                positionlist.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(positionlist, f)


while True:
    img = cv2.imread('whts.jpg')
    for pos in positionlist:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (10,100,200), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseclick)
    if(cv2.waitKey(1) & 0XFF == ord('a')):
        break