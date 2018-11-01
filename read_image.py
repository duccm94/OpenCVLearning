import cv2

im = cv2.imread("blob.jpg", cv2.IMREAD_UNCHANGED)
print("Size %s, type %s" % (im.shape, im.dtype))