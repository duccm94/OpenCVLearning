import cv2

src = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE)

thresh = 127
maxValue = 255

th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO_INV)
cv2.imwrite("thresh-result.jpg", dst)