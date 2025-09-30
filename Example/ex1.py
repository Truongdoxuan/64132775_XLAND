# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 10:46:55 2025

@author: dxt81
"""

"Ví dụ chương 2 trang 6 tạo bản sao và xem xét sự thay đổi so với ảnh trước"
import cv2
img = cv2.imread("D:\\64132775_XLAND\\Images\\pikachu.png")

""" show ảnh 1
cv2.imshow("pikachu", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""tạo bản sao ảnh 2"""
img2 = img.copy()

"""thay đổi giá trị pixel trong ảnh màu"""
height = img2.shape[0]
width = img2.shape[1]
for i in range(height // 2):
    for j in range(width //2):
        img2[i,j] = (0,0,0)
cv2.imshow("pikachu2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
