import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.withKey[0]

flipped = cv2.flip(image, 1) ## flip horizonatlly
cv2.imshow("Flipped Horizontally", flipped)
cv2.withKey[0]

##flip val direction
## 0	   vertically
##	1		horizontally
## -1 		both axis

