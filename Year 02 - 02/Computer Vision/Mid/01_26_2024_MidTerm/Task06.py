import numpy as np
import cv2

# Brute Foruce
print(-10-18-12+45)
print(-12-8-10)
print(-10-8-8+81)
print(-8-8-18+54)

'''
1428
1248
= -10-18-12+45, -12-8-10, -10,-8,-8,81, -8-8-18+54

1248
5, -30, 55, 20

1428 (ans)
5, 55, -30, 20

'''

# Compute
m = np.int16([[6, 9, 0, 0, 0, 9, 5, 0],
              [0, 5, 6, 9, 5, 4, 6, 0],
              [6, 5, 0, 4, 9, 0, 5, 0],
              [0, 9, 0, 6, 4, 6, 0, 9],
              [9, 0, 0, 9, 0, 4, 4, 9],
              [0, 6, 5, 6, 0, 0, 6, 0],
              [6, 0, 9, 0, 0, 6, 4, 9]])

kernel = np.int16([[0, -2, 0],
                   [-2, 9, -2],
                   [0, -2, 0]])

res = cv2.filter2D(m, -1, kernel)
print('\n\n', res)