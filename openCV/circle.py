import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype = "uint8")

(centerX, centerY) = (int(canvas.shape[1] / 2), int(canvas.shape[0] /2))
white = (255, 255, 255)

for r in range(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0, 25):
	radius = np.random.randint(5, high = 200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	pt = np.random.randint(0, high = 300, size = (2,))
	cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
