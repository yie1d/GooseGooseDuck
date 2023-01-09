import time

import pyautogui
# Size(width=2560, height=1440)
# x=132, y=257
# x=2197, y=262
# x=125, y=1189
# x=2202, y=1191
# 1.
# x=134, y=257
# x=624, y=256
# x=621, y=463
#
# 2.
# x=657, y=256
# x=1145, y=261
#
# 3.
# x=1183, y=257
# x=1668, y=260
#
# 4.
# x=1704, y=253
# x=2200, y=257
#
# 5.
# x=129, y=495
# x=621, y=496
#
# 9.
# x=128, y=733
#
#
# 大的 2170 935
# x=131, y=253
# x=2201, y=254
# x=126, y=1189
# x=2202, y=1188
#
# 横间隔  25/30
# x=625, y=949
# x=652, y=947
#
# 竖间隔  25
# x=625, y=949
# x=626, y=974
#
# 宽  500
# x=125, y=944
# x=627, y=950
# 高  200
# x=126, y=733
# x=125, y=944
# while True:
#     print(pyautogui.position())
#     time.sleep(1)
import cv2

img = cv2.imread('1.jpg')
height, width, _ = img.shape
box_height, box_width = int(height * 0.1459), int(width * 0.194)

x = int(height * 0.09)
for _ in range(4):
    y = int(width * 0.1)
    for _ in range(4):
        cv2.rectangle(img, (x, y), (x + box_width, y + box_height), (0, 255, 0))
        y = y + box_height + 30
    x = x + box_width + 30
cv2.imwrite('2.jpg', img)
