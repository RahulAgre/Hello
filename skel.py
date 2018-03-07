import cv2
import numpy as np

img = cv2.imread('core.png',0)
cv2.imshow("core", img)
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

#ret, img = cv2.threshold(img, 127, 255, 0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done = False

while (not done):
    eroded = cv2.erode(img, element)
    cv2.imshow("eroded", eroded)
    cv2.waitKey(0)
    temp = cv2.dilate(eroded, element)
    cv2.imshow("temp", temp)
    cv2.waitKey(0)
    temp = cv2.subtract(img, temp)
    cv2.imshow("temp", temp)
    cv2.waitKey(0)
    skel = cv2.bitwise_or(skel, temp)
    cv2.imshow("skel", skel)
    cv2.waitKey(0)

    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True
cv2.imshow("skel", skel)
cv2.waitKey(0)
cv2.destroyAllWindows(
