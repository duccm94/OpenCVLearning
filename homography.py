import cv2
import numpy as np

if __name__ == '__main__':
  im_src = cv2.imread('book1.jpg')
  pts_src = np.array([[318, 256], [534, 372], [316, 670], [73, 473]])

  pts_dst = np.array([[0,0], [299, 0], [299, 399], [0, 399]])

  h, status = cv2.findHomography(pts_src, pts_dst)

  im_out = cv2.warpPerspective(im_src, h, (300, 400))

  cv2.imshow('Source Image', im_src)
  cv2.imshow('Warped Source Image', im_out)

  cv2.waitKey(0)
