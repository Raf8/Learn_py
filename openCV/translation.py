import numpy as np
import argparse 
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
##[[1,0,tx][0,1,ty]]
##[1,0,tx] tx-> +ve -> shift right by tx
##         tc-> -ve -> shift left by tx
## ty-> -ve up; +ve down
M = np.float32([[1, 0, 25], [0, 1, 50]])##translation matrix
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]]) ## or imutils.translate(image, -50, -90)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)


