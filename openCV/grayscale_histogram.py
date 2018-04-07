from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
## cv2.calcHist()
##1. This is the image that we want to compute a
##   histogram for.
##2. channels : A list of indexes, where we specify the in-
#    dex of the channel we want to compute a histogram
#    for. To compute a histogram of a grayscale image, the
#    list would be [0]. To compute a histogram for all
#    three red, green, and blue channels, the channels list
#    would be [0,1,2].
##3. mask : If a mask is provided, a histogram will be 		    computed for masked pixels only. If we do not have a 			mask or do not want to apply one, we can just provide 			a value of None
##4. histSize : This is the number of bins we want to use
#		when computing a histogram. Again, this is a list, one
#		for each channel we are computing a histogram for.
# 		The bin sizes do not all have to be the same. Here is
#		an example of 32 bins for each channel: [32,32,32].
##5. ranges : The range of possible pixel values. Normally,
#			this is [ 0, 256 ] for each channel, but if you 			are using a
#			color space other than RGB (such as HSV), the ranges might be different.

plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)


