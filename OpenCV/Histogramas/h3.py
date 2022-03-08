import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile("everest.jpg"))
bgr_planes = cv.split(img)
histSize = 256
histRange = (0, 256)
accumulate = False
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)

hist_w = 512
hist_h = 400
bin_w = int(round(hist_w/histSize))
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
for i in range(1, histSize):
	cv.line(histImage, (bin_w * (i - 1), hist_h - int(np.round(b_hist[i - 1]))),
			(bin_w * (i), hist_h - int(np.round(b_hist[i]))),
			(255, 0, 0), thickness=1)
	cv.line(histImage, (bin_w * (i - 1), hist_h - int(np.round(g_hist[i - 1]))),
			(bin_w * (i), hist_h - int(np.round(g_hist[i]))),
			(0, 255, 0), thickness=1)
	cv.line(histImage, (bin_w * (i - 1), hist_h - int(np.round(r_hist[i - 1]))),
			(bin_w * (i), hist_h - int(np.round(r_hist[i]))),
			(0, 0, 255), thickness=1)

cv.imshow('Source image', img)
cv.imshow('calcHist Demo', histImage)
cv.waitKey()