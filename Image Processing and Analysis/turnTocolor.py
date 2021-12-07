import cv2

im_gray = cv2.imread("H:/gdal/rs-data/result/ndvi.jpg", cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
cv2.imwrite('H:/gdal/rs-data/result/ndvi_color.jpg', im_color)