import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True,
                help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

(b,g,r) = image[0,0] ##opencv stores colors as B G R
print("Pixel at (0,0) - Red: %d, Green: %d, Blue: %d"%(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0] ##opencv stores colors as B G R
print("Pixel at (0,0) - Red: %d, Green: %d, Blue: %d"%(r,g,b))

corner = image[0:100,0:100]
cv2.imshow("Corner",corner)

image[0:100, 0:100] = (0, 250, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

#print("width: %d pixels"% (image.shape[1]))
#print("height: %d pixels"% (image.shape[0]))
#print("channels: %d"% (image.shape[2]))


#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.imwrite("newimage.jpg", image)
