import cv2
path_image_car = "/media/thanhln11/sda1_mnt/BTL_XLTTM/self-driving-car-main/media/car_player.png"
img = cv2.imread(path_image_car)
img = cv2.resize(img, (28,42))
cv2.imwrite("/media/thanhln11/sda1_mnt/BTL_XLTTM/self-driving-car-main/media/car_32_24.png", img)