import cv2
import random
import xlrd
import os 
os.environ["DISPLAY"] = ":0"

# a =  cv2.imread('media/map4.png')
# cv2.imshow('hi',a)
# cv2.waitKey(0)
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()
# for i in range(1, 2):
#     print(i)

TRAFFIC_LAMP_POS = []
MAP_NAVS = []
TRAFFIC_LAMP_COORDINATES = []
with xlrd.open_workbook('/home/luuthanh/Desktop/fuzzy-logic-project/media/toa-do2.xlsx') as book:
    sheet = book.sheet_by_index(3 - 1) 

    x_coordinate = [x for x in sheet.col_values(1)]
    y_coordinate = [y for y in sheet.col_values(2)]
    # print(x_coordinate)
    for i in range(1, len(x_coordinate)):
        MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))

    sheet = book.sheet_by_index(3 + 3)

    pos_tmp = [x for x in sheet.col_values(1)]
    for i in range(1, len(pos_tmp)):
        TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
    print("TRAFFIC LAMP POS: ", TRAFFIC_LAMP_POS)

    sheet = book.sheet_by_index(3 + 7)
    x_coordinate = [x for x in sheet.col_values(1)]
    y_coordinate = [y for y in sheet.col_values(2)]
    direction = [direction for direction in sheet.col_values(3)]
    index = [index for index in sheet.col_values(4)]

    for i in range(1, len(x_coordinate)):
        TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))
    print(TRAFFIC_LAMP_COORDINATES)
    print(type(TRAFFIC_LAMP_COORDINATES[0][0]))

# import math
# def calculate_angle(pt1, pt2):
#     neg_dir = math.atan2(pt1[1] - pt2[1], pt2[0] - pt1[0]) * 180 / math.pi
#     if neg_dir < 0:
#         neg_dir += 360
#     if neg_dir < 90:
#         dir = neg_dir + 360 - 90
#     else:
#         dir = neg_dir - 90
#     return dir
#
# def change_dir(target_dir):
#     viet = 2
#     if abs(self.dir - target_dir) > viet:
#         if self.dir > target_dir:
#             angle = self.dir_factor * float(self.dir - target_dir)
#             change_dir = angle if angle <viet else viet
#             self.dir -= change_dir
#         else:
#             angle = self.dir_factor * float(target_dir - self.dir)
#             change_dir = angle if angle < viet else viet
#             self.dir += change_dir
#     self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
#
# def find_way_direction():
#     return calculate_angle(self.x, self.y, next_nav_x, next_nav_y)
#
# # coordinat = [[977, 700],[1037,700],[1094, 690], [1106, 680],[1117, 670],[1120, 660], [1140, 650], [1140, 640]]
# # # coordinat = [[0,-2],[0,-5], [0, -6], [0, -8], [0, -10], [0, -12], [0, -14]]
# # for i, a in enumerate(coordinat):
# #     if(i == 7):
# #         break
# #     print(calculate_angle(a,coordinat[i+1]))
# # print(math.atan2(1, 0))
# def BestMonster(a):
#     return math.sin(math.radians(a))*math.cos(math.radians(a))
# #kiem tra xem neu target_dir va dir cung goc phan tu
# def check(a, b):
#     return True if BestMonster(a)*BestMonster(b) >= 0 else False
#
# print(check(1, 271))