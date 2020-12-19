# import cv2
# import os 
# import xlrd
# os.environ["DISPLAY"] = ":0"

# path = "/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map_ledaihanh.png"

# toa_do = "/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/abc.xlsx"
# image = cv2.imread(path)
# image = cv2.resize(image, (940,640))
# print(image.shape)
# # w,h,_ = image.shape
# # image = cv2.resize(image,(200,350))
# with xlrd.open_workbook(toa_do) as book:
#     sheet = book.sheet_by_name('Map06')
#     x_coordinate = [x for x in sheet.col_values(1)]
#     y_coordinate = [y for y in sheet.col_values(2)]


# x_coordinate = [int(int(x_coordinate[i])) for i in range(1, len(x_coordinate))]
# y_coordinate = [int(int(y_coordinate[i])) for i in range(1, len(y_coordinate))]


# for i in range(len(x_coordinate)):
#     # print(y_coordinate[i])
#     center_coordinates = (int(x_coordinate[i]),int(y_coordinate[i]))
#     radius = 5
#     color = (255,0,0)
#     thickness = -1
#     image = cv2.circle(image, center_coordinates, radius, color, thickness)

# cv2.imshow("",image)
# cv2.waitKey(10000)
