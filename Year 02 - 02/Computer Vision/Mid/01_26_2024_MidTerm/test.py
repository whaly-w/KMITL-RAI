import cv2 
import numpy as np

img = cv2.imread('Source/gray.bmp')

ret, green = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# plt.imshow(green, cmap= 'gray')

ret, red = cv2.threshold(img, 140, 255, cv2.THRESH_TOZERO)
red = red - green
# plt.imshow(red, cmap= 'gray')

# Recolor image
red_gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
green_gray = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)

# red
r = np.uint8(red_gray * 0)
g = np.uint8(red_gray * 0)
b = np.uint8(red_gray * 1)
red_rgb = cv2.merge([r, g, b])

# green
r = np.uint8(green_gray * 0)
g = np.uint8(green_gray * 1)
b = np.uint8(green_gray * 0)
green_rgb = cv2.merge([r, g, b])

result = red_rgb + green_rgb
# result_rgb = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

print(green_gray[50][200])
cv2.imshow('name', result)
cv2.waitKey(0)
